import openai

openai.api_key = 'YOUR_OPENAI_KEY'

def generate_response(query):
    # Your logic to generate response using OpenAI Chat Completions API
    # Replace the code below with your implementation

    temperature = 0.2
    top_p = 1
    engine = 'gpt-3.5-turbo'

    messages=[
    {"role": "system", "content": "You are a travel iternary planner. You will get the travel destination with the days. Need to create a iternary out of it. If you not able to understand the destination you can give error meesage."},
    {"role": "user", "content": query}]
    response = openai.ChatCompletion.create(
    model=engine,
    messages = messages,
    # prompt=prompt,
    temperature=temperature,
    # max_tokens=min(4096-estimated_prompt_tokens, max_tokens),
    top_p=top_p
    )

    response = response['choices'][0]['message']['content'].strip()
        
    return response
