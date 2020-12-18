import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/_services/Authentication.service';

@Component({
  selector: 'app-landingPage',
  templateUrl: './landingPage.component.html',
  styleUrls: ['./landingPage.component.scss']
})
export class LandingPageComponent implements OnInit {

  constructor(private router: Router, private as: AuthenticationService) { }

  ngOnInit() {

  }

  public startApp(){
    this.as.login().subscribe();
    this.router.navigate(['home']);
  }
}
