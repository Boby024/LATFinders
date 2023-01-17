import pandas as pd
import json
import plotly
import plotly.express as px
from utils import response


def plot_ratings(data):
    title = "Rating Courses"
    df = pd.DataFrame(data)
    fig = px.line(df, x="date", y="overall_rating", labels={
                     "date": "Date",
                     "overall_rating": "Rating",
                 }) # , title=title)
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON = plotly.io.to_json(fig, pretty=True)

    return response.setRep(graphJSON, "f")