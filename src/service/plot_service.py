import pandas as pd
import json
import plotly
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots



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
      title = result["query1"]["course_name"] +" vs. "+ result["query2"]["course_name"]
   
   fig.update_layout(title = title ,
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
      y=df1['course_contents_rating'],mode='lines+markers'),
      row=1, col=1
   )

   fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Course's Content at "+result["query2"]["uni_name"],
      x=df2.index,
      y=df2['course_contents_rating'],mode='lines+markers'),
      row=1, col=1
   )


   fig.add_trace(go.Scatter(name=result["query1"]["course_name"] + " Docents at "+result["query1"]["uni_name"],
      x=df1.index,
      y=df1['docents_rating'],mode='lines+markers'),
      row=1, col=2
   )

   fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Docents at "+result["query2"]["uni_name"],
      x=df2.index,
      y=df2['docents_rating'],mode='lines+markers'),
      row=1, col=2
   )

   fig.add_trace(go.Scatter(name=result["query1"]["course_name"] + " Lectures at "+result["query1"]["uni_name"],
      x=df1.index,
      y=df1['lectures_rating'],mode='lines+markers'),
      row=2, col=1
   )

   fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Lectures at "+result["query2"]["uni_name"],
      x=df2.index,
      y=df2['lectures_rating'],mode='lines+markers'),
      row=2, col=1
   )

   fig.add_trace(go.Scatter(name=result["query1"]["course_name"] + " Organization at "+result["query1"]["uni_name"],
      x=df1.index,
      y=df1['organization_rating'],mode='lines+markers'),
      row=2, col=2
   )

   fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Organization at "+result["query2"]["uni_name"],
      x=df2.index,
      y=df2['organization_rating'],mode='lines+markers'),
      row=2, col=2
   )


   fig.add_trace(go.Scatter(name=result["query1"]["course_name"] + " Library at "+result["query1"]["uni_name"],
      x=df1.index,
      y=df1['library_rating'],mode='lines+markers'),
      row=3, col=1
   )

   fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Library at "+result["query2"]["uni_name"],
      x=df2.index,
      y=df2['library_rating'],mode='lines+markers'),
      row=3, col=1
   )

   fig.add_trace(go.Scatter(name=result["query1"]["course_name"] + " Digitization at "+result["query1"]["uni_name"],
      x=df1.index,
      y=df1['digitization_rating'],mode='lines+markers'),
      row=3, col=2
   )
   fig.add_trace(go.Scatter(name=result["query2"]["course_name"] + " Digitization at "+result["query2"]["uni_name"],
      x=df2.index,
      y=df2['digitization_rating'],mode='lines+markers'),
      row=3, col=2
   )
   # fig.show()

   graphJSON = plotly.io.to_json(fig, pretty=True)
   return graphJSON


def indexing2(data):
   df= pd.DataFrame( [[ij for ij in i] for i in data] )
   df.rename(columns={0: 'course_contents_rating', 1: 'docents_rating',
                     2: 'lectures_rating', 3: 'organization_rating',
                     4: 'library_rating', 5: 'digitization_rating',
                     6: 'overall_rating', 7: 'author_age',
                     8: 'author_gender', 9: 'author_current_semester',
                        }, inplace=True)
   
   return df



def single_comparaison_mode(uni_name, course_name, dataFrame, compare_mode):
   if dataFrame.size !=0 :    
         
      ## Compare based on Age:
      if compare_mode == 1:
         dataFrame=dataFrame.groupby(['author_age']).mean(numeric_only = True).reset_index()           
         fig = px.bar(dataFrame, x = "author_age", y = "overall_rating",
               color = "author_age",
               labels={
                  "author_age": "Age Range",
                  "overall_rating": "Average Ratings",
                  },
               title = course_name +" Course Rating: based on age at " + uni_name)
               
               
      ## Compare based on Gender:        
      elif compare_mode == 2:
            
            dataFrame=dataFrame.groupby(['author_gender']).mean(numeric_only = True).reset_index()           
            fig = px.bar(dataFrame, x = "author_gender", y = "overall_rating",
                        color = "author_gender",
                        labels={
                           "author_gender": "Male vs. Female",
                           "overall_rating": "Average Ratings",
                           },
                        title = course_name +" Course Rating: based on gender at " + uni_name)
               
         
      ## Compare based on Current Semester:
      elif compare_mode == 3:
            
            dataFrame=dataFrame.groupby(['author_current_semester']).mean(numeric_only = True).reset_index()           
            fig = px.bar(dataFrame, x = "author_current_semester", y = "overall_rating",
                        color = "author_current_semester",
                        labels={
                           "author_current_semester": "Current Semester",
                           "overall_rating": "Average Ratings",
                           },
                        title = course_name + " Course Rating: based on current semester at " + uni_name)
               
      # fig.show()
      graphJSON = plotly.io.to_json(fig, pretty=True)
      return graphJSON


def single_comparaison_detailed_charts_mode(df, compare_mode):
   if df.size !=0 :    
        
      ## Create subplots
      fig = make_subplots(rows=2, cols=3, start_cell="top-left")
      
      ## Compare based on Age:
      if compare_mode == 1:
         df=df.groupby(['author_age']).mean(numeric_only = True).reset_index() 
         df1 = df.iloc[: , [0,1]].copy()  
         df2 = df.iloc[: , [0,2]].copy() 
         df3 = df.iloc[: , [0,3]].copy() 
         df4 = df.iloc[: , [0,4]].copy() 
         df5 = df.iloc[: , [0,5]].copy() 
         df6 = df.iloc[: , [0,6]].copy() 

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
            
        ## Compare based on Gender:        
      elif compare_mode == 2:
         df=df.groupby(['author_gender']).mean(numeric_only = True).reset_index() 
         df1 = df.iloc[: , [0,1]].copy()  
         df2 = df.iloc[: , [0,2]].copy() 
         df3 = df.iloc[: , [0,3]].copy() 
         df4 = df.iloc[: , [0,4]].copy() 
         df5 = df.iloc[: , [0,5]].copy() 
         df6 = df.iloc[: , [0,6]].copy() 

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
            
        ## Compare based on Current Semester:
      elif compare_mode == 3:
         df=df.groupby(['author_current_semester']).mean(numeric_only = True).reset_index() 
         df1 = df.iloc[: , [0,1]].copy()  
         df2 = df.iloc[: , [0,2]].copy() 
         df3 = df.iloc[: , [0,3]].copy() 
         df4 = df.iloc[: , [0,4]].copy() 
         df5 = df.iloc[: , [0,5]].copy() 
         df6 = df.iloc[: , [0,6]].copy()

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
   
   graphJSON1 = single_comparaison_mode(uni_name1, course_name1, df1, compare_mode)
   graphJSON2 = single_comparaison_mode(uni_name2, course_name2, df2, compare_mode)

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