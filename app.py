from flask import Flask, jsonify, render_template, request, redirect

from database import add_application_to_db, load_jobs_from_db, add_job_to_db, remove_job_from_db, update_job_in_db


app = Flask(__name__)
app.secret_key = 'atlantis-global-2023'

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

@app.route("/job/<int:id>/delete")
def delete_job(id):
    # Assuming load_jobs_from_db returns the job with the given id
    job = load_jobs_from_db(id)[0]

    if job:
        remove_job_from_db(id)
        return redirect('/')  # Redirect to the home page or any other page after deletion
    else:
        return ' did not successfully delete you idiot'

@app.route("/job/<id>/apply")
def apply_to_job(id):
  form=ApplicationForm()
  job = load_jobs_from_db(id)[0]

  add_application_to_db(id, data)
  # send email
  # update data to database 
  return render_template("submitted_application.html", application=data, job=job)

@app.route("/post_job", methods=["POST", "GET"])
def post_job():
  if request.method == "POST":
    data = request.form
    add_job_to_db(data)
    return redirect('/')
  else:
    job =load_jobs_from_db()
    return render_template('post_job.html', job=job)


@app.route("/job/<int:id>/update", methods=["POST", "GET"])
def update_job(id):
    #job = load_jobs_from_db(id)[0]
    #print(job)
    #form = JobForm(obj=job)  # Pass the job data to the form to pre-fill the fields
    #if request.method == "POST" and form.validate_on_submit():
        #update_job_in_db(id, form.data)
        #return redirect('/')
    #return render_template("update_job.html", job=job, form=form)
  if request.method == "POST":
    new_data = request.form

    update_job_in_db(id, new_data)
    return redirect('/')  # Redirect to the home page 
  else:
    job = load_jobs_from_db(id)[0]
  #   print(job)
    return render_template("update_job.html", job=job)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
  