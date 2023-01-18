import os
import json
from setting import create_app, request, jsonify
from service import model_service
from dotenv import load_dotenv
from flask import render_template, redirect
from service import plot_service
from utils import response


load_dotenv()
PORT = int(os.environ.get('PORT', 5000))
app = create_app()


@app.route('/group_name')
def test():
    return {"group": "LATFinders"}

@app.route('/unis', methods=['GET'])
def get_unis():
    return response.setRep(model_service.get_all_unis(), "f")

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