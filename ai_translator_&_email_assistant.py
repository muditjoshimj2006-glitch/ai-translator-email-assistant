# AI translator and email assistant

from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("API_KEY")
)

print("="*60)
print("     WELCOME TO THE AI TRANSLATOR AND EMAIL ASSISTANT")
print("="*60)


# List of languages
languages = [
    "english",
    "hindi",
    "marwari",
    "french"
]



# function translator
def translate_text(text,language):
    if language in languages:
        print("-"*60)
        print(f"TRANSLATING YOUR TEXT INTO YOUR PREFERABLE LANGUAGE : {language}.....")
        print(f"Your original text : {text}")

        prompt = f"""Translate {text} into {language} language into simple words
        keep it professional
        don't use technical jargons
        in very short
        max 1 line
        your name is {name}"""

        response = client.models.generate_content(
           model="gemini-3.6-flash",
           contents=prompt,
)
        print("-" * 60)
        return response.text
        
        

    else:
        print("No language found")
        return None



# function calling {translator}
text = input("Enter text : ")
language = input("Enter language : ")
name = input("Enter your name : ")
language = language.lower()


translated = translate_text(text,language)
if translated is None:
     exit()

print()
print("-"*60)
print(f"Your translated text : {translated}")
print("-"*60)
print()




# user demand asking
qst = input("Do you want to send this as an email? [yes/no] : ")
flag = False

if qst == "no":
    print("THANK YOU FOR USING OUR PROGRAM")


elif qst == "yes":
    flag = True


else:
    print("Invalid input")




# function {send_email}
def send_email(to,subject,body):
        print("-"*60)

        print(f"TO : {to}")
        print(f"SUBJECT : {subject}")
        print(f"BODY : {body}")
        print("-"*60)
        


#function calling {send_email}
if flag:
    to = input("Whom do you want to send email? :  ")
    subject = input("What is the subject topic? : ")
    body = input("Enter body : ")

    send_email(to,subject,body)

    prompt_email = f"""Write an professsional email in short
using these information
to : {to}
subject : {subject}
body : {body}
in short
don't use technical jargon
make it simple
use best formatting
very short
email formated cleaned and organized
"""

    response_email = client.models.generate_content(
      model="gemini-3.6-flash",
      contents=prompt_email
)

    print()
    print("-"*60)
    print(f"EMAIL : {response_email.text}")
    print()

print("-"*60)
print("THANK YOU FOR USING OUR PROGRAM") 
print("-"*60)