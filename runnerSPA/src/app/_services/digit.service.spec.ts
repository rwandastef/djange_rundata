/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { DigitService } from './digit.service';

describe('Service: Digit', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [DigitService]
    });
  });

  it('should ...', inject([DigitService], (service: DigitService) => {
    expect(service).toBeTruthy();
  }));
});
