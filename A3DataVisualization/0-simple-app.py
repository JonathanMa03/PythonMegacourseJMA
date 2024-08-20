
#Run code using http://127.0.0.1:8000 and "python3 /Users/jonathanma/Desktop/A3DataVisualization/0-simple-app.py"

import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="Visualiations of Sourse Reviews")
   
    return wp

jp.justpy(app)