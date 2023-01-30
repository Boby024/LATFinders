import { Component, OnInit } from '@angular/core';
import { Course } from '../model/main';
import { MainService } from '../service/main.service';

@Component({
  selector: 'app-courses-page',
  templateUrl: './courses-page.component.html',
  styleUrls: ['./courses-page.component.css']
})
export class CoursesPageComponent implements OnInit {
  detailedCourse?: Course;
  compareMode: number = 1;
  
  constructor() { }

  ngOnInit(): void {
  }

  log(event: any) {
    this.detailedCourse = event.course;
    this.compareMode = event.compareMode;
  }

  
}
