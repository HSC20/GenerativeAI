#from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai import GenerativeModel
#load_dotenv()
apikey = 'AIzaSyBaEsTJWRAlgNJ4MWfBylH8i-lvwmqo3ys'  # Replace with your key
genai.configure(api_key=apikey)
def gem(question):
    model = GenerativeModel(model_name="gemini-pro")
    response = model.generate_content(question)
    return response.text

question=input("Please enter the question:")
answer = gem(question)
print (answer)