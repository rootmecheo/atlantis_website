from flask import Flask, jsonify, render_template, request

from database import load_jobs_from_db, add_application_to_db

import requests

app = Flask(__name__)

@app.route( "/")
def main():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)
 
@app.route("/job/<id>")
def show_job(id):
  job = load_jobs_from_db(id)  # Use load_jobs_from_db to fetch a specific job by id
  if job:
    return render_template('jobpage.html', job=job[0])  
  else:
    return "Job not found", 404  # If the job is not found, return a 404 error

@app.route("/job/<id>/apply", methods=["POST"])
def apply_to_job(id):
  data = request.form
  job = load_jobs_from_db(id)[0]

  add_application_to_db(id, data)
  # send email
  # update data to database 
  return render_template("submitted_application.html", application=data, job=job)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
  