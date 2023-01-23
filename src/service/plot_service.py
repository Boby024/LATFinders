import pandas as pd
import json
import plotly
import plotly.express as px
from utils import response
from model.rating import Rating
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_ratings(data):
    title = "Rating Courses"
    df = pd.DataFrame(data)
    fig = px.line(df, x="date", y="overall_rating", labels={
        "date": "Date",
        "overall_rating": "Rating",
    })  # , title=title)
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON = plotly.io.to_json(fig, pretty=True)

    return graphJSON  # response.setRep(graphJSON, "f")


def plot_number_of_ratings_by_uni_id(data, uni_name):
    df = pd.DataFrame(data)
    # Create subplots
    fig = make_subplots(rows=2, cols=3, specs=[[{"type": "pie"}, {"type": "pie"}, {"type": "pie"}], [
                        {"type": "pie"}, {"type": "pie"}, {"type": "pie"}]], start_cell="top-left")

    df_BoA = df[df['degree_type'] == 'Bachelor of Arts']
    df_BoE = df[df['degree_type'] == 'Bachelor of Engineering']
    df_BoS = df[df['degree_type'] == 'Bachelor of Science']
    df_MoA = df[df['degree_type'] == 'Master of Arts']
    df_MoE = df[df['degree_type'] == 'Master of Engineering']
    df_MoS = df[df['degree_type'] == 'Master of Science']

    chart_type = 1
    if df.size != 0:
        # Pie Chart
        if chart_type == 1:
            fig.add_trace(
                go.Pie(labels=df_BoA['course_name'], values=df_BoA['number_of_ratings']), row=1, col=1)

            fig.add_trace(
                go.Pie(labels=df_BoE['course_name'], values=df_BoE['number_of_ratings']), row=1, col=2)

            fig.add_trace(
                go.Pie(labels=df_BoS['course_name'], values=df_BoS['number_of_ratings']), row=1, col=3)

            fig.add_trace(
                go.Pie(labels=df_MoA['course_name'], values=df_MoA['number_of_ratings']), row=2, col=1)

            fig.add_trace(
                go.Pie(labels=df_MoE['course_name'], values=df_MoE['number_of_ratings']), row=2, col=2)

            fig.add_trace(
                go.Pie(labels=df_MoS['course_name'], values=df_MoS['number_of_ratings']), row=2, col=3)
        # Bar Chart
        elif chart_type == 2:
            fig = px.bar(df, x="course_name", y="overall_rating",
                         color="course_name",
                         labels={
                             "course_name": "Courses",
                             "overall_rating": "Overall Ratings",
                         },
                         title=degree_type+" courses at "+get_uni_name(uni_id))
        graphJSON = plotly.io.to_json(fig, pretty=True)

        return graphJSON
    else:
        print("Degree Type is not available :) ")


def plot_uni_number_of_ratings_by_all_course_types(uni_id, course_id, dataFrame, compare_mode):
    if df.size != 0:
        # Pie Chart
        if chart_type == 1:
            fig = px.pie(values=dataFrame['overall_rating'],
                         names=dataFrame['course_name'],
                         title=degree_type+" courses at "+get_uni_name(uni_id),
                         hole=.4)

        # Bar Chart
        elif chart_type == 2:
            fig = px.bar(dataFrame, x="course_name", y="overall_rating",
                         color="course_name",
                         labels={
                             "course_name": "Courses",
                             "overall_rating": "Overall Ratings",
                         },
                         title=degree_type+" courses at "+get_uni_name(uni_id))

        fig.show()
    else:
        print("Degree Type is not available :) ")
