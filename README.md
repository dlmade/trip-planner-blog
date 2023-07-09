# File understanding

1. Flask App:
   - `app.py`: The entrypoint file that initializes the Flask application and defines the routes.

2. UI:
   - `index.html`: The HTML template for the user interface.
   - `styles.css`: The CSS file for styling the UI.
   - `script.js`: The JavaScript file for handling user interactions and making API requests.

3. Chat Completions API:
   - `chat_completions.py`: A module that interacts with the OpenAI Chat Completions API to generate responses based on user queries.

# Run the project in local

1. Install requirements.
   - `pip install requirements.txt`

2. Add your openai api key in code.
   - Change the `openai.api_key` variable in chat_completions.py file.

3. Run the app.py
   - `python app.py`

# Run the project in lambda

1. Make sure your local and lambda python version is same.

2. Install the requirements.txt in current folder. 
   - `pip install -r requirements.txt -t .`

3. Delete the urllib3 folder.

4. zip the all the files and folder from current directory. 

5. upload that zip into the lambda.