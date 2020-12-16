from flask import Flask,render_template,url_for,request, redirect


import csv

import smtplib 

from email.message import EmailMessage

from string import Template

from pathlib import Path

MY_ADDRESS,PASSWORD='hello.hell3096@gmail.com','Hello.hell#3096'

# instance of Flask
app = Flask(__name__)

# print(__name__)


#decorator 
@app.route('/')
def my_home():

    # print(url_for('static', filename='thunder.ico'))
    # return 'Hello, ANEE! Welcome to the Flask App'
    
    return render_template('index.html')




@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  
    if request.method=="POST":
        try:
            data=request.form.to_dict()
            # print(data)
            write_to_csv(data)
            send_mail(data)
            write_to_file(data)
            
            
            return render_template('/thankyou.html',name=data['username'])
        except Exception as e:
            # print(e)
            return f"did not save to database"
    else:
        return "something went wrong" 



def write_to_file(data):
    with open(r'D:\JS\PYTHONCODE\Testing\web_dev\WEBSERVER\database.txt',mode='a') as db:
        email=data['email']
        subject=data['subject']
        name=data['username']
        message=data['message']
        file=db.write(f'\n {name}{email},{subject},{message}')



def write_to_csv(data):
 
    with open(r'D:\JS\PYTHONCODE\Testing\web_dev\WEBSERVER\database2.csv',mode='a',newline='') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        name=data['username']
        print([name,email,subject,message])
        csv_writer = csv.writer(db2,delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])
        print(csv_writer)


def send_mail(data):
   
    email=EmailMessage()
     
    email['from'] = 'Anil K Rajamoni '
    email['to'] = 'rajamonianil0909@gmail.com'
    email['subject'] = "Hey ! AK You Have New Response From Profolio"
    msg=f" \t From Portfolio Website \n Name:{data['username']} \n EMAIL : {data['email']} \n SUBJECT : {data['subject']} \n MESSAGE : {data['message']}"


    email.set_content(msg)


    with smtplib.SMTP('smtp.gmail.com:587') as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(MY_ADDRESS,PASSWORD)
        smtp.send_message(email)
        print('all good boss')


if __name__ == '__main__':
    app.run(debug=True)


"""

# links=[
#     "https://flask.palletsprojects.com/en/1.1.x/quickstart/",

# ]



#  set FLASK_APP=hello.py
# $ flask run or python -m flask run
#  * Running on http://127.0.0.1:5000/  local host 

# set FLASK_ENV=development

# some sites
# https://robohash.org/
# https://xkcd.com/
# http://www.mashup-template.com/
"""