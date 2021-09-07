#!/usr/bin/env python
# coding: utf-8

# In[4]:


from random import choice
import random

class Question:
     def __init__(self,prompt,answer):
            self.prompt = prompt
            self.answer = answer
         
            
            
question_prompts =open ("crg.txt", "r") 
content = question_prompts.read()


questions = [
    Question(content[1:355],"a"),
    Question(content[355:684],"b"),
    Question(content[684:1019],"c"),
    Question(content[1019:1259],"a"),
    Question(content[1259:1541],"a"),
    Question(content[1541:2008],"b"),
    Question(content[2008:2355],"a"),
    Question(content[2355:2679],"c"),
    Question(content[2679:2891],"c"),
    Question(content[2891:3289],"b"), 
]                          
random.shuffle(questions)
             

def run_quiz(questions):
    score=0
    for question in questions:
        answer= input(question.prompt)
        if answer == question.answer:
             score += 1
    print("you got", score, "out of", len(questions))
run_quiz(questions)

