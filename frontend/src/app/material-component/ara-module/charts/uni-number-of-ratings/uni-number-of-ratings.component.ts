import { Component, OnInit } from '@angular/core';
import { Uni } from '../../model/main';
import { MainService } from '../../service/main.service';

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
  isBarChart = true;

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
    this.uni = value;
    this.is_uni_selected = true;

    this.getNumberOfRatingsOfUniPlotted(uniID,2);
  }

  setLayoutConfig() {
    //this.uniCoursesPlot!.layout!.width = 600;
  }
  getNumberOfRatingsOfUniPlotted(uniID:number,compare_mode:number) {
    this.mainService.getNumberOfRatingsPlotted(uniID,compare_mode).subscribe((data) => {
      this.uniCoursesPlot = data;
    });
  }
  toBarChart() {
    if (this.uni) {
      this.getNumberOfRatingsOfUniPlotted(this.uni?.id, 1)
      this.isBarChart = true;
    }
  }
  toPieChart() {
    if (this.uni) {
      this.getNumberOfRatingsOfUniPlotted(this.uni?.id, 1)
      this.isBarChart = false;
    }
  }
}
