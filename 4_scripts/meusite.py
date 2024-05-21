from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('homepage.html')
@app.route('/hora/')

def hora():
    data = datetime.today()
    data2 = str (data)[0:10]
    horae = str (data)[11:19]
    return render_template('hora.html').format(data2, horae)

if __name__ == '__main__':
    app.run(debug=True)