import { Injectable } from '@angular/core';
import {environment} from "../../environments/environment.prod";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {AnalyticQuery, Course, SearchQuery, Uni} from "../model/main";

@Injectable({
  providedIn: 'root'
})
export class MainService {
  private main = environment.root

  constructor(private http:HttpClient) { }

  getUnis(): Observable<Uni[]>{
    return this.http.get<Uni[]>(`${this.main}/unis`)
  }

  getCoursesByUniID(uniID: number):Observable<Course[]>{
    return this.http.get<Course[]>(`${this.main}/courses_by_uni_id?uni_id=${uniID}`)
  }

  filterUnis(s: SearchQuery):Observable<Uni[]>{
    return this.http.get<Uni[]>(`${this.main}/filter_unis?query=${s.query}`)
  }

  filterCourses(s: SearchQuery):Observable<Course[]>{
    return this.http.get<Course[]>(`${this.main}/filter_courses?uni_id=${s.id}&query=${s.query}`)
  }

  getCourses(): Observable<Course>{
    return this.http.get<Course>(`${this.main}/courses`)
  }

  getRatingPlotted(course_id: number): Observable<any>{
    return this.http.get<any>(`${this.main}/plot_ratings?course_id=${course_id}`)
  }

  getNumberOfRatingsPlotted(uni_id: number): Observable<any>{
    return this.http.get<any>(`${this.main}/unis/plot_number_of_ratings_by_uni_id?uni_id=${uni_id}`)
  }
}
