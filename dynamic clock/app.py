from flask import Flask, render_template, jsonify, request
#from apscheduler.schedulers.background import BackgroundScheduler
import requests
from os import system,cpu_count
import psutil
import json
from time import sleep
from datetime import datetime  as dt

system("clear")

def show():
  ct = dt.now()
  dict = {"year":ct.year,"month":ct.month,"day":ct.day,"hour":ct.hour,"minute":ct.minute,"second":ct.second}
  return dict

def load(value):
  if value <= 9:
    var = "◼️◻️◻️◻️◻️◻️"
  elif value <= 19:  
    var = "◼️◼️◻️◻️◻️◻️"
  elif value <= 29:  
    var = "◼️◼️◼️◻️◻️◻️"
  elif value <= 39:  
    var = "◼️◼️◼️◼️◻️◻️"     
  elif value <= 49:  
    var = "◼️◼️◼️◼️◼️◻️"
  elif value <= 59:  
    var = "◼️◼️◼️◼️◼️◼️"  
  return var  

def sec(value):
  if value%2 == 0:
    return "◼️ ◻️"
  else:
    return "◻️ ◼️"


app = Flask(__name__)
 
@app.route("/")
def index():
    test = request.form.get("test")
    tm = show()
    bc = json.dumps(tm)
    return render_template("index.html",message = tm,pattern =load(tm['second']),tick=sec(tm['second']))
  
if __name__ == "__main__":
    #scheduler = BackgroundScheduler()
    #scheduler.add_job(chuck, "interval", seconds=15)
    #scheduler.start()
    app.run(debug=True)


