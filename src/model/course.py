from setting import db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Course(db.Model):
    __tablename__ = 'courses'
    __table_args__ = {"schema":"testschema"}

    id = Column(Integer, primary_key=True)
    course_name = Column(String(100))
    uni_id = Column(Integer, ForeignKey("unis.id")) # relationship('Uni') # , foreign_keys='Uni.user_id')

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
            "uni_id": self.uni_id
        }