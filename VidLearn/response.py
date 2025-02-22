from google import genai
from google.genai import types

import PIL.Image


image = PIL.Image.open('/path/to/image.png')

client = genai.Client(api_key="GEMINI_API_KEY")
response = client.models.generate_content(

    # model="gemini-2.0-flash",
    model="gemini-1.5-flash-8B",
    contents=["What is this image?", image])

print(response.text)

with open("response.txt", "w") as file:
    file.write(response.text)
