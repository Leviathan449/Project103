import pandas as pd 
import plotly.express as pe 


data = pd.read_csv("project103.csv")

graph = pe.scatter(data , x = "date", y = "cases", color = "country")

graph.show()

