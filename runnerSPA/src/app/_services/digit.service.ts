import { environment } from './../../environments/environment';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DigitService {
// TODO: define http options

singleDigitUrl = environment.apiUrl + 'singledigit'
constructor(private httpClient: HttpClient) { }

public uploadDigit(digitFile: File): Observable<any>{
  const formData = new FormData();
  formData.append('files', digitFile, digitFile.name);
  const headers = new HttpHeaders();
  headers.append('Content-Type', 'multipart/form-data');
  return this.httpClient.post<any>(this.singleDigitUrl + '/upload_digit', formData, { headers })
}
}
