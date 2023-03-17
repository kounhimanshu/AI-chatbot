

print("This application/software is an AI based chatbot")
print('Created by Himanshu using openai API')
print()
import openai 
# Set up your OpenAI API key
openai.api_key =("Your API Key")



def askGPT(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages
        )
    output = response["choices"][0]["message"]["content"]
    output = output.lstrip("\n")
    msg.append({"role": "assistant", "content": output})
    print(output)
    return 


msg = [] # this list record the conversation
msg.append({"role": "system", "content": "Hi"})
askGPT(msg)

while True:
    print()
    inp = input("You: ")
    """Exit if user enters exit """
    if inp == 'exit' or inp == 'Exit':
        break
    
    #Clear previous conversation record for fresh new chat
    elif inp == 'clear' or inp == 'Clear':
        print("Previous conversation cleared.   Start New")
        print()
        msg.clear() #clear conversation record
        msg.append({"role": "system", "content": "Hi"})
        askGPT(msg)

    else:
        msg.append({"role": "user", "content": inp}) # add conversation to record for accuracy
        print()
        askGPT(msg)

    
