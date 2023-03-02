import { Routes } from '@angular/router';
import { HomeComponent } from './ara-module/home/home.component';
import { CoursesPageComponent } from './ara-module/courses-page/courses-page.component';
import { UniversityComponent } from './ara-module/university/university.component';
import { CoursePredictionComponent } from './ara-module/course-prediction/course-prediction.component';
import { CompareCourseTrendComponent } from './ara-module/compare-course-trend/compare-course-trend.component';
import { AboutUsComponent } from './ara-module/about-us/about-us.component';
import { ContactUsComponent } from './ara-module/contact-us/contact-us.component';

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
  },
  {
    path: 'about-us',
    component: AboutUsComponent
  },
  {
    path: 'contact-us',
    component: ContactUsComponent
  }
];
