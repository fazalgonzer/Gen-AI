import os 
import json
import traceback
import pandas as pd

from src.Mcq_Generator.Mcq_gen import McqGen
from src.Mcq_Generator.utils.common import *
import streamlit as st 



with open("src/Mcq_Generator/Response.json", 'r') as f:
    file_content = f.read()
    response_json=json.loads(file_content)






list_dif=["simple","intermediate ", "hard"]

st.title("Mcq generator")

with st.form("user_input"):








    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt", "json"])
    


    number=st.number_input("number of Mcqs")

    tone = st.selectbox(
        'Select difficulty',
        list_dif)

    st.write('You selected: ', tone)

    subject=st.text_input("insert the subject",max_chars=29)

    button=st.form_submit_button("Create MCQs")
    

    if button and uploaded_file is not None and subject and tone and number:
        with st.spinner("loading....."):
            text=read_file(uploaded_file)
            obj=McqGen(text,number,subject,tone,response_json)
            response=obj.gen_quiz()
            quiz=response.get("quiz",dict)
            if quiz is not None:
                table_data=get_table_data(quiz)
                st.text(table_data)
                #df=pd.DataFrame(table_data)
               # df.index=df.index+1
               # st.table(df)
            st.write(quiz)

            

            
            

