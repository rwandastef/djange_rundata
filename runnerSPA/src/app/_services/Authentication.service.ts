import { EventEmitter, Injectable, Output } from '@angular/core';
import { Observable, Subject, of as observableOf } from 'rxjs';

@Injectable({
  providedIn: 'root'
})


export class AuthenticationService {

  @Output() getLoggedInName: EventEmitter<any> = new EventEmitter();

  login(): Observable<boolean> {
    this.getLoggedInName.emit(true);
    return observableOf(true);
  }


}
