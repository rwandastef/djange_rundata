import { UitslagenService } from './../../_services/uitslagen.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-HomePage',
  templateUrl: './HomePage.component.html',
  styleUrls: ['./HomePage.component.scss']
})
export class HomePageComponent implements OnInit {

  constructor(private uitslagenService: UitslagenService) { }

  ngOnInit() {
    this.getExampleTextApi();
  }

  public getExampleTextApi(){
    const sub = this.uitslagenService.getWelcome().subscribe(x => console.log(x),
      err => console.log(err) )
  }

}
