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


def plot_course_with_ratings(data, compare_mode):
    dataFrame = pd.DataFrame(data)
    fig = {}
    if dataFrame.size != 0:
        uni_name = data[0]['name']
        course_name = data[0]['course_name']
        # Compare based on Age:
        if compare_mode == "1":
            dataFrame = dataFrame.groupby(['author_age']).mean(
                numeric_only=True).reset_index()
            fig = px.bar(dataFrame, x="author_age", y="overall_rating",
                         color="author_age",
                         labels={
                             "author_age": "Age Range",
                             "overall_rating": "Average Ratings",
                         },
                         title=course_name+" Course Rating: based on age at " + uni_name)

        # Compare based on Gender:
        elif compare_mode == "2":

            dataFrame = dataFrame.groupby(['author_gender']).mean(
                numeric_only=True).reset_index()
            fig = px.bar(dataFrame, x="author_gender", y="overall_rating",
                         color="author_gender",
                         labels={
                             "author_gender": "Male vs. Female",
                             "overall_rating": "Average Ratings",
                         },
                         title=course_name+" Course Rating: based on age at " + uni_name)

        # Compare based on Current Semester:
        elif compare_mode == "3":

            dataFrame = dataFrame.groupby(['author_current_semester']).mean(
                numeric_only=True).reset_index()
            fig = px.bar(dataFrame, x="author_current_semester", y="overall_rating",
                         color="author_current_semester",
                         labels={
                             "author_current_semester": "Current Semester",
                             "overall_rating": "Average Ratings",
                         },
                         title=course_name+" Course Rating: based on age at " + uni_name)

        graphJSON = plotly.io.to_json(fig, pretty=True)
        return graphJSON
    else:
        print("Wrong uni_id or course_id :) ")


def plot_course_with_ratings_detailed(data, compare_mode):
    df = pd.DataFrame(data)
    fig = {}
    if df.size != 0:
        # Create subplots
        fig = make_subplots(rows=2, cols=3, start_cell="top-left")
        # Compare based on Age:
        if compare_mode == "1":
            df = df.groupby(['author_age']).mean(
                numeric_only=True).reset_index()
            df1 = df.iloc[:, [0, 1]].copy()
            df2 = df.iloc[:, [0, 2]].copy()
            df3 = df.iloc[:, [0, 3]].copy()
            df4 = df.iloc[:, [0, 4]].copy()
            df5 = df.iloc[:, [0, 5]].copy()
            df6 = df.iloc[:, [0, 6]].copy()

            # Set traces for the 1st bar chart
            fig.add_trace(go.Bar(name="Course's Content Rating",
                                 x=df1['author_age'],
                                 y=df1['course_contents_rating']),
                          row=1, col=1)

            # Traces for the 2nd bar chart
            fig.add_trace(go.Bar(name="Docents Rating",
                                 x=df2['author_age'],
                                 y=df2['docents_rating']),
                          row=1, col=2)

            # Traces for the 3rd bar chart
            fig.add_trace(go.Bar(name="Lectures Rating",
                                 x=df3['author_age'],
                                 y=df3['lectures_rating']),
                          row=1, col=3)

            # Traces for the 4th bar chart
            fig.add_trace(go.Bar(name="Organization Rating",
                                 x=df4['author_age'],
                                 y=df4['organization_rating']),
                          row=2, col=1)

            # Traces for the 5th bar chart
            fig.add_trace(go.Bar(name="Library Rating",
                                 x=df5['author_age'],
                                 y=df5['library_rating']),
                          row=2, col=2)

            # Traces for the 6th bar chart
            fig.add_trace(go.Bar(name="Digitization Rating",
                                 x=df6['author_age'],
                                 y=df6['digitization_rating']),
                          row=2, col=3)

        # Compare based on Gender:
        elif compare_mode == "2":
            df = df.groupby(['author_gender']).mean(
                numeric_only=True).reset_index()
            df1 = df.iloc[:, [0, 1]].copy()
            df2 = df.iloc[:, [0, 2]].copy()
            df3 = df.iloc[:, [0, 3]].copy()
            df4 = df.iloc[:, [0, 4]].copy()
            df5 = df.iloc[:, [0, 5]].copy()
            df6 = df.iloc[:, [0, 6]].copy()

            # Set traces for the 1st bar chart
            fig.add_trace(go.Bar(name="Course's Content Rating",
                                 x=df1['author_gender'],
                                 y=df1['course_contents_rating']),
                          row=1, col=1)

            # Traces for the 2nd bar chart
            fig.add_trace(go.Bar(name="Docents Rating",
                                 x=df2['author_gender'],
                                 y=df2['docents_rating']),
                          row=1, col=2)

            # Traces for the 3rd bar chart
            fig.add_trace(go.Bar(name="Lectures Rating",
                                 x=df3['author_gender'],
                                 y=df3['lectures_rating']),
                          row=1, col=3)

            # Traces for the 4th bar chart
            fig.add_trace(go.Bar(name="Organization Rating",
                                 x=df4['author_gender'],
                                 y=df4['organization_rating']),
                          row=2, col=1)

            # Traces for the 5th bar chart
            fig.add_trace(go.Bar(name="Library Rating",
                                 x=df5['author_gender'],
                                 y=df5['library_rating']),
                          row=2, col=2)

            # Traces for the 6th bar chart
            fig.add_trace(go.Bar(name="Digitization Rating",
                                 x=df6['author_gender'],
                                 y=df6['digitization_rating']),
                          row=2, col=3)

        # Compare based on Current Semester:
        elif compare_mode == "3":
            df = df.groupby(['author_current_semester']).mean(
                numeric_only=True).reset_index()
            df1 = df.iloc[:, [0, 1]].copy()
            df2 = df.iloc[:, [0, 2]].copy()
            df3 = df.iloc[:, [0, 3]].copy()
            df4 = df.iloc[:, [0, 4]].copy()
            df5 = df.iloc[:, [0, 5]].copy()
            df6 = df.iloc[:, [0, 6]].copy()

            # Set traces for the 1st bar chart
            fig.add_trace(go.Bar(name="Course's Content Rating",
                                 x=df1['author_current_semester'],
                                 y=df1['course_contents_rating']),
                          row=1, col=1)

            # Traces for the 2nd bar chart
            fig.add_trace(go.Bar(name="Docents Rating",
                                 x=df2['author_current_semester'],
                                 y=df2['docents_rating']),
                          row=1, col=2)

            # Traces for the 3rd bar chart
            fig.add_trace(go.Bar(name="Lectures Rating",
                                 x=df3['author_current_semester'],
                                 y=df3['lectures_rating']),
                          row=1, col=3)

            # Traces for the 4th bar chart
            fig.add_trace(go.Bar(name="Organization Rating",
                                 x=df4['author_current_semester'],
                                 y=df4['organization_rating']),
                          row=2, col=1)

            # Traces for the 5th bar chart
            fig.add_trace(go.Bar(name="Library Rating",
                                 x=df5['author_current_semester'],
                                 y=df5['library_rating']),
                          row=2, col=2)

            # Traces for the 6th bar chart
            fig.add_trace(go.Bar(name="Digitization Rating",
                                 x=df6['author_current_semester'],
                                 y=df6['digitization_rating']),
                          row=2, col=3)
        print(fig)
        graphJSON = plotly.io.to_json(fig, pretty=True)
        return graphJSON

#TODO: delete or edit


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
