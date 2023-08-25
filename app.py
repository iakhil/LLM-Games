import os 
import openai
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == 'POST':
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="You are a well-renowned investor who is capable of determining nonsense pitches. You invest generously in startups that are genuine yet ambitious. A no-name founder comes to you for funding. Role play the conversation. Start immediately.",
            temperature=0.6,
        )

        result = response.args.get("result")
        return render_template("index.html", result)