/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { WeerListComponent } from './WeerList.component';

describe('WeerListComponent', () => {
  let component: WeerListComponent;
  let fixture: ComponentFixture<WeerListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WeerListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WeerListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
