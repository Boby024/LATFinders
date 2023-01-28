import pandas as pd
import json
import plotly
import plotly.express as px
from utils import response
from model.rating import Rating
import numpy as np
import plotly.graph_objects as go



def plot_ratings(data):

    title = "Rating Courses"
    df = pd.DataFrame(data)
    fig = px.line(df, x="date", y="overall_rating", labels={
                     "date": "Date",
                     "overall_rating": "Rating",
                 }) # , title=title)
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON = plotly.io.to_json(fig, pretty=True)

    return graphJSON # response.setRep(graphJSON, "f")


def indexing1(data):
    df= pd.DataFrame( [[ij for ij in i] for i in data] )
    df.rename(columns={0: 'date', 1: 'overall_rating',
                           2: 'course_contents_rating', 3: 'docents_rating',
                           4: 'lectures_rating', 5: 'organization_rating',
                           6: 'library_rating', 7: 'digitization_rating',
                          }, inplace=True);
        
    df['date'] = pd.to_datetime(df['date'])
    indexedDataset = df.set_index(['date'])
    indexedDataset = indexedDataset.resample('M').mean()


    for i in range(0, len(indexedDataset)-1): 
        if np.isnan(indexedDataset.iat[i,0]) == True:
            for j in range(1, len(indexedDataset)-1):
                if(np.isnan(indexedDataset.iat[i+j,0]) == False):
                    indexedDataset.iat[i,0] = (indexedDataset.iat[i-1,0] + indexedDataset.iat[i+j,0])/2
                    break

    return indexedDataset

def plot_trend_from_two_unis(result):
    print(result.keys())

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
        title = result["query1"]["course_name"] +" vs. "+ result["query2"]["course_name"]
    
    fig.update_layout(title = title ,
                   xaxis_title='Date',
                   yaxis_title='Overall Ranking')

    # fig.show()

    graphJSON = plotly.io.to_json(fig, pretty=True)
    return graphJSON