from setting import db
from sqlalchemy import Column, String, Integer


class Uni(db.Model):
    __tablename__ = 'unis'
    __table_args__ = {"schema":"testschema"}

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

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