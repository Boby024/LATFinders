import {Component, OnInit} from '@angular/core';
import {MainService} from "../service/main.service";
import {Course, SearchQuery, Uni} from "../model/main";

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

  constructor(
    private mainService: MainService
  ) { }

  ngOnInit(): void {
    this.getUnis();

    this.getRatingPlotted();
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

  setCourses(e: any) {
    const value = e.value;
    const s = {id: value.id, query: value.name};
    this.is_uni_selected = false;

    this.filterCourses(s)
  }

  filterCourses(s: SearchQuery) {
    this.mainService.filterCourses(s).subscribe((data) => {
      this.courses = data;
    });
  }

  getRatingPlotted() {
    this.mainService.getRatingPlotted().subscribe((data) => {
      this.ratingsPlot = data;
      console.warn(this.ratingsPlot);
    });
  }
}
