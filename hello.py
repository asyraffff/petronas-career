from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Kuala Lumpur',
        'salary' : 'RM4500'
    },
    {
        'id' : 2,
        'title' : 'Pi Analyst',
        'location' : 'Kuala Lumpur',
        'salary' : 'RM5500'
    },{
        'id' : 3,
        'title' : 'Data Scientist',
        'location' : 'Kuala Lumpur',
        'salary' : 'RM6000'
    },{
        'id' : 4,
        'title' : 'Petroleum Engineer',
        'location' : 'Ketereh',
        'salary' : 'RM4500'
    }
]

@app.route("/")
def hello_petronas():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True)