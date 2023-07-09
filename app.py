from flask import Flask, render_template, request, jsonify
from chat_completions import generate_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='templates',)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.form['query']
    response = generate_response(user_query)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
