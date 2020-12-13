import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-landingPage',
  templateUrl: './landingPage.component.html',
  styleUrls: ['./landingPage.component.scss']
})
export class LandingPageComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  public startApp(){
    sessionStorage.setItem('logedIn', 'true');
    this.router.navigate(['home']);
  }
}
