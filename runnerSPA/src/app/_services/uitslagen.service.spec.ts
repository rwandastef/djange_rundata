/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { UitslagenService } from './uitslagen.service';

describe('Service: Uitslagen', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [UitslagenService]
    });
  });

  it('should ...', inject([UitslagenService], (service: UitslagenService) => {
    expect(service).toBeTruthy();
  }));
});
