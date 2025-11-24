from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Optional


load_dotenv()
model = ChatOllama(model="llama3.2")


#schema

class Review(TypedDict):
    key_theme: Annotated[list[str], "write down all the key themes discussed in the preview in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment review in positive, negative, neutral"]
    pros: Annotated[Optional[list[str]], "write down list"]

structured_model = model.with_structured_output(Review)


result = structured_model.invoke("""The Samsung Galaxy S24 Ultra is a premium flagship loaded with power, AI features, and an improved design. It comes with a titanium frame, a flat 6.8" AMOLED 120Hz display, and is powered by the Snapdragon 8 Gen 3 chip. The cameras deliver excellent detail with a 200MP main sensor, and Samsung’s Galaxy AI adds smart features like Circle to Search, live translation, and AI photo editing. Battery life is strong with a 5000mAh battery, though fast charging is still limited to 45W.

Pros
* Premium titanium design + flat bright 120Hz display
* Powerful Snapdragon 8 Gen 3 performance
* Excellent 200MP camera and strong 5x optical zoom
* Galaxy AI features are genuinely useful
* Built-in S Pen and good stylus experience
* Long 7 years of OS & security updates

Cons
* 45W charging is slower than many competitors
* Very expensive
* Large and heavy phone
* Ultra-wide camera is not a huge upgrade
* No charger in the box""")

print(result)
print(result['pros'])
print(result['summary'])
