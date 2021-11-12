from flask import Flask, json

results= { "documents": [{"id": 1, "score": 123456789}], "errors":[] }
health_good = {"status": "healthy"}

app = Flask(__name__)

@app.route('/results', methods=['GET'])
def get_results():
  response = app.response_class(response=json.dumps(results),
                                  status=200,
                                  mimetype='application/json')
  return response

@app.route('/health', methods=['GET'])
def get_health():
  response = app.response_class(response=json.dumps(health_good),
                                  status=200,
                                  mimetype='application/json')
  return response


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True) 
