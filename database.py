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

