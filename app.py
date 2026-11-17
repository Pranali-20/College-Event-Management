
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store college events
events = [
    {
        "name": "Technical Fest",
        "date": "2026-12-10",
        "venue": "College Auditorium",
        "description": "Technical competitions and workshops"
    },
    {
        "name": "Cultural Fest",
        "date": "2026-12-15",
        "venue": "College Ground",
        "description": "Dance, music and cultural activities"
    }
]

# Home page
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        event = {
            "name": request.form["name"],
            "date": request.form["date"],
            "venue": request.form["venue"],
            "description": request.form["description"]
        }

        events.append(event)

        return redirect("/")

    return render_template("index.html", events=events)


# Start application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
