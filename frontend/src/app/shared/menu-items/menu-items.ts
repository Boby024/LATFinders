import { Injectable } from '@angular/core';

export interface Menu {
  state: string;
  name: string;
  type: string;
  icon: string;
}

const MENUITEMS = [
  { state: 'university', name: 'Ara Homepage', type: 'link', icon: 'av_timer' },
  { state: 'course', name: 'Course Analysis', type: 'link', icon: 'library_books' },
  { state: 'compare', name: 'Compare Courses', type: 'link', icon: 'compare' },
  { state: 'trend-prediction', name: 'Trend Prediction', type: 'link', icon: 'bar_chart' }
];

@Injectable()
export class MenuItems {
  getMenuitem(): Menu[] {
    return MENUITEMS;
  }
}
