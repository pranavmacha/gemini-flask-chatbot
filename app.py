from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Your Gemini API key
genai.configure(api_key="AIzaSyDn31EcJLctnM8hMt6i4wu9SNBWG1Nj-Uw")
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    response_text = ""

    if request.method == "POST":
        user_input = request.form["message"]
        if user_input:
            response = model.generate_content(user_input)
            response_text = response.text

    return render_template("index.html", user_input=user_input, response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
