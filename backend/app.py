from flask import Flask, send_file, jsonify
from flask_cors import CORS
#from matplotlib import pyplot as plt

import ml
import time

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET'])



@app.route("/prediction/<algo>/<rooms>/<year>/<area>/<plt>")
def prediction(algo,rooms,year,area,plt):
    print('starting prediction')
    # n1 = escape(n1)
    # a = calc.add(int(n1), int(n2))
    #print(rooms)
    rooms = int(rooms)
    year = int(year)
    area = int(area)
    algo = str(algo)
    plot=str(plt)
    pred = str(ml.predict(algo,rooms,year,area))
    img = str(ml.interpret_instance(algo,rooms,year,area))
    img1 = str(ml.interpret_model(algo,rooms,year,area,plt))
    print('prediction ended')
    #print(pred)
    data = {"algorithm": algo, "prediction": pred,"image_water":'/images/img.jpg',"image_summ":'/images/img1.jpg'}
    print(data)
    return data
 #   return "<h1>" + str(a) + "</h1>" 
 


@app.route("/images/<filename>")
def send_an_image(filename):
    img_file = './images/' + filename 
    return send_file(img_file)

if __name__ == "__main__":
    app.run()