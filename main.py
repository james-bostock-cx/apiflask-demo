# Change 1
# Change 2
# Change 3
# Change 4
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_user_code_unsafe():
    user_code = request.args.get('code')
    result = eval(user_code)
    return result['value']

@app.route('/execute-test', methods=['POST'])
def execute_user_code_unsafe_test():
    user_code = request.args.get('code')
    result = eval(user_code)
    return result['value']
