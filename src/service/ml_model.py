import pandas as pd
import json
import plotly
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as smapi
from sklearn.metrics import mean_squared_error
from math import sqrt
from pandas.tseries.offsets import DateOffset


def indexing(data):
    df = pd.DataFrame([[ij for ij in i] for i in data])
    df.rename(columns={0: 'date', 1: 'overall_rating'}, inplace=True)

    return df


def visualize_data(dataFrame):

    # Parse strings to datetime type
    dataFrame['date'] = pd.to_datetime(dataFrame['date'])
    indexedDataset = dataFrame.set_index(['date'])
    indexedDataset = indexedDataset.resample('M').mean()

    # Dealing with miss values
    for i in range(0, len(indexedDataset)-1):
        if np.isnan(indexedDataset.iat[i, 0]) == True:
            for j in range(1, len(indexedDataset)-i):
                if (np.isnan(indexedDataset.iat[i+j, 0]) == False):
                    indexedDataset.iat[i, 0] = (
                        indexedDataset.iat[i-1, 0] + indexedDataset.iat[i+j, 0])/2
                    break

    return indexedDataset


def plot_Charts(dataFrame, indexedDataset):

    # plotting the line chart before
    fig = px.line(dataFrame, x='date', y='overall_rating',
                  labels={
                      "date": "Date",
                      "overall_rating": "Average Ratings",
                  },
                  title="Before preprocessing: ")
    # fig.show()
    graphJSON1 = plotly.io.to_json(fig, pretty=True)

    # plotting the line chart after
    fig = px.line(indexedDataset, x=indexedDataset.index, y='overall_rating',
                  labels={
                      "date": "Date",
                      "overall_rating": "Average Ratings",
                  },
                  title="After preprocessing: ")
    # fig.show()
    graphJSON2 = plotly.io.to_json(fig, pretty=True)

    return {"graph1": json.loads(graphJSON1), "graph2": json.loads(graphJSON2)}


def adfuller_test(timeseries):
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries['overall_rating'], autolag='AIC')
    dfoutput = pd. Series(dftest[0:4], index=[
                          'Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput[' Critical Value (%s) ' % key] = value
    # print(dfoutput)

    if dfoutput[1] <= 0.05:
        print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")

    return dfoutput[1]


def SARIMA_model(indexedDataset, _order, _sorder):

    model = smapi.tsa.statespace.SARIMAX(endog=indexedDataset['overall_rating'],
                                         order=_order, seasonal_order=_sorder,
                                         trend='c', enforce_invertibility=False)

    result = model.fit()

    return result


def accurate_model(indexedDataset):

    pred = indexedDataset

    # Model 1:
    result_1 = SARIMA_model(indexedDataset, (2, 0, 1), (2, 1, 0, 12))
    pred['forecast1'] = result_1.predict(start=round(
        len(indexedDataset)*0.8), end=len(indexedDataset)-1, dynamic=True)

    # Model 2:
    result_2 = SARIMA_model(indexedDataset, (2, 0, 0), (2, 1, 0, 12))
    pred['forecast2'] = result_2.predict(start=round(
        len(indexedDataset)*0.8), end=len(indexedDataset)-1, dynamic=True)

    # Model 3:
    result_3 = SARIMA_model(indexedDataset, (1, 0, 1), (2, 1, 0, 12))
    pred['forecast3'] = result_3.predict(start=round(
        len(indexedDataset)*0.8), end=len(indexedDataset)-1, dynamic=True)

    # Model 4:
    result_4 = SARIMA_model(indexedDataset, (2, 0, 1), (0, 1, 0, 12))
    pred['forecast4'] = result_4.predict(start=round(
        len(indexedDataset)*0.8), end=len(indexedDataset)-1, dynamic=True)

    # Model 5:
    result_5 = SARIMA_model(indexedDataset, (2, 0, 2), (2, 1, 0, 12))
    pred['forecast5'] = result_5.predict(start=round(
        len(indexedDataset)*0.8), end=len(indexedDataset)-1, dynamic=True)

    # Model 6:
    result_6 = SARIMA_model(indexedDataset, (3, 0, 1), (0, 1, 0, 12))
    pred['forecast6'] = result_6.predict(start=round(
        len(indexedDataset)*0.8), end=len(indexedDataset)-1, dynamic=True)

    result = [result_1, result_2, result_3, result_4, result_5, result_6]

    # calculate RMSE
    pred = pred.dropna()
    rmse_val = [sqrt(mean_squared_error(pred['overall_rating'], pred['forecast1'])),
                sqrt(mean_squared_error(
                    pred['overall_rating'], pred['forecast2'])),
                sqrt(mean_squared_error(
                    pred['overall_rating'], pred['forecast3'])),
                sqrt(mean_squared_error(
                    pred['overall_rating'], pred['forecast4'])),
                sqrt(mean_squared_error(
                    pred['overall_rating'], pred['forecast5'])),
                sqrt(mean_squared_error(pred['overall_rating'], pred['forecast6']))]

    min_val = min(rmse_val)

    best_Model = result[rmse_val.index(min_val)]

    indexedDataset['forecast'] = best_Model.predict(
        start=0, end=len(indexedDataset)-1, dynamic=True)

    return indexedDataset, best_Model


def future_trend(indexedDataset, result, months_num):

    future_dates = [indexedDataset.index[-1] +
                    DateOffset(months=x)for x in range(0, months_num)]
    future_datest_df = pd.DataFrame(
        index=future_dates[1:], columns=indexedDataset.columns)

    future_df = pd.concat([indexedDataset, future_datest_df])
    future_df['forecast'] = result.predict(start=len(
        indexedDataset)-1, end=len(indexedDataset) + months_num-1, dynamic=True)

    for i in range(len(indexedDataset)-1, len(future_df)-1):
        if np.isnan(future_df.iat[i, 7]) == True:
            for j in range(1, len(future_df)-i):
                if (np.isnan(future_df.iat[i+j, 7]) == False):
                    future_df.iat[i, 7] = (
                        future_df.iat[i-1, 7] + future_df.iat[i+j, 7])/2
                    break

    return future_df


def plot_future_trend(future_df, uni_name, course_name):

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=future_df.index, y=future_df['overall_rating'],
                             mode='lines+markers',
                             name='Current trend'))
    fig.add_trace(go.Scatter(x=future_df.index, y=future_df['forecast'],
                             mode='lines+markers',
                             name='Future trend'))

    fig.update_layout(title=course_name + " at " + uni_name,
                      xaxis_title='Date',
                      yaxis_title='Overall Ranking')

    fig.update_layout(legend=dict(yanchor="top", y=1, xanchor="left", x=0))

    # fig.show()
    graphJSON = plotly.io.to_json(fig, pretty=True)
    return json.loads(graphJSON)


def final(result):
    graphs = {}

    df = indexing(result["query"]["data"])
    uni_name = result["query"]["uni_name"]
    course_name = result["query"]["course_name"]

    indexedDataset = visualize_data(df)
    figs1 = plot_Charts(df, indexedDataset)
    graphs = {
        "preprocessing": {
            "graph1": figs1["graph1"],
            "graph2": figs1["graph2"]
        }
    }

    adfuller_test(indexedDataset)
    indexedDataset, result = accurate_model(indexedDataset)
    future_df = future_trend(indexedDataset, result, 24)
    graphs["future_trend_fig"] = plot_future_trend(
        future_df, uni_name, course_name)

    graphs["current_trend_mean"] = round(
        indexedDataset['overall_rating'].mean(), 2)
    graphs["future_trend_mean"] = round(future_df['forecast'].mean(), 2)

    return graphs
