from flask import Flask
from housing.logger import logging


app=Flask( __name__ )
@app.route("/",methods=['GET','POST'])
def index():
    logging.info("we r testing logging")
    return "Starting Machine Learning Project"

    



if __name__ == "__main__":
    app.run(debug=True)
