import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create_engine allows you to access the SQLITE database
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

# Reflecting database tables
Base.prepare(engine, reflect=True)

# References for each table
Measurement = Base.classes.measurement

Station = Base.classes.station

# Session link in Python
session = Session(engine)

app = Flask(__name__)

@app.route('/')

def addition(number_one, number_two):

    sum = number_one + number_two
    return sum

num_one = int(input('Please enter first number: '))
num_two = int(input('Please enter second number: '))
print(addition(num_one, num_two))