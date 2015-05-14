__author__ = 'roy'

from flask import Flask, render_template, redirect
from flask_wtf import Form
from wtforms import StringField, SubmitField
import plotter

class SuburbForm(Form):
    suburb = StringField("suburb")
    submit = SubmitField("Go")

app = Flask("__name__")
app.secret_key = "THIS IS SECRET"

@app.route("/", methods=("GET", "POST"))
def index():
    form = SuburbForm()
    if form.validate_on_submit():
        return redirect("/map/" + form.suburb.data.upper())
    return render_template("index.html", form=form)

@app.route("/map/<suburb>")
def display_map(suburb=""):
    plotter.create_map(suburb)
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)
