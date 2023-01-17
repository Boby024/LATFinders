import { Component, OnInit } from '@angular/core';
import {MainService} from "../service/main.service";
import {Course} from "../model/main";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  public courses: Course | undefined;
  public ratingsPlot: any;

  constructor(
    private mainService: MainService
  ) { }

  ngOnInit(): void {
    // this.getCourse();
  }

  getCourse() {
    this.mainService.getCourses().subscribe((data) => {
      this.courses = data;
      console.warn(this.courses);
    });

    this.getRatingPlotted();
  }

  getRatingPlotted() {
    this.mainService.getRatingPlotted().subscribe((data) => {
      this.ratingsPlot = data;
      console.warn(this.ratingsPlot);
    });
  }
}
