import { Component, Input, OnChanges, OnInit } from '@angular/core';
import { Course } from '../../model/main';
import { MainService } from '../../service/main.service';

@Component({
  selector: 'app-courses-detailed',
  templateUrl: './courses-detailed.component.html',
  styleUrls: ['./courses-detailed.component.css']
})
export class CoursesDetailedComponent implements OnInit, OnChanges {
  
  @Input() course?: Course;
  courses: Course[] = [];
  public plot?: Plotly.PlotlyDataLayoutConfig;
  @Input() compareMode: number = 1;
  
  constructor(private mainService: MainService) { }

  ngOnInit(): void {

  }
  ngOnChanges() {
    if (this.course) {
      this.getCourseRatingsPlotted(this.course.id, this.compareMode);
    }
  }

  getCourseRatingsPlotted(course_id: number,compare_mode:number=1) {
    this.mainService.getCourseRatingsDetailedPlotted(course_id,compare_mode).subscribe((data) => {
      this.plot = data;
    });
  }
}
