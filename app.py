from flask import Flask, json

results= { "documents": [{"id": 1, "score": 123456789}], "errors":[] }
health_good = {"status": "healthy"}

api = Flask(__name__)

@api.route('/results', methods=['GET'])
def get_results():
  response = api.response_class(response=json.dumps(results),
                                  status=200,
                                  mimetype='application/json')
  return response

@api.route('/health', methods=['GET'])
def get_health():
  response = api.response_class(response=json.dumps(health_good),
                                  status=200,
                                  mimetype='application/json')
  return response


if __name__ == '__main__':
    api.run() 