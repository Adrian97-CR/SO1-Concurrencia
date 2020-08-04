#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,request
from flask_cors import CORS
from datetime import date,timedelta
from apscheduler.scheduler import Scheduler


app = Flask(__name__)
CORS(app)

# @app.route("/search_function", methods=['POST'])
# def search_func():
#     return (search_function(request.form['code'],request.form['search']))

# @app.route("/get_functions", methods=['GET'])
# def get_func():
#     return ('hola mundo')

@app.route("/get_functions", methods=['POST'])
def get_func():
    my_job()
    return ('hola mundo')

if __name__ == "__main__":
    app.run(host='0.0.0.0')



# Start the scheduler
sched = Scheduler()
sched.start()
delta2 = timedelta(hours=24)

exec_date = date(2009, 11, 6)
# Define the function that is to be executed
def my_job():
    exec_date = date.today()
    delta2 = timedelta(hours=24)
    print(delta2, exec_date, exec_date+delta2)
    # Store the job in a variable in case we want to cancel it
    # job = sched.add_date_job(my_job, exec_date+delta2)
