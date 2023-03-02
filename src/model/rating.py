from setting import db
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Rating(db.Model):
    __tablename__ = 'ratings'
    __table_args__ = {"schema":"araschema"}

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"))  #relationship('Course') # , foreign_keys='Uni.user_id')
    date = Column(DateTime)
    author_name = Column(String(50))
    author_current_semester= Column(Integer)
    review_heading = Column(String(150))
    author_school_leaving_qualification = Column(String(100))
    author_gpa= Column(Integer)
    author_year_of_study = Column(Integer)
    author_age = Column(String(20))
    furnishings_rating = Column(Integer)
    author_form_of_study = Column(String(100))
    course_contents_rating = Column(Integer)
    library_rating = Column(Integer)
    organization_rating = Column(Integer)
    review_day_of_publication = Column(String(20))
    author_study_status= Column(String(30))
    review_recommendation= Column(Boolean)
    author_gender = Column(String(3))
    review_day_of_creation= Column(String(20))
    lectures_rating = Column(Integer)
    digitization_rating = Column(Integer)
    review_views = Column(String(150))
    overall_rating = Column(Integer)
    docents_rating = Column(Integer)
    identity_link = Column(String(200))


    def __init__(self, id, course_id):
        self.id = id
        self.course_id = course_id

    def __repr__(self):
        return f"<Rating {self.id}>"

    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'course_id': self.course_id,
    #         "date": self.date,
    #         "general_rating": self.general_rating,
    #         "rating_of_content": self.rating_of_content,
    #         "rating_of_professors": self.rating_of_professors,
    #         "rating_of_lectures": self.rating_of_lectures,
    #         "rating_of_equipments": self.rating_of_equipments,
    #         "rating_of_Organisation": self.rating_of_Organisation,
    #         "rating_of_library": self.rating_of_library,
    #         "rating_of_digital_studying": self.rating_of_digital_studying,
    #         "start_of_studies": self.start_of_studies,
    #         "suggest_to_others": self.suggest_to_others,
    #         "gender": self.gender,
    #         "degree": self.degree,
    #         "age": self.age,
    #     }