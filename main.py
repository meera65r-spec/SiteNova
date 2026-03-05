import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("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"))

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Hello AI"
)

print(response.output[0].content[0].text)