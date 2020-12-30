/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { WeerService } from './weer.service';

describe('Service: Weer', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [WeerService]
    });
  });

  it('should ...', inject([WeerService], (service: WeerService) => {
    expect(service).toBeTruthy();
  }));
});
