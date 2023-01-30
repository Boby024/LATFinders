import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { Course, Uni } from '../../model/main';
import { MainService } from '../../service/main.service';

@Component({
  selector: 'app-courses-with-compare-mode',
  templateUrl: './courses-with-compare-mode.component.html',
  styleUrls: ['./courses-with-compare-mode.component.css']
})
export class CoursesWithCompareModeComponent implements OnInit {
  uni?: Uni;
  is_uni_selected = false;
  course?: Course;
  unis: Uni[] = [];
  courses: Course[] = [];
  public plot?: Plotly.PlotlyDataLayoutConfig;
  compareMode: number = 1;
  is_course_selected = false;
  @Output() showMoreDetail = new EventEmitter<Course | undefined>();

  constructor(private mainService: MainService) { }

  ngOnInit(): void {
    this.getUnis();
  }
  getUnis() {
    this.mainService.getUnis().subscribe((data) => {
      this.unis = data;
    });
  }
  setUni(e: any) {
    const value = e.value;
    const uniID = value.id;
    this.is_uni_selected = true;
    this.getCoursesByUniID(uniID);
  }
  setCourse(e: any) {
    const value = e.value;
    this.course = value;
    const courseID = value.id;
    this.is_course_selected = true;
    this.getCourseRatingsPlotted(courseID,this.compareMode);
  }
  setCompareMode(e: any) {
    const value = e.value;
    const compareMode = value;
    if (this.course) {
      this.getCourseRatingsPlotted(this.course?.id, compareMode);
    }
  }
  getCoursesByUniID(uniID: number) {
    this.mainService.getCoursesByUniID(uniID).subscribe((data) => {
      this.courses = data;
    });
  }
  getCourseRatingsPlotted(course_id: number,compare_mode:number=1) {
    this.mainService.getCourseRatingsPlotted(course_id,compare_mode).subscribe((data) => {
      this.plot = data;
      this.setLayoutConfig();
    });
  }
  setLayoutConfig() {
    //this.plot!.layout!.width = 600;
  }
}
