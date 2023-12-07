from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://6lvdzbx1c7vssw2vp4h0:pscale_pw_FNoCzlKyJvB4a2Emis9dU50q1JHu2v4zwX9tpAe5N1J@aws.connect.psdb.cloud/atlantiscareers"
engine = create_engine(
  db_connection_string,
  connect_args= {
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem",
        }
    } ) 

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs"))

  result_dicts = [r._asdict() for r in result.all()]
  print(result_dicts)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = [r._asdict() for r in result.all()]
    return jobs
  

  


