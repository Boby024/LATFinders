import os
import json
from setting import create_app, request, jsonify
from service import model_service
from dotenv import load_dotenv
from flask import render_template, redirect
from service import plot_service
from utils import response
from service import ml_model

load_dotenv()
PORT = int(os.environ.get('PORT', 5000))
app = create_app()


@app.route('/group_name')
def test():
    return {"group": "LATFinders"}


@app.route('/unis', methods=['GET'])
def get_unis():
    return response.setRep(model_service.get_all_unis(), "f")


@app.route('/unis2', methods=['GET'])
def get_uni_courses_with_ratings_over_n():
    return response.setRep(model_service.get_uni_courses_with_ratings_over_n(), "f")


@app.route('/courses', methods=['GET'])
def get_courses():
    return response.setRep(model_service.get_all_courses(), "f")


@app.route('/courses_by_uni_id', methods=['GET'])
def get_all_courses_by_uni_id():
    return response.setRep(model_service.get_all_courses_by_uni_id(request.args), "f")


@app.route('/filter_unis', methods=['GET'])
def filter_unis():
    return response.setRep(model_service.filter_unis(request.args), "f")


@app.route('/filter_courses', methods=['GET'])
def filter_courses():
    return response.setRep(model_service.filter_courses(request.args), "f")


@app.route("/plot_ratings")
def plot_ratings():
    ratings = model_service.get_all_ratings_by_params(request.args)
    return response.setRep(plot_service.plot_ratings(ratings), "f")


@app.route("/unis/plot_number_of_ratings_by_uni_id")
def plot_number_of_ratings_by_uni_id():
    uni = model_service.get_uni_by_params(request.args)
    courses_with_count = model_service.get_courses_and_number_of_ratings_by_uni(
        request.args)
    return response.setRep(plot_service.plot_number_of_ratings_by_uni_id(courses_with_count, uni['name']), "f")


@app.route("/course/plot_course_ratings_with_compare_mode")
def plot_course_ratings_with_compare_mode():
    course_id = request.args.get('course_id')
    compare_mode = request.args.get('compare_mode')
    courses_with_ratings = model_service.get_course_and_ratings(
        course_id)

    return response.setRep(plot_service.plot_course_with_ratings(courses_with_ratings, compare_mode), "f")


@app.route("/course/plot_course_ratings_detailed_mode")
def plot_course_ratings_detailed_mode():
    course_id = request.args.get('course_id')
    compare_mode = request.args.get('compare_mode')
    courses_with_ratings = model_service.get_course_and_ratings(
        course_id)

    return response.setRep(plot_service.plot_course_with_ratings_detailed(courses_with_ratings, compare_mode), "f")


@app.route("/compare-course-default", methods=['POST'])
def compare_course_trend():
    request_data = request.get_json()
    sql_result = model_service.compare_unis_default(request_data)
    return response.setRep(plot_service.compare_default_trend_from_two_unis(sql_result), "f")


@app.route("/compare-course-mode", methods=['POST'])
def compare_course_mode():
    request_data = request.get_json()

    sql_result = model_service.compare_unis_with_mode(request_data)
    return response.setRep(plot_service.compare_courses_with_mode(sql_result), "f")


@app.route("/course-prediction", methods=['POST'])
def course_prediction():
    request_data = request.get_json()

    sql_result = model_service.get_unis_courses_for_ml(request_data)
    return response.setRep(ml_model.final(sql_result), "f")

# @app.route('/ratings', methods=['GET'])
# def get_ratings():
#     return jsonify(model_service.get_all_ratings())


# @app.route("/rating")
# def rating_page():
#     ratings = model_service.get_all_ratings()
#     return render_template("rating.html", graphJSON=plot_service.rating(ratings))

# @app.route("/login")
# def login():
#     return render_template("login.html")

# @app.route("/")
# def home():
#     courses = model_service.get_all_courses()
#     print(courses)
#     return render_template("main.html", course=courses)

# @app.route('/comparison', methods = ['POST', 'GET'])
# def comparison():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         print(f"username -> {username} and password -> {password}")
#         courses = model_service.get_all_courses()
#         return render_template("comparison.html", course=courses)
if __name__ == '__main__':
    app.run(threaded=True, host=('0.0.0.0'), port=PORT)
