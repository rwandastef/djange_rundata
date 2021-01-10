import { UitslagenService } from './../../_services/uitslagen.service';
import { Component, OnInit } from '@angular/core';
import { AnalysedUitslag } from './analysedUitslag'

@Component({
  selector: 'app-analysedUitslagen',
  templateUrl: './analysedUitslagen.component.html',
  styleUrls: ['./analysedUitslagen.component.scss']
})
export class AnalysedUitslagenComponent implements OnInit {

  analyse: AnalysedUitslag;
  math = Math;

  constructor(private uitslagenService: UitslagenService) { }

  ngOnInit() {
    this.analyse = new AnalysedUitslag()
    this.getAnalyed();
  }

  public getAnalyed(){
    const sub = this.uitslagenService.getAnalysedUitslagen().subscribe( (response: AnalysedUitslag) =>{
      this.analyse = response;
      console.log(this.getAnalyed)
    }
     , err => console.log(err))
  }

}
