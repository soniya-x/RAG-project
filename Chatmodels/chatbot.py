from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage


model=ChatMistralAI(
      model= "mistral-small-latest",
      temperature=0.9
         
)

print("Choose your AI Mode")
print("Press 1 for Angry Mode")
print("Press 2 for Funny Mode")
print("Press 3 for Sad Mode")

choice = int(input("Enter your choice: "))

if choice == 1:
    mode = "You are an angry AI assistant. Answer every question in an angry and frustrated tone."
elif choice == 2:
    mode = "You are a funny AI assistant. Answer every question with humor and jokes."
elif choice == 3:
    mode = "You are a sad AI assistant. Answer every question in a sad and emotional tone."
else:
    mode = "You are a helpful AI assistant."

print("\nSelected Mode:")
print(mode)


'''
SIMPLE BASIC STEP USING SHORT  TERM MEMORY
messages=[] //short terms memory 
print("----------------Welcome type 0 to exit the application---------------------")
while True:
        prompt=input("You : ")
        messages.append(prompt)
        if prompt=="0":
                break
        response=model.invoke(messages)
        messages.append(response.content)


        print("Bot : ",response.content)
print(messagees)

In this(current shoert term memory)we face some problems
No role seperations(no sys,/user)
just row string
memory keeps growing infinitely
will hit token limit
aip cost increase over time
slower resposne 
''' 


messages=[
    SystemMessage(content=mode)

]
print("----------------Welcome type 0 to exit the application---------------------")
while True:
        prompt=input("You : ")
        messages.append(HumanMessage(content=prompt))
        if prompt=="0":
                break
        response=model.invoke(messages)
        messages.append(AIMessage(content=response.content))


        print("Bot : ",response.content)
print(messages)



