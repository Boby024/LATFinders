import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CoursePredictionComponent } from './course-prediction.component';

describe('CoursePredictionComponent', () => {
  let component: CoursePredictionComponent;
  let fixture: ComponentFixture<CoursePredictionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CoursePredictionComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CoursePredictionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
