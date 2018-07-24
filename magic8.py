import random
import time
responses = ["Maybe", "Most likely", "Absolutely", "No, just no", "Yes", "I don't think so", "No", "Signs point to yes"]
def answerQuery():
    question = input("Ask Me: ")
    print("hold on, now processing your answer...") 
    time.sleep(3)
    print(random.choice(responses))
answerQuery()