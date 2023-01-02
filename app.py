# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
from dash import Dash, html, dcc, dash_table
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import time
import datetime

from dash import Dash, dcc, html, Input, Output
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors, svm
import plotly.graph_objects as go
import plotly.express as px
import numpy as np


app = Dash(__name__)

# assume you have a "long-form" data frame
# Connect to your postgres DB

engine = create_engine('postgresql://aratestuser:ZcNftCy7Af2esE56DovpXY4vxuL0mwEV@dpg-celimjda4991ihk6gumg-a.frankfurt-postgres.render.com:5432/aratestdb')

dfAraDB = pd.read_sql_query("SELECT * FROM testschema.courses c "
            "JOIN testschema.unis u ON c.uni_id = u.id "
            "JOIN testschema.ratings r ON r.course_id = c.id  ",con=engine)

# rows where courseid is 1
dfAraDB = dfAraDB.loc[dfAraDB["course_id"] == 1]
dfAraDB["date"] = dfAraDB["date"].apply(lambda date: time.mktime(datetime.datetime.strptime(str(date), "%Y-%m-%d").timetuple()))
dfAraDB = dfAraDB.sort_values(by="date")
#print(dfAraDB)

#datex = np.array([time.mktime(datetime.datetime.strptime(str(date), "%Y-%m-%d").timetuple()) for date in dfAraDB["date"].tolist()])
datex = np.array(dfAraDB["date"].tolist())
ratingy = np.array(dfAraDB["general_rating"].tolist())

dfReg  = pd.DataFrame({'date': datex, 'rating':ratingy})

reg = LinearRegression().fit(np.vstack(dfReg["date"]), dfReg["rating"])
dfReg['bestfit'] = reg.predict(np.vstack(dfReg["date"]))
# plotly figure setup
figReg=go.Figure()
figReg.add_trace(go.Scatter(name='X vs Y', x=dfReg["date"], y=dfReg["rating"].values, mode='markers'))
figReg.add_trace(go.Scatter(name='line of best fit', x=datex, y=dfReg['bestfit'], mode='lines'))
# plotly figure layout
figReg.update_layout(xaxis_title = 'date', yaxis_title = 'rating')


fig = px.scatter(dfAraDB, x="date", y="general_rating", trendline="ols")#, color="date")

app.layout = dash_table.DataTable(dfAraDB.to_dict('records'), [{"name": i, "id": i} for i in dfAraDB.columns])
models = {'Regression': linear_model.LinearRegression,
          'Decision Tree': tree.DecisionTreeRegressor,
          'k-NN': neighbors.KNeighborsRegressor,
          'SVR': svm.SVR}
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Graph(
        id='linear-reg_example',
        figure=figReg
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    html.H4("Predicting study-course ratings"),
    html.P("Select model:"),
    dcc.Dropdown(
        id='dropdown',
        options=["Regression", "Decision Tree", "k-NN", "SVR"],
        value='Decision Tree',
        clearable=False
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"),
    Input('dropdown', "value"))
def train_and_display(name):
    df = dfAraDB.sort_values(by="date", ascending=True) # replace with your own data source
    print(df)
    X = df.date.values[:, None]
    Y = df.general_rating.values[:]
    #X_train, X_test, y_train, y_test = train_test_split(
     #   X, df.general_rating, random_state=0)

    model = models[name]()
    model.fit(X, Y)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))

    fig = go.Figure([
        go.Scatter(x=X.squeeze(), y=Y,
                   name='train'),# mode='markers'),
        #go.Scatter(x=X.squeeze(), y=Y,
         #          name='test'),# mode='markers'),
        go.Scatter(x=x_range, y=y_range,
                   name='prediction')
    ])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
