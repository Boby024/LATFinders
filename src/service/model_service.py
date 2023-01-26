from model.uni import Uni
from model.course import Course
from model.rating import Rating
from operator import or_, and_
from sqlalchemy import func, text
from setting import db


def get_all_unis():
    unis = Uni.query.all()
    unis = [d.serialize() for d in unis]
    return unis


def get_all_courses():
    courses = Course.query.all()
    courses = [d.serialize() for d in courses]
    return courses


def get_all_courses_by_uni_id(params):  # request.args
    uni_id = params.get("uni_id")
    courses = Course.query.filter(Course.uni_id == uni_id)
    courses = [d.serialize() for d in courses]
    return courses


def get_courses_and_number_of_ratings_by_uni(params):
    uni_id = params.get("uni_id")
    sqlResult = db.engine.execute(text(
        '''
        SELECT degree_type, course_id, course_name, COUNT(araschema.ratings.id) as number_of_ratings
        FROM araschema.ratings
        INNER JOIN araschema.courses ON course_id= araschema.courses.id
        WHERE araschema.courses.uni_id = :uni_id
        GROUP BY course_id, degree_type, course_name
        '''),
        {'uni_id': uni_id}
    )
    courses = [dict(d.items()) for d in sqlResult]

    return courses


def get_all_ratings():
    ratings = Rating.query.limit(10).all()
    ratings = [d.__dict__ for d in ratings]

    return ratings


def get_all_ratings_by_params(params):  # course_id, rating_gender
    course_id = params.get("course_id")
    print(course_id)

    ratings = Rating.query.filter(
        Rating.course_id == course_id).limit(10).all()

    # ratings = Rating.query.limit(10).all()
    ratings = [d.__dict__ for d in ratings]

    return ratings


def get_uni_by_params(params):
    id = params.get("uni_id")
    print(id)

    uni = Uni.query.filter(Uni.id == id).all()

    unires = [d.__dict__ for d in uni]

    return unires[0]


def get_course_and_ratings(course_id):
    sqlResult = db.engine.execute(text(
        '''
        SELECT u.name,c.course_name, r.course_contents_rating, r.docents_rating,
                     r.lectures_rating, r.organization_rating, r.library_rating,
                     r.digitization_rating, r.overall_rating,
                     r.author_age ,r.author_gender, r.author_current_semester
                     FROM araschema.ratings r
                     JOIN araschema.courses c
                     ON c.id = r.course_id
					 JOIN araschema.unis u
					 ON u.id=c.uni_id
                     WHERE c.id =:course_id
                     AND (r.author_gender ='F' OR r.author_gender ='M')
                     AND r.author_age !='keine Angabe'
                     ORDER BY r.author_age ASC ;
        '''),
        {'course_id': course_id}
    )
    course_and_ratings = [dict(d.items()) for d in sqlResult]

    return course_and_ratings


def filter_unis(params):  # request.args
    query = params.get("query")

    unis = Uni.query.filter(
        func.lower(Uni.name).contains(str(query).lower(), autoescape=True)
    )

    unis = [d.serialize() for d in unis]
    return unis


def filter_courses(params):  # request.args
    uni_id = params.get("uni_id")
    query = params.get("query")

    courses = Course.query.filter(
        and_(
            func.lower(Course.course_name).contains(
                str(query).strip().lower(), autoescape=True),
            Course.uni_id == uni_id
        )
    )  # .distinct().group_by(Course.uni_id, Course.course_name)

    courses = [d.serialize() for d in courses]
    return courses
