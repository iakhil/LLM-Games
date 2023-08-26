import os 
import openai
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
prompt = "You are a well-renowned investor who is capable of determining nonsense pitches. You invest generously in startups that are genuine yet ambitious. A no-name founder comes to you for funding. Role play the conversation. Start immediately."
                

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == 'GET':
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Hi! I am a founder looking for some seed funding."},
                ],
            temperature=0.6,
        )

    elif request.method == 'POST':
        user_text = request.form["user-input"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
                 messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_text},
                ],
            temperature=0.6,
        )
        
        print(response)
        result = response['choices'][0]['message']['content']
        print(result)
        return render_template("index.html", result=result)

    return render_template("index.html", result="no result")

if __name__ == "__main__":
    app.run(debug=True)