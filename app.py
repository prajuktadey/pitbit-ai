import openai
import json

# Set up your OpenAI API key
openai.api_key = 'your-api-key-here'

def parse_resume(resume_text):
    prompt = """
    You are an AI assistant specialized in parsing resumes. Your task is to take the following resume and convert it into a structured JSON format. Follow these guidelines:

    1. Identify and extract key sections such as Personal Information, Education, Work Experience, Skills, Projects, and any other relevant sections present in the resume.
    2. For each section, create appropriate JSON keys and values.
    3. Ensure that dates, job titles, company names, and other important details are correctly captured.
    4. For lists (such as skills or responsibilities), use JSON arrays.
    5. If any information is unclear or missing, use "N/A" as the value.
    6. Format the JSON output with proper indentation for readability.

    Here's the resume to parse:

    {resume}

    Please provide the parsed resume in JSON format.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that parses resumes into JSON format."},
            {"role": "user", "content": prompt.format(resume=resume_text)}
        ]
    )

    return json.loads(response.choices[0].message['content'])

# Example usage
with open('sample_resume.txt', 'r') as file:
    resume_text = file.read()

parsed_resume = parse_resume(resume_text)
print(json.dumps(parsed_resume, indent=2))
