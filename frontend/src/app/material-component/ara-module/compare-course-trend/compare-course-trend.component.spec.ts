import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CompareCourseTrendComponent } from './compare-course-trend.component';

describe('CompareCourseTrendComponent', () => {
  let component: CompareCourseTrendComponent;
  let fixture: ComponentFixture<CompareCourseTrendComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CompareCourseTrendComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CompareCourseTrendComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
