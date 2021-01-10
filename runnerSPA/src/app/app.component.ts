import { Router } from '@angular/router';
import { AuthenticationService } from './_services/Authentication.service';
import { Component, OnChanges, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'runnerSPA';
  isLogedIn=false;

  constructor(private authenticationService: AuthenticationService, private router: Router) {}


  ngOnInit() {
    this.isLogedIn = false;
    this.router.navigate(['']);
    this.authenticationService.getLoggedInName.subscribe(logedIn =>this.changeBool(logedIn) );
  }

  private changeBool(lg: boolean): void {
    this.isLogedIn = lg;
}
}
