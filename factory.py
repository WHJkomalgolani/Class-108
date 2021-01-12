import random
import plotly.figure_factory as ff
#Plotly's Python API contains a figure factory module which includes many wrapper 
# functions that create unique chart types that are not yet included in plotly.js,
#  Plotly's open-source graphing library. The figure factory functions create a full figure,
#  so some Plotly features,
#  such as subplotting, should be implemented slightly differently with these charts.


dice_result = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)
    

fig = ff.create_distplot([dice_result],["Result"]) 
fig.show()   