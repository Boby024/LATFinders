import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import {RouterModule, RouterOutlet, Routes} from "@angular/router";
import {HttpClientModule} from "@angular/common/http";
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {PlotlyModule} from "angular-plotly.js";
import * as PlotlyJS from 'plotly.js-dist-min';
import {MatFormFieldModule} from "@angular/material/form-field";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {MatInputModule} from "@angular/material/input";
import {MatListModule} from "@angular/material/list";
import { AnalyticComponent } from './analytic/analytic.component';
import {MatSelectModule} from "@angular/material/select";
import {MatButtonModule} from '@angular/material/button';
import {MatSidenavModule} from "@angular/material/sidenav";
import {MatIconModule} from "@angular/material/icon";
import {MatToolbarModule} from "@angular/material/toolbar";
import { CompareCourseTrendComponent } from './compare-course-trend/compare-course-trend.component';
import {MatRadioModule} from "@angular/material/radio";
import {MatProgressSpinnerModule} from "@angular/material/progress-spinner";
import { CoursePredictionComponent } from './course-prediction/course-prediction.component';

PlotlyModule.plotlyjs = PlotlyJS;
const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'compare-courses', component: CompareCourseTrendComponent},
  { path: 'course-prediction', component: CoursePredictionComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoginComponent,
    AnalyticComponent,
    CompareCourseTrendComponent,
    CoursePredictionComponent,
  ],
  imports: [
    BrowserModule,
    RouterOutlet,
    RouterModule.forRoot(routes),
    HttpClientModule,
    BrowserAnimationsModule,
    PlotlyModule,
    MatFormFieldModule,
    ReactiveFormsModule,
    MatInputModule,
    MatListModule,
    MatSelectModule,
    MatButtonModule,
    MatSidenavModule,
    MatIconModule,
    MatToolbarModule,
    MatRadioModule,
    MatProgressSpinnerModule,
    FormsModule
  ],
  exports: [RouterModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
