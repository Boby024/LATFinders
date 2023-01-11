import pandas as pd
import json
import plotly
import plotly.express as px


def plot_ratings(data):
    title = "Rating Courses"
    df = pd.DataFrame(data)
    fig = px.line(df, x="date", y="course_id", labels={
                     "date": "Date",
                     "course_id": "Course ID",
                 }) # , title=title)
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON = plotly.io.to_json(fig, pretty=True)

    return graphJSON