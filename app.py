from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
{
"id":1 ,
"title": "Data Analyst",
"company": "Google",
"location": "Mountain View",
"salary": "$120,000"

},
{
  "id":2,
  "title": "Frontend Engineer",
  "company": "Amazon",
  "location": "Seattle",
  "salary": "$110,000"
},
{
  "id":3,
  "title": "Data Scientist",
  "company": "Microsoft",
  "location": "Redmond",
  "salary": "$90,000"
},
  {
    "id":4,
    "title": "Backend engineer",
    "company": "safaricom",
    "location": "Mountain View",
    "salary": "$100,000"
}
]

@app.route( "/")
def main():
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)