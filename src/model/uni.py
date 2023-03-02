from setting import db
from sqlalchemy import Column, String, Integer


class Uni(db.Model):
    __tablename__ = 'unis'
    __table_args__ = {"schema":"araschema"}

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    type = Column(String(100))
    number_ofcourses = Column(Integer)
    identity_link = Column(String(200))
    year_of_foundation = Column(Integer)
    number_of_students = Column(Integer)
    number_of_docents = Column(Integer)
    number_of_professors = Column(Integer)
    score = Column(Integer)


    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Uni {self.id}>"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }