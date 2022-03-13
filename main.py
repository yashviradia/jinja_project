from flask import Flask, render_template
import requests
import random
from datetime import date

# API URLs and Parameters

AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"


app = Flask(__name__)

todays_date = date.today()


@app.route("/")
def home():
    return "<h1>Hello, World!</h1>"


@app.route("/year")
def year():
    random_number = random.randint(1, 10)
    current_year = todays_date.year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<username>")
def use_api(username):
    parameters = {
        "name": username
    }
    agify_response = requests.get(url=AGIFY_URL, params=parameters)
    genderize_response = requests.get(url=GENDERIZE_URL, params=parameters)

    agify_data = agify_response.json()["age"]
    genderize_data = genderize_response.json()["gender"]

    return render_template("index.html", name=username, gender=genderize_data, age=agify_data)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/8c8cb60a3116ae7e94ed"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    print(all_posts)
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


