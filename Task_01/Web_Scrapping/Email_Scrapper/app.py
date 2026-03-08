from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)

# ----------------------------
# Email Extract Function
# ----------------------------
def extract_emails_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        html = response.text

        emails = re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            html
        )
        return list(set(emails))
    except:
        return []

# ----------------------------
# Route
# ----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    emails = []

    if request.method == "POST":
        url = request.form["url"]
        emails = extract_emails_from_url(url)

    return render_template("index.html", emails=emails)

# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
