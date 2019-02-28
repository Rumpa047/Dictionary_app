from flask import Flask, render_template, request
import pymysql
import json

db = pymysql.connect(user="root", passwd="", host="localhost", database="dictionary_data")
print("connection success....")
mycursor = db.cursor()
sql_word = "SELECT * FROM english_bangle_word_meaning"
mycursor.execute(sql_word)
data = mycursor.fetchall()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    meaning = None
    if request.method =='POST':
        word = request.form['search']
        for row in data:
            if row[1] == word:
                meaning = row[2]
                break
        return render_template('about.html', meaning= meaning)

    return render_template('home.html')


@app.route('/About')
def about():
    return render_template('about.html')


@app.route('/test')
def test():
    lst = []
    for item in data:
        lst.append( {'word': item[1], 'meaning': item[2]})

    return render_template('test.html', data=lst)


# @app.route('/data')
# def data():
#     # print(print (json.dumps(data,indent=4)))
#     # return render_template('data.html', data = (json.dumps(data)))
#     return render_template('data.html', data = data)
#
#     # return render_template('test.html', data = data)

if __name__ == '__main__':

     app.run(debug=True)