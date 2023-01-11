from setting import db
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Rating(db.Model):
    __tablename__ = 'ratings'
    __table_args__ = {"schema":"testschema"}

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"))  #relationship('Course') # , foreign_keys='Uni.user_id')
    date = Column(DateTime)
    general_rating = Column(Integer)
    rating_of_content = Column(Integer)
    rating_of_professors = Column(Integer)
    rating_of_lectures = Column(Integer)
    rating_of_equipments = Column(Integer)
    rating_of_Organisation = Column(Integer)
    rating_of_library = Column(Integer)
    rating_of_digital_studying = Column(Integer)
    start_of_studies = Column(Integer)
    suggest_to_others = Column(Boolean)
    gender = Column(String(255))
    degree = Column(String(255))
    age = Column(Integer)


    def __init__(self, id, course_id):
        self.id = id
        self.course_id = course_id

    def __repr__(self):
        return f"<Rating {self.id}>"

    def serialize(self):
        return {
            'id': self.id,
            'course_id': self.course_id,
            "date": self.date,
            "general_rating": self.general_rating,
            "rating_of_content": self.rating_of_content,
            "rating_of_professors": self.rating_of_professors,
            "rating_of_lectures": self.rating_of_lectures,
            "rating_of_equipments": self.rating_of_equipments,
            "rating_of_Organisation": self.rating_of_Organisation,
            "rating_of_library": self.rating_of_library,
            "rating_of_digital_studying": self.rating_of_digital_studying,
            "start_of_studies": self.start_of_studies,
            "suggest_to_others": self.suggest_to_others,
            "gender": self.gender,
            "degree": self.degree,
            "age": self.age,
        }