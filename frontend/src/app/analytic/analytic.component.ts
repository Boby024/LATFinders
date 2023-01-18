import {Component, OnInit} from '@angular/core';
import {MainService} from "../service/main.service";
import {AnalyticQuery, Course, SearchQuery, Uni} from "../model/main";

@Component({
  selector: 'app-analytic',
  templateUrl: './analytic.component.html',
  styleUrls: ['./analytic.component.css']
})
export class AnalyticComponent implements OnInit {
  // @Input() item = '';
  // searchQuery = { query: ""};

  uni?: Uni;
  is_uni_selected = true;
  course?: Course;
  unis: Uni[] = [];
  courses: Course[] = [];
  public ratingsPlot: any;
  is_rating = true;

  constructor(
    private mainService: MainService
  ) { }

  ngOnInit(): void {
    this.getUnis();
  }

  getUnis() {
    this.mainService.getUnis().subscribe((data) => {
      this.unis = data;
    });
  }

  /*
  onKeyUniName(event: any) {
    this.searchQuery.query = (event.target as HTMLInputElement).value;
    this.filterUnis(this.searchQuery);
  }
  filterUnis(s: SearchQuery) {
    this.mainService.filterUnis(s).subscribe((data) => {
      this.unis = data;
    });
  }*/

  setUnis(e: any) {
    const value = e.value;
    const uniID = value.id;
    this.is_uni_selected = false;

    this.getCoursesByUniID(uniID);
  }

  setCourse(e: any) {
    const value = e.value;
    const courseID = value.id;

    this.getRatingPlotted(courseID);
  }

  getCoursesByUniID(uniID: number) {
    this.mainService.getCoursesByUniID(uniID).subscribe((data) => {
      this.courses = data;
    });
  }

  getRatingPlotted(course_id: number) {
    this.mainService.getRatingPlotted(course_id).subscribe((data) => {
      this.ratingsPlot = data;
      this.is_rating = false;
    });
  }
}
