import { Component, OnInit } from '@angular/core';
import {Course, Uni} from "../model/main";
import {MainService} from "../service/main.service";
import {FormBuilder, Validators} from "@angular/forms";

@Component({
  selector: 'app-compare-course-trend',
  templateUrl: './compare-course-trend.component.html',
  styleUrls: ['./compare-course-trend.component.css']
})
export class CompareCourseTrendComponent implements OnInit {
  unis1: Uni[] = [];
  courses1: Course[] = [];
  unis2: Uni[] = [];
  courses2: Course[] = [];
  public trendPlotted: any = undefined;
  public trendPlottedDetailed: any = undefined;
  startSearching = false;
  showErrorMessage = false;

  public compareInfo =  this.fb.group({
    uni_id1: [null, Validators.required],
    course_id1: [null, Validators.required],
    uni_id2: [null, Validators.required],
    course_id2: [null, Validators.required],
    // type: ['1'],
    date: ['2016-12-31'],
    mode: [null]
  });

  constructor(
    private mainService: MainService,
    private fb: FormBuilder
  ) { }

  fbTrigger() {
    this.compareInfo.valueChanges.subscribe(data => {
      if (data.uni_id1) {
        this.getCoursesByUniID(data.uni_id1, 1);
      }
      if (data.uni_id2) {
        this.getCoursesByUniID(data.uni_id2, 2);
      }
    });
  }

  ngOnInit(): void {
    this.getUnis();
    this.fbTrigger();
  }

  getUnis() {
    this.mainService.getUnis().subscribe((data) => {
      this.unis1 = data;
      this.unis2 = data;
    });
  }

  getCoursesByUniID(uniID: number, f: number) {
    this.mainService.getCoursesByUniID(uniID).subscribe((data) => {
      if (f === 1) {
        this.courses1= data;
      }
      if (f === 2) {
        this.courses2= data;
      }
    });
  }

  compareDefault() {
    this.startSearching = true;
    this.showErrorMessage = false;
    this.trendPlotted = undefined;
    this.mainService.getCompareCourseDefault(this.compareInfo.value).subscribe(
      (data) => {
      this.trendPlotted = data;
      },
      (error) => {
        this.showErrorMessage = true;
      }
    );

    this.startSearching = false;
  }

  compareWithMode() {
    this.mainService.getCompareCourseMode(this.compareInfo.value).subscribe(
      (data) => {
        this.trendPlottedDetailed = data;
      },
      (error) => {
        // this.showErrorMessage = true;
      }
    );
  }
}
