from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key
API_KEY = os.getenv("API_KEY")

# Initialize Gemini client (replace with your real API key or load from env)
client = genai.Client(api_key=API_KEY)

# Prompt template for structured extraction
TEMPLATE = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_gemini(dom_chunks, parse_description, model_name="gemini-2.5-flash"):
    
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        prompt = TEMPLATE.format(dom_content=chunk, parse_description=parse_description)

        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )

        print(f"[Parser] Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response.text.strip())

    return "\n".join(parsed_results)


# standalone test (only runs when executing parser.py directly)
if __name__ == "__main__":
    chunks = [
        "<div>Phone: 12345</div>",
        "<div>Email: test@example.com</div>"
    ]
    description = "Extract only the email address"
    print(parse_with_gemini(chunks, description))
