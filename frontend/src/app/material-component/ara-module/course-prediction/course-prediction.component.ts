import { Component, OnInit } from '@angular/core';
import {MainService} from "../service/main.service";
import {FormBuilder, Validators} from "@angular/forms";
import {Course, Uni} from "../model/main";

@Component({
  selector: 'app-course-prediction',
  templateUrl: './course-prediction.component.html',
  styleUrls: ['./course-prediction.component.css']
})
export class CoursePredictionComponent implements OnInit {
  unis: Uni[] = [];
  courses: Course[] = [];
  public predictionPlottedDetail: any = undefined;
  startSearching = false;

  public predictionInfo =  this.fb.group({
    uni_id: [null, Validators.required],
    course_id: [null, Validators.required]
  });

  constructor(
    private mainService: MainService,
    private fb: FormBuilder
  ) { }

  fbTrigger() {
    this.predictionInfo.valueChanges.subscribe(data => {
      if (data.uni_id) {
        this.getCoursesByUniID(data.uni_id);
      }
    });
  }

  ngOnInit(): void {
    this.getUnis();
    this.fbTrigger();
  }

  getUnis() {
    this.mainService.getUnis().subscribe((data) => {
      this.unis = data;
    });
  }

  getCoursesByUniID(uniID: number) {
    this.mainService.getCoursesByUniID(uniID).subscribe((data) => {
      this.courses = data;
    });
  }

  predict() {
    this.startSearching = true;

    this.mainService.getCoursePrediction(this.predictionInfo.value).subscribe(
      (data) => {
        this.predictionPlottedDetail = data;
      },
      (error) => {
        // this.showErrorMessage = true;
      }
    );
    this.startSearching = false;
  }
}