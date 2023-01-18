from model.uni import Uni
from model.course import Course
from model.rating import Rating


def get_all_unis():
    unis = Uni.query.all() 
    unis = [d.serialize() for d in unis]
    return unis


def get_all_courses():
    courses = Course.query.all() 
    courses = [d.serialize() for d in courses]
    return courses


def get_all_ratings():
    ratings = Rating.query.all() 
    ratings = [d.serialize() for d in ratings]
    return ratings