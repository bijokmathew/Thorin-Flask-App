import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("FLASH_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<user_name>")
def about_member(user_name):
    person = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == user_name:
                person = obj
    return render_template("member.html", person=person)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, We have recieved your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact Us")


@app.route(("/career"))
def career():
    return render_template("career.html", page_title="Join With Us")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
