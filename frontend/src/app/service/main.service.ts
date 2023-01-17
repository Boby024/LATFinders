import { Injectable } from '@angular/core';
import {environment} from "../../environments/environment.prod";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Course, SearchQuery, Uni} from "../model/main";

@Injectable({
  providedIn: 'root'
})
export class MainService {
  private main = environment.root

  constructor(private http:HttpClient) { }

  filterUnis(s: SearchQuery):Observable<Uni[]>{
    return this.http.get<Uni[]>(`${this.main}/filter_unis?query=${s.query}`)
  }

  filterCourses(s: SearchQuery):Observable<Course[]>{
    console.warn(s);

    return this.http.get<Course[]>(`${this.main}/filter_courses?uni_id=${s.id}&query=${s.query}`)
  }

  getUnis(): Observable<Uni[]>{
    return this.http.get<Uni[]>(`${this.main}/unis`)
  }

  getCourses(): Observable<Course>{
    return this.http.get<Course>(`${this.main}/courses`)
  }

  getRatingPlotted(): Observable<any>{
    return this.http.get<any>(`${this.main}/plot_ratings`)
  }
}
