import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NewTestCompComponent } from './new-test-comp/new-test-comp.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { AnalyticComponent } from './analytic/analytic.component';
import { UniNumberOfRatingsComponent } from './charts/uni-number-of-ratings/uni-number-of-ratings.component';
import { CoursesPageComponent } from './courses-page/courses-page.component';
import { CoursesWithCompareModeComponent } from './charts/courses-with-compare-mode/courses-with-compare-mode.component';
import { PlotlyModule } from 'angular-plotly.js';
import * as PlotlyJS from 'plotly.js-dist-min';
import { MatFormFieldModule } from '@angular/material/form-field';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { MatSelectModule } from '@angular/material/select';
import { MatButtonModule } from '@angular/material/button';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { LayoutModule } from '@angular/cdk/layout';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatIconModule } from '@angular/material/icon';
import { UniversityComponent } from './university/university.component';
import { MatCardModule } from '@angular/material/card';
import { FlexLayoutModule } from '@angular/flex-layout';
import { CoursesDetailedComponent } from './charts/courses-detailed/courses-detailed.component';
import { CompareCourseTrendComponent } from './compare-course-trend/compare-course-trend.component';
import { CoursePredictionComponent } from './course-prediction/course-prediction.component';
import {MatRadioModule} from "@angular/material/radio";
import { MatProgressSpinnerModule } from "@angular/material/progress-spinner";

PlotlyModule.plotlyjs = PlotlyJS;

@NgModule({
  declarations: [
    NewTestCompComponent,
    HomeComponent,
    LoginComponent,
    AnalyticComponent,
    UniversityComponent,
    UniNumberOfRatingsComponent,
    CoursesPageComponent,
    CoursesWithCompareModeComponent,
    CoursesDetailedComponent,
    CompareCourseTrendComponent,
    CoursePredictionComponent
  ],
  imports: [
    CommonModule,
    PlotlyModule,
    MatFormFieldModule,
    ReactiveFormsModule,
    MatInputModule,
    MatListModule,
    MatSelectModule,
    MatButtonModule,
    MatSnackBarModule,
    LayoutModule,
    MatToolbarModule,
    MatSidenavModule,
    MatIconModule,
    MatCardModule,
    FlexLayoutModule,
    MatRadioModule,
    MatProgressSpinnerModule,
    FormsModule
  ],
  exports: [
    NewTestCompComponent
  ]
})
export class AraModuleModule { }
