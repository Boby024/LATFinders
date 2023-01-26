import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewTestCompComponent } from './new-test-comp.component';

describe('NewTestCompComponent', () => {
  let component: NewTestCompComponent;
  let fixture: ComponentFixture<NewTestCompComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NewTestCompComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NewTestCompComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
