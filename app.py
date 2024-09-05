from flask import Flask, render_template 

jobs =[ { "id":1, "title": "Data Analyst", "location": "Bengaluru, India", "salary":"Rs 10,00,000"
    },
    {
    "id":2, "title": "Data Scienctist", "location": "Bengaluru, India", "salary":"Rs 20,00,000"
    },
    {
    "id":3, "title": "Software engineer", "location": "Pune, India", "salary":"Rs 8,00,000"
    },
    {
    "id":4, "title": "Cyber Security", "location": "Hyderabad, India", "salary":"Rs 15,00,000"
    }
    ]

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('home.html',job =jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)