from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def  index():
    try:
            raise Exception ("We are testing customer exception")
    except Exception  as e:
             housing =  HousingException(e,sys)
             logging.info("housing error message")
             logging.info("testing logging mod")

      
    return "CI CD pipeline has establised."


if __name__== "__main__" :
       app.run(debug=True)


