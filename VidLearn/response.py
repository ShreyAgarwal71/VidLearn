from google import genai
from google.genai import types

import PIL.Image

image = PIL.Image.open('PNG/path/here.png')

client = genai.Client(api_key="AIzaSyCZDI2WQbEAVhWH7AxasayTdkBK5yA5Uk8")
response = client.models.generate_content(

    model="gemini-2.0-flash",
    # model="gemini-1.5-flash-8b-exp-0827",
    contents=["INSERT PROMPT HERE", image])

print(response.text)
