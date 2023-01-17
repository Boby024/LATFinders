import { Component, OnInit } from '@angular/core';
import {FormBuilder, Validators} from "@angular/forms";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public user = this.fb.group({
    username: [null, Validators.required],
    password: [null, Validators.required],
  });
  constructor(
    private fb: FormBuilder
  ) { }

  ngOnInit(): void {
  }

}
