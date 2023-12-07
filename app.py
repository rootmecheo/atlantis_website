from flask import Flask, jsonify, render_template

from database import load_jobs_from_db

app = Flask(__name__)

@app.route( "/")
def main():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)