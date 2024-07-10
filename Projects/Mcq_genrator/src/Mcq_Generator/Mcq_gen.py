import os
import json
import pandas as  pd 
import traceback

from  dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain




class McqGen:
    def __init__(self,text,number,subject,tone,response_json) :
        self.llm = ChatGroq(
                groq_api_key=,
                model_name="Llama3-8b-8192"
            )


        self.text=text
        self.number=number
        self.tone=tone
        self.subject=subject
        self.response=response_json
        self.template1="""
                                    Text:{text}
                                    Your are an expert MCQ maker. Given above text, it is your job to \
                                    create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
                                    Make sure the question are not repeated and check all the questions to be conforming the text as well.
                                    Make sure to format your response like RESPONSE_JSON and use it as guide. \
                                    Ensure to make {number} MCQs
                                    ### RESPONSE_JSON
                                    {response_json}

                                    """
        self.template2="""
                                    You are an expert english grammarian and writer . Given a Multiple Choice Quiz for {subject} students. \
                                    You need to evaluate the complexity of the question and a give a complete anaylsis of the quiz .Only use at max 50 words for a complexity
                                    if the quiz is not at per with the cognitive and analytical abibilities of the student ,\
                                    update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities.
                                    Quiz_MCQs:
                                    {quiz}
                                    Check from an expert English Writer of the above quiz :
                                    """
    def gen_quiz(self):

        
        quiz_generation_prompt=PromptTemplate(
                input_variables=["text","number","subject","tone","response_json"],
                template=self.template1


        )
        quiz_chain=LLMChain(llm=self.llm,prompt=quiz_generation_prompt,output_key="quiz",verbose=True)
        quiz_evaluation_prompt=PromptTemplate(input_variables=["subject","quiz"], template=self.template2)

        Eval_chain=LLMChain(llm=self.llm,prompt=quiz_evaluation_prompt,output_key="review", verbose=True)
        from langchain.chains import SequentialChain
        generate_chain=SequentialChain(chains=[quiz_chain,Eval_chain], input_variables=["text","number","subject","tone","response_json"],output_variables=["quiz","review"]
                                    ,verbose=True)
        response=generate_chain({"text":self.text,"number":self.number,"subject":self.subject,"tone":self.tone,"response_json":self.response})

        return response
        


