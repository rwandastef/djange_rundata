import { WeerService } from './../../_services/weer.service';
import { Weer } from './../weer';
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-WeerList',
  templateUrl: './WeerList.component.html',
  styleUrls: ['./WeerList.component.scss']
})
export class WeerListComponent implements OnInit {


  dataSource: MatTableDataSource<Weer>;
  displayedColumns: string[] = ['dateAndId', 'temperature', 'dayNumber'];

  @ViewChild(MatSort, {static: true}) sort: MatSort;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;
  constructor(private weerService: WeerService) { }

  ngOnInit() {
    this.getWeerList();
  }

  public getWeerList(){
    const sub = this.weerService.getWeer().subscribe((result: Weer[]) => {
      console.log(result);
      this.dataSource = new MatTableDataSource<Weer>(result);
      this.dataSource.filterPredicate = (data: any, filter) => {
        const dataStr = JSON.stringify(data).toLowerCase();
        return dataStr.indexOf(filter) != -1; };
      this.dataSource.sort = this.sort;
      this.dataSource.sort = this.sort;
      this.dataSource.paginator = this.paginator;
    }, err => console.log(err)
      );
  }

}
