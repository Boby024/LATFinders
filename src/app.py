import os
import json
from setting import create_app, request, jsonify
from service import model_service
from dotenv import load_dotenv
from flask import render_template, redirect
from service import main


load_dotenv()
PORT = int(os.environ.get('PORT', 5000))
app = create_app()


@app.route('/group_name')
def test():
    return {"group": "LATFinders"}

@app.route('/unis', methods=['GET'])
def get_unis():
    return jsonify(model_service.get_all_unis())

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(model_service.get_all_courses())

@app.route('/filter_unis', methods=['GET'])
def filter_unis():
    return jsonify(model_service.filter_unis(request.args))

@app.route('/filter_courses', methods=['GET'])
def filter_courses():
    return jsonify(model_service.filter_courses(request.args))



@app.route('/ratings', methods=['GET'])
def get_ratings():
    return jsonify(model_service.get_all_ratings())


@app.route("/plot_ratings")
def plot_ratings():
    ratings = model_service.get_all_ratings()
    return main.plot_ratings(ratings)





@app.route("/rating")
def rating_page():
    ratings = model_service.get_all_ratings()
    return render_template("rating.html", graphJSON=main.rating(ratings))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/")
def home():
    courses = model_service.get_all_courses()
    print(courses)
    return render_template("main.html", course=courses)

@app.route('/comparison', methods = ['POST', 'GET'])
def comparison():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"username -> {username} and password -> {password}")
        
        courses = model_service.get_all_courses()
        return render_template("comparison.html", course=courses)


if __name__ == '__main__':
    app.run(threaded=True, host=('0.0.0.0'), port=PORT)