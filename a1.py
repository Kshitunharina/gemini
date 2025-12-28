from google import genai
import config

# Create Gemini client
client = genai.Client(api_key=config.GEMINI_API_KEY)

def generate_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # ✅ Updated to supported model
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

def silly_prompt():
    print("Welcome to the AI Prompt Engineering Tutorial!")
    print("Learning Clarity, Specificity, and Context\n")

    vague_prompt = input("Enter a vague prompt: ")
    print("\nAI Response:")
    print(generate_response(vague_prompt))

    specific_prompt = input("\nMake it more specific: ")
    print("\nAI Response:")
    print(generate_response(specific_prompt))

    contextual_prompt = input("\nAdd context: ")
    print("\nAI Response:")
    print(generate_response(contextual_prompt))

if __name__ == "__main__":
    silly_prompt()
