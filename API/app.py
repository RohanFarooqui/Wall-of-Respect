# ==> Imports 

# => Flask Lib
import re
from flask                 import Flask ,url_for,request,jsonify

# => Other Lib
from   datetime import datetime
import emoji

# => Flask 
app = Flask(__name__)

#=> Main Class
class main:
    def __init__(self):
        self.app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    ## ==> Default Route
    @app.route("/",methods=['GET'])
    def main():
        Msg = { "1.Name ": "Wall of Respect",
                "2.Api Version": "1.0",
                "3.Developed by" : "M.ROHAN FAROOQUI©",
                "4.API Status" : "Running "+emoji.emojize(":grinning_face_with_big_eyes:"),}
                #"5.Database Status " :  Database_Status }
        return jsonify(Msg),200






if __name__ == '__main__':
    #app.run(debug=True)  ## For Debug
    app.run()