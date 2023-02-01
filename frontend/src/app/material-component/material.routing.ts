import { Routes } from '@angular/router';
import { HomeComponent } from './ara-module/home/home.component';
import { CoursesPageComponent } from './ara-module/courses-page/courses-page.component';
import { UniversityComponent } from './ara-module/university/university.component';
import { CoursePredictionComponent } from './ara-module/course-prediction/course-prediction.component';
import { CompareCourseTrendComponent } from './ara-module/compare-course-trend/compare-course-trend.component';

export const MaterialRoutes: Routes = [
  //ARA
  {
    path: 'university',
    component: UniversityComponent
  },
  {
    path: 'home',
    component: HomeComponent
  },
  {
    path: 'course',
    component: CoursesPageComponent
  },
  {
    path: 'trend-prediction',
    component: CoursePredictionComponent
  },
  {
    path: 'compare',
    component: CompareCourseTrendComponent
  }
];
