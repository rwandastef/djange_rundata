import { environment } from './../../environments/environment';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UitslagenService {
// TODO: define http options

uitslagenUrl = environment.apiUrl + 'uitslagen'
constructor(private httpClient: HttpClient) { }

public getWelcome(): Observable<any>{
  return this.httpClient.get<any>(this.uitslagenUrl + '/example')
}
}
