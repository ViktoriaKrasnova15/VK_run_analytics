from flask import Flask, render_template, request, redirect, url_for
import os

basedir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/student_tf')
def student_tf_hist():
    return render_template("student_tf.html")

@app.route("/sechenovrunnersclub")
def sechenovrunnersclub_hist():
    return render_template("sechenovrunnersclub.html")

@app.route("/studathletics")
def studathletics_hist():
    return render_template("studathletics.html")

@app.route("/ranepa_run")
def ranepa_run_hist():
    return render_template("ranepa_run.html")

@app.route("/runlab")
def runlab_hist():
    return render_template("runlab.html")

@app.route("/begvpitere")
def begvpitere_hist():
    return render_template("begvpitere.html")

@app.route("/enjoytherunspb")
def enjoytherunspb_hist():
    return render_template("enjoytherunspb.html")

@app.route("/goldenringrun")
def goldenringrun_hist():
    return render_template("goldenringrun.html")

@app.route("/runcomrun")
def uncomrun_hist():
    return render_template("runcomrun.html")

@app.route("/moscowmarathon")
def moscowmarathon_hist():
    return render_template("moscowmarathon.html")

@app.route("/general_hist")
def general_hist():
    return render_template("general_hist.html")

if __name__ == '__main__':
    app.run(debug=True)