from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://6x33avd9nis33j29xn7m:pscale_pw_jVCukQFK1ES7IncxnBzyCtD43fdfTQVmOzc9ASSetPn@aws.connect.psdb.cloud/atlantiscareers"
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
  

  


