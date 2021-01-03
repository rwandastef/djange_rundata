import { WeerAnalyse } from './../weerAnalyse';
import { WeerService } from './../../_services/weer.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-weerregressie',
  templateUrl: './weerregressie.component.html',
  styleUrls: ['./weerregressie.component.scss']
})
export class WeerregressieComponent implements OnInit {

  weerAnalyse: WeerAnalyse;

  constructor(private weerService: WeerService) { }

  ngOnInit() {
    this.getAnalysed();
  }

  public getAnalysed(){
    const sub = this.weerService.getWeerRegression().subscribe((response: WeerAnalyse) =>
    {
      this.weerAnalyse = response;
      console.log(this.weerAnalyse);
    })

  }

}
