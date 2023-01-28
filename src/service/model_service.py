from model.uni import Uni
from model.course import Course
from model.rating import Rating
from operator import or_, and_
from sqlalchemy import func
from setting import db
from sqlalchemy import text



def get_all_unis():
    unis = Uni.query.all() 
    unis = [d.serialize() for d in unis]
    return unis


def get_uni_by_id(id) -> Uni:
    uni = Uni.query.get(id)
    return uni #.serialize()


def get_all_courses():
    courses = Course.query.all() 
    courses = [d.serialize() for d in courses]
    return courses


def get_course_by_id(id) -> Course:
    course = Course.query.get(id)
    return course #.serialize()


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


def get_uni_courses_with_ratings_over_n():
    unis = db.session.query(Uni).join(Course, Course.uni_id==Uni.id).join(Rating, Rating.course_id==Course.id).all()
    unis = [d.serialize() for d in unis]
    return unis


def get_rating_by_uniId_courseId_date(params):
    uni_id1 = params['uni_id1']
    course_id1 = params['course_id1']
    uni_id2 = params['uni_id2']
    course_id2 = params['course_id2']
    date = params['date']
    type = params['type']

    # if date is None:
    #     date = '2016-12-31'

    query1 = f"""SELECT r.date, r.overall_rating, 
                    r.course_contents_rating, r.docents_rating,
                    r.lectures_rating, r.organization_rating, 
                    r.library_rating, r.digitization_rating 
                    FROM araschema.ratings r 
                    JOIN araschema.courses c 
                    ON c.id = r.course_id 
                    WHERE c.id = {course_id1} 
                    AND c.uni_id = {uni_id1} 
                    AND date > '{date}' 
                    ORDER BY date ASC ;"""
    data1 = db.session.execute(query1).fetchall()

    query2 = f"""SELECT r.date, r.overall_rating, 
                    r.course_contents_rating, r.docents_rating,
                    r.lectures_rating, r.organization_rating, 
                    r.library_rating, r.digitization_rating 
                    FROM araschema.ratings r 
                    JOIN araschema.courses c 
                    ON c.id = r.course_id 
                    WHERE c.id = {course_id2} 
                    AND c.uni_id = {uni_id2} 
                    AND date > '{date}' 
                    ORDER BY date ASC ;"""
    data2 = db.session.execute(query2).fetchall()

    return {
        "query1": {
            "uni_id": uni_id1,
            "uni_name": get_uni_by_id(uni_id1).name,
            "course_id": course_id1,
            "course_name": get_course_by_id(course_id1).course_name,
            "data": data1
        },
        "query2": {
            "uni_id": uni_id2,
            "uni_name": get_uni_by_id(uni_id2).name,
            "course_id": course_id2,
            "course_name": get_course_by_id(course_id2).course_name,
            "data": data2
        }
    }