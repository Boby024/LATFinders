import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CoursesDetailedComponent } from './courses-detailed.component';

describe('CoursesDetailedComponent', () => {
  let component: CoursesDetailedComponent;
  let fixture: ComponentFixture<CoursesDetailedComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CoursesDetailedComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CoursesDetailedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
