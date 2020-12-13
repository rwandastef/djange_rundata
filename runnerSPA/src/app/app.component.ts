import { Component, OnChanges } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnChanges {
  title = 'runnerSPA';
  isLogedIn = false;

  public ngOnChanges() {
    this.isLogedIn = (sessionStorage.getItem('logedIn')=== 'true');
    console.log('íets');
  }
}
