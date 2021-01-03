import { HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-SingleDigit',
  templateUrl: './SingleDigit.component.html',
  styleUrls: ['./SingleDigit.component.scss']
})
export class SingleDigitComponent implements OnInit {

  temp: File;
  imgURL: any;
  files: FileList;
  digitSelected: boolean;
  id: number;
  subId: number;
  width = 0;
  height = 0;
  top = 0;
  left = 0;
  style: any;
  imagePath: any;
  message: string;
  rotationAmount = 0;
  urlString : string;

  constructor() { }

  ngOnInit() {
  }

  onFilesSelected(evt: Event) {
    this.files = (evt.target as HTMLInputElement).files;
    const reader = new FileReader();
    this.imagePath = this.files;
    reader.readAsDataURL(this.files[0]);
    reader.onload = (_event) => {
      this.imgURL = reader.result;
    };
    this.digitSelected = true;
  }

  public cancel() {
    this.digitSelected = false;
  }

  public upload() {
    const formData = new FormData();
    const file = this.files[0];
    formData.append('files', file, file.name);
    const headers = new HttpHeaders();
    headers.append('Content-Type', 'multipart/form-data');


    // if (this.subId === 0) {
    //   this.httpClient
    //   .post( this.urlString + this.id.toString(), formData, { headers })
    //   .subscribe(() =>
    //     window.location.reload(), err => this.alertify.error(err));
    //   return;
    // } else {
    //   this.httpClient
    //   .post(this.urlString + this.id.toString() + '/' + this.subId.toString(), formData, { headers })
    //   .subscribe(() =>
    //       window.location.reload(), err => this.alertify.error(err));
    // }
  }
}
