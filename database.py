import os

from sqlalchemy import create_engine, text

# retrieve environment variable
db_connection_string = os.environ["DB_CONNECTION_STRING"]

engine = create_engine(
  db_connection_string,
  connect_args= {
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem",
        }
    } ) 

# read from the database
def load_jobs_from_db(id=None):
  if id:
      with engine.connect() as conn:
          result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
          jobs = [r._asdict() for r in result.all()]
          return jobs
  else:
      # If no id is provided, fetch all jobs
      with engine.connect() as conn:
          result = conn.execute(text("SELECT * FROM jobs"))
          jobs = [r._asdict() for r in result.all()]
          return jobs

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    conn.execute(query, {
        "job_id": job_id,
        "full_name": data["full_name"],
        "email": data["email"],
        "linkedin_url": data["linkedin_url"],
        "education": data["education"],
        "work_experience": data["work_experience"],
        "resume_url": data["resume_url"]
    })

# add job to the database
def add_job_to_db(data):
    try:
        with engine.connect() as conn:
            query = text("INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements) VALUES (:title, :location, :salary, :currency, :responsibilities, :requirements)")
            conn.execute(query, {
                "title": data["title"],
                "location": data["location"],
                "salary": data["salary"],
                "currency": data["currency"],
                "responsibilities": data["responsibilities"],
                "requirements": data["requirements"]
            })
        return True  # Return True to indicate successful insertion
    except Exception as e:
        print(f"Error occurred while adding job to database: {e}")
        return False  # Return False to indicate insertion failure

# remove job from the database
def remove_job_from_db(job_id):
  with engine.connect() as conn:
    query = text("DELETE FROM jobs where id = :id")
    conn.execute(query, {"id": job_id})


# update job in the database
def update_job_in_db(job_id, new_data):
  try:
      with engine.connect() as conn:
          query = text("""
              UPDATE jobs
              SET title = :title,
                  location = :location,
                  salary = :salary,
                  currency = :currency,
                  responsibilities = :responsibilities,
                  requirements = :requirements
              WHERE id = :id
          """)
          conn.execute(query, {**new_data, "id": job_id})
  except Exception as e:
      print(f"Error occurred while updating job: {e}")