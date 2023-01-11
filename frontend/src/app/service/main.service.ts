import { Injectable } from '@angular/core';
import {environment} from "../../environments/environment.prod";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Course} from "../model/main";

@Injectable({
  providedIn: 'root'
})
export class MainService {
  private main = environment.root

  constructor(private http:HttpClient) { }

  getCourses(): Observable<Course>{
    return this.http.get<Course>(`${this.main}/courses`)
  }

  getRatingPlotted(): Observable<any>{
    return this.http.get<any>(`${this.main}/plot_ratings`)
  }
}
