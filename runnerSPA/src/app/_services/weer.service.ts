import { HttpClient } from '@angular/common/http';
import { environment } from './../../environments/environment';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WeerService {
// TODO: define http options

uitslagenUrl = environment.apiUrl + 'weer'
constructor(private httpClient: HttpClient) { }

public getWeer(): Observable<any>{
  return this.httpClient.get<any>(this.uitslagenUrl + '/list')
}

public getWeerRegression(): Observable<any>{
  return this.httpClient.get<any>(this.uitslagenUrl);
}

}
