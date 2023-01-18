from model.uni import Uni
from model.course import Course
from model.rating import Rating
from operator import or_, and_
from sqlalchemy import func



def get_all_unis():
    unis = Uni.query.all() 
    unis = [d.serialize() for d in unis]
    return unis


def get_all_courses():
    courses = Course.query.all() 
    courses = [d.serialize() for d in courses]
    return courses


def get_all_courses_by_uni_id(params): # request.args
    uni_id = params.get("uni_id")
    courses = Course.query.filter(Course.uni_id == uni_id) 
    courses = [d.serialize() for d in courses]
    return courses


def get_all_ratings():
    ratings = Rating.query.limit(10).all()
    ratings = [ d.__dict__ for d in ratings]

    return ratings


def get_all_ratings_by_params(params): # course_id, rating_gender
    course_id = params.get("course_id")
    print(course_id)
    
    ratings = Rating.query.filter(Rating.course_id == course_id).limit(10).all()

    # ratings = Rating.query.limit(10).all()
    ratings = [ d.__dict__ for d in ratings]

    return ratings


def filter_unis(params): # request.args
    query = params.get("query")

    unis = Uni.query.filter(
        func.lower(Uni.name).contains(str(query).lower(), autoescape=True)
    )

    unis = [d.serialize() for d in unis]
    return unis


def filter_courses(params): # request.args
    uni_id = params.get("uni_id")
    query = params.get("query")

    courses = Course.query.filter(
        and_(
            func.lower(Course.course_name).contains(str(query).strip().lower(), autoescape=True),
            Course.uni_id == uni_id
        )
    ) #.distinct().group_by(Course.uni_id, Course.course_name)
    
    courses = [d.serialize() for d in courses]
    return courses





