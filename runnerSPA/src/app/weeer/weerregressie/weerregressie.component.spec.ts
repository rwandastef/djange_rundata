/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { WeerregressieComponent } from './weerregressie.component';

describe('WeerregressieComponent', () => {
  let component: WeerregressieComponent;
  let fixture: ComponentFixture<WeerregressieComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WeerregressieComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WeerregressieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
