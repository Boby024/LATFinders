from setting import db
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Course(db.Model):
    __tablename__ = 'courses'
    __table_args__ = {"schema":"araschema"}

    id = Column(Integer, primary_key=True)
    course_name = Column(String(150))
    uni_id = Column(Integer, ForeignKey("unis.id")) # relationship('Uni') # , foreign_keys='Uni.user_id')
    degree_type = Column(String(40))
    is_teacher_training = Column(Boolean)
    identity_link = Column(String(200))
    standard_period_of_study = Column(String(40))
    classroom_languages = Column(String(200))

    def __init__(self, id, course_name, uni_id):
        self.id = id
        self.course_name = course_name
        self.uni_id = uni_id

    def __repr__(self):
        return f"<Course {self.id}>"

    def serialize(self):
        return {
            'id': self.id,
            'course_name': self.course_name,
            "uni_id": self.uni_id,
            "degree_type": self.degree_type
        }