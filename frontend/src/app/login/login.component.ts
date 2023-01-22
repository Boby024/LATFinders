import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from "@angular/forms";
import {Router} from "@angular/router"
import { MatSnackBar } from '@angular/material/snack-bar';

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
    private fb: FormBuilder,
    private router: Router,
    private _snackBar: MatSnackBar
  ) { }

  ngOnInit(): void {
  }
  doLogin() {
    let username = this.user.controls.username.value;
    let password = this.user.controls.username.value;
    if (username === "admin" && password === "admin") {
      this.router.navigate(['/']);
    } else {
      this._snackBar.open("Wrong password!", "OK");
    }
  }

}
