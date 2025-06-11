from flask import Flask, render_template, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests")

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "<h1>Welcome to My Flask App 🚀</h1>"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
