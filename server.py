#IMPORTS
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
import yaml

#imports of our scripts
import parseSchedule
import myMilton



app = Flask(__name__)

@app.route('/getInfo')
def collect_info():


  #get data from website
  user = request.args.get("user")
  password = request.args.get("pass")
  phone = request.args.get("phone")
  week  = request.args.get("week")

  #write sensitive data to yamal
  stream = open("info.yml", 'r')
  data = yaml.safe_load(stream)
  milton_username = user
  milton_pass = password

  data["fb_user"]["UserLogin"] = milton_username
  data["fb_user"]["UserPassword"] = milton_pass

  with open("info.yml", 'w') as yaml_file:
    yaml_file.write( yaml.dump(data, default_flow_style=False))




  #parse and send schedule
  parseSchedule.mainFunction(user,password,phone,week)


  return render_template('success.html')


@app.route('/')
def send_form():
  return render_template('mainPage.html')


if __name__ == '__main__':
  app.run(debug=True)