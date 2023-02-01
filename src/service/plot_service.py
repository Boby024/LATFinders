import pandas as pd
import json
import plotly
import plotly.express as px
from utils import response
from model.rating import Rating
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
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


def plot_number_of_ratings_by_uni_id(data, uni_name, compare_mode):
    df = pd.DataFrame(data)
    # Create subplots
    fig = {}

    df_BoA = df[df['degree_type'] == 'Bachelor of Arts']
    df_BoE = df[df['degree_type'] == 'Bachelor of Engineering']
    df_BoS = df[df['degree_type'] == 'Bachelor of Science']
    df_MoA = df[df['degree_type'] == 'Master of Arts']
    df_MoE = df[df['degree_type'] == 'Master of Engineering']
    df_MoS = df[df['degree_type'] == 'Master of Science']

    if df.size != 0:
        # Pie Chart
        fig = make_subplots(rows=3, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}], [
                            {"type": "pie"}, {"type": "pie"}], [{"type": "pie"}, {"type": "pie"}]], start_cell="top-left", subplot_titles=("Bachelor of Arts", "Bachelor of Engineering", "Bachelor of Science", "Master of Arts", "Master of Engineering", "Master of Science"))
        if compare_mode == "1":
            fig.add_trace(
                go.Pie(labels=df_BoA['course_name'], values=df_BoA['number_of_ratings'], name="Bachelor of Arts"), row=1, col=1)

            fig.add_trace(
                go.Pie(labels=df_BoE['course_name'], values=df_BoE['number_of_ratings'], name="Bachelor of Engineering"), row=1, col=2)

            fig.add_trace(
                go.Pie(labels=df_BoS['course_name'], values=df_BoS['number_of_ratings'], name="Bachelor of Science"), row=2, col=1)

            fig.add_trace(
                go.Pie(labels=df_MoA['course_name'], values=df_MoA['number_of_ratings'], name="Master of Arts"), row=2, col=2)

            fig.add_trace(
                go.Pie(labels=df_MoE['course_name'], values=df_MoE['number_of_ratings'], name="Master of Engineering"), row=3, col=1)

            fig.add_trace(
                go.Pie(labels=df_MoS['course_name'], values=df_MoS['number_of_ratings'], name="Master of Science"), row=3, col=2)
            fig.update_layout(
                autosize=True,
                width=1500,
                height=2000)
        # Bar Chart
        elif compare_mode == "2":
            fig = make_subplots(rows=6, cols=1, specs=[[{"type": "bar"}], [{"type": "bar"}], [{"type": "bar"}], [
                                {"type": "bar"}], [{"type": "bar"}], [{"type": "bar"}]], start_cell="top-left", subplot_titles=("Bachelor of Arts", "Bachelor of Engineering", "Bachelor of Science", "Master of Arts", "Master of Engineering", "Master of Science"))
            fig.add_trace(
                go.Bar(x=df_BoA['course_name'], y=df_BoA['number_of_ratings'], name="abc"), row=1, col=1)
            fig.add_trace(
                go.Bar(x=df_BoE['course_name'], y=df_BoE['number_of_ratings']), row=2, col=1)
            fig.add_trace(
                go.Bar(x=df_BoS['course_name'], y=df_BoS['number_of_ratings']), row=3, col=1)
            fig.add_trace(
                go.Bar(x=df_MoA['course_name'], y=df_MoA['number_of_ratings']), row=4, col=1)
            fig.add_trace(
                go.Bar(x=df_MoE['course_name'], y=df_MoE['number_of_ratings']), row=5, col=1)
            fig.add_trace(
                go.Bar(x=df_MoS['course_name'], y=df_MoS['number_of_ratings']), row=6, col=1)
            fig.update_layout(
                autosize=True,
                width=1300,
                height=3000)

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


def indexing1(data):
    df = pd.DataFrame([[ij for ij in i] for i in data])
    df.rename(columns={0: 'date', 1: 'overall_rating',
                       2: 'course_contents_rating', 3: 'docents_rating',
                       4: 'lectures_rating', 5: 'organization_rating',
                       6: 'library_rating', 7: 'digitization_rating',
                       }, inplace=True)

    df['date'] = pd.to_datetime(df['date'])
    indexedDataset = df.set_index(['date'])
    indexedDataset = indexedDataset.resample('M').mean()

    for i in range(0, len(indexedDataset)-1):
        if np.isnan(indexedDataset.iat[i, 0]) == True:
            for j in range(1, len(indexedDataset)-1):
                if (np.isnan(indexedDataset.iat[i+j, 0]) == False):
                    indexedDataset.iat[i, 0] = (
                        indexedDataset.iat[i-1, 0] + indexedDataset.iat[i+j, 0])/2
                    break

    return indexedDataset


def compare_default_trend_from_two_unis(result):
    df1 = indexing1(result["query1"]["data"])
    df2 = indexing1(result["query2"]["data"])

    # Create traces
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df1.index, y=df1['overall_rating'],
                             mode='lines+markers',
                             name=result["query1"]["uni_name"]))

    fig.add_trace(go.Scatter(x=df2.index, y=df2['overall_rating'],
                             mode='lines+markers',
                             name=result["query2"]["uni_name"]))

    if result["query1"]["course_name"] == result["query2"]["course_name"]:
        title = result["query1"]["course_name"]
    else:
        title = result["query1"]["course_name"] + \
            " vs. " + result["query2"]["course_name"]

    fig.update_layout(title=title,
                      xaxis_title='Date',
                      yaxis_title='Overall Ranking')

    # fig.show()

    graphJSON = plotly.io.to_json(fig, pretty=True)
    graphJSON2 = compare_default_detailed_trends(result, df1, df2)

    return {"graph1": json.loads(graphJSON), "graph2": json.loads(graphJSON2)}


# drawing two detailed courses trends:
def compare_default_detailed_trends(result, df1, df2):

    # Create subplots
    fig = make_subplots(rows=3, cols=2, start_cell="top-left")

    fig.add_trace(go.Scatter(name=result["query1"]["course_name"] + " Course's Content at "+result["query1"]["uni_name"],
                             x=df1.index,
                             y=df1['course_contents_rating'], mode='lines+markers'),
                  row=1, col=1
                  )

    fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Course's Content at "+result["query2"]["uni_name"],
                             x=df2.index,
                             y=df2['course_contents_rating'], mode='lines+markers'),
                  row=1, col=1
                  )

    fig.add_trace(go.Scatter(name=result["query1"]["course_name"] + " Docents at "+result["query1"]["uni_name"],
                             x=df1.index,
                             y=df1['docents_rating'], mode='lines+markers'),
                  row=1, col=2
                  )

    fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Docents at "+result["query2"]["uni_name"],
                             x=df2.index,
                             y=df2['docents_rating'], mode='lines+markers'),
                  row=1, col=2
                  )

    fig.add_trace(go.Scatter(name=result["query1"]["course_name"] + " Lectures at "+result["query1"]["uni_name"],
                             x=df1.index,
                             y=df1['lectures_rating'], mode='lines+markers'),
                  row=2, col=1
                  )

    fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Lectures at "+result["query2"]["uni_name"],
                             x=df2.index,
                             y=df2['lectures_rating'], mode='lines+markers'),
                  row=2, col=1
                  )

    fig.add_trace(go.Scatter(name=result["query1"]["course_name"] + " Organization at "+result["query1"]["uni_name"],
                             x=df1.index,
                             y=df1['organization_rating'], mode='lines+markers'),
                  row=2, col=2
                  )

    fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Organization at "+result["query2"]["uni_name"],
                             x=df2.index,
                             y=df2['organization_rating'], mode='lines+markers'),
                  row=2, col=2
                  )

    fig.add_trace(go.Scatter(name=result["query1"]["course_name"] + " Library at "+result["query1"]["uni_name"],
                             x=df1.index,
                             y=df1['library_rating'], mode='lines+markers'),
                  row=3, col=1
                  )

    fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Library at "+result["query2"]["uni_name"],
                             x=df2.index,
                             y=df2['library_rating'], mode='lines+markers'),
                  row=3, col=1
                  )

    fig.add_trace(go.Scatter(name=result["query1"]["course_name"] + " Digitization at "+result["query1"]["uni_name"],
                             x=df1.index,
                             y=df1['digitization_rating'], mode='lines+markers'),
                  row=3, col=2
                  )
    fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Digitization at "+result["query2"]["uni_name"],
                             x=df2.index,
                             y=df2['digitization_rating'], mode='lines+markers'),
                  row=3, col=2
                  )
    # fig.show()
    fig.update_layout(
        autosize=True,
        width=1500,
        height=800,)
    graphJSON = plotly.io.to_json(fig, pretty=True)
    return graphJSON


def indexing2(data):
    df = pd.DataFrame([[ij for ij in i] for i in data])
    df.rename(columns={0: 'course_contents_rating', 1: 'docents_rating',
                       2: 'lectures_rating', 3: 'organization_rating',
                       4: 'library_rating', 5: 'digitization_rating',
                       6: 'overall_rating', 7: 'author_age',
                       8: 'author_gender', 9: 'author_current_semester',
                       }, inplace=True)

    return df


def single_comparaison_mode(uni_name, course_name, dataFrame, compare_mode):
    if dataFrame.size != 0:

        # Compare based on Age:
        if compare_mode == 1:
            dataFrame = dataFrame.groupby(['author_age']).mean(
                numeric_only=True).reset_index()
            fig = px.bar(dataFrame, x="author_age", y="overall_rating",
                         color="author_age",
                         labels={
                             "author_age": "Age Range",
                             "overall_rating": "Average Ratings",
                         },
                         title=course_name + " Course Rating: based on age at " + uni_name)

        # Compare based on Gender:
        elif compare_mode == 2:

            dataFrame = dataFrame.groupby(['author_gender']).mean(
                numeric_only=True).reset_index()
            fig = px.bar(dataFrame, x="author_gender", y="overall_rating",
                         color="author_gender",
                         labels={
                             "author_gender": "Male vs. Female",
                             "overall_rating": "Average Ratings",
                         },
                         title=course_name + " Course Rating: based on gender at " + uni_name)

        # Compare based on Current Semester:
        elif compare_mode == 3:

            dataFrame = dataFrame.groupby(['author_current_semester']).mean(
                numeric_only=True).reset_index()
            fig = px.bar(dataFrame, x="author_current_semester", y="overall_rating",
                         color="author_current_semester",
                         labels={
                             "author_current_semester": "Current Semester",
                             "overall_rating": "Average Ratings",
                         },
                         title=course_name + " Course Rating: based on current semester at " + uni_name)

        # fig.show()
        graphJSON = plotly.io.to_json(fig, pretty=True)
        return graphJSON


def single_comparaison_detailed_charts_mode(df, compare_mode):
    if df.size != 0:

        # Create subplots
        fig = make_subplots(rows=2, cols=3, start_cell="top-left")

        # Compare based on Age:
        if compare_mode == 1:
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
        elif compare_mode == 2:
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
        elif compare_mode == 3:
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

        # fig.show()
        graphJSON = plotly.io.to_json(fig, pretty=True)
        return graphJSON


def compare_courses_with_mode(result):
    df1 = indexing2(result["query1"]["data"])
    df2 = indexing2(result["query2"]["data"])

    uni_name1 = result["query1"]["uni_name"]
    course_name1 = result["query1"]["course_name"]
    uni_name2 = result["query2"]["uni_name"]
    course_name2 = result["query2"]["course_name"]
    compare_mode = int(result["mode"])

    graphJSON1 = single_comparaison_mode(
        uni_name1, course_name1, df1, compare_mode)
    graphJSON2 = single_comparaison_mode(
        uni_name2, course_name2, df2, compare_mode)

    graphJSON12 = single_comparaison_detailed_charts_mode(df1, compare_mode)
    graphJSON21 = single_comparaison_detailed_charts_mode(df2, compare_mode)

    return {
        "graph1": {
            "first": json.loads(graphJSON1),
            "second": json.loads(graphJSON12)
        },
        "graph2": {
            "first": json.loads(graphJSON2),
            "second": json.loads(graphJSON21)
        }
    }
