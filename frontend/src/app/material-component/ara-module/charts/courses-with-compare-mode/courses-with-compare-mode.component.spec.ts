import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CoursesWithCompareModeComponent } from './courses-with-compare-mode.component';

describe('CoursesWithCompareModeComponent', () => {
  let component: CoursesWithCompareModeComponent;
  let fixture: ComponentFixture<CoursesWithCompareModeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CoursesWithCompareModeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CoursesWithCompareModeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
