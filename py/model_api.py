from openai import OpenAI

# Initialize client with your endpoint
client = OpenAI(
    base_url="http://localhost:5001/v1" # e.g., "http://localhost:8000/v1"
)

def get_llm_response(prompt):
    pre_token = "<think>\n"
    try:
        response = client.chat.completions.create(
            model="your-model-name",
            messages=[
                {"role": "system", "content": "You are a content safety assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            prefix = pre_token,
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error during API call: {e}")
        return None
