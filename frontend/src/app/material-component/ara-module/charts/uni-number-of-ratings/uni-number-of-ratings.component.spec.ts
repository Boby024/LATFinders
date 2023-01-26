import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UniNumberOfRatingsComponent } from './uni-number-of-ratings.component';

describe('UniNumberOfRatingsComponent', () => {
  let component: UniNumberOfRatingsComponent;
  let fixture: ComponentFixture<UniNumberOfRatingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UniNumberOfRatingsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UniNumberOfRatingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
