import { Component, OnInit } from '@angular/core';
import { Course, Uni } from 'src/app/model/main';
import { MainService } from 'src/app/service/main.service';

@Component({
  selector: 'app-uni-number-of-ratings',
  templateUrl: './uni-number-of-ratings.component.html',
  styleUrls: ['./uni-number-of-ratings.component.css']
})
export class UniNumberOfRatingsComponent implements OnInit {
  uni?: Uni;
  is_uni_selected = false;
  unis: Uni[] = [];
  public uniCoursesPlot?: Plotly.PlotlyDataLayoutConfig;

  constructor(
    private mainService: MainService
  ) {
   }

  ngOnInit(): void {
    this.getUnis();
  }

  getUnis() {
    this.mainService.getUnis().subscribe((data) => {
      this.unis = data;
    });
  }

  setUni(uniElement: any) {
    const value = uniElement.value;
    const uniID = value.id;
    this.is_uni_selected = true;

    this.getNumberOfRatingsOfUniPlotted(uniID);
  }

  setLayoutConfig() {
    //this.uniCoursesPlot!.layout!.width = 600;
  }
  getNumberOfRatingsOfUniPlotted(uniID:number) {
    this.mainService.getNumberOfRatingsPlotted(uniID).subscribe((data) => {
      this.uniCoursesPlot = data;
    });
  }

}
