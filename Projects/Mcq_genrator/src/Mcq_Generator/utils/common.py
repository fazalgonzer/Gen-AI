import os 
import PyPDF2
import json
import traceback


def read_file(file):
    

    file_name = file.name

    if file_name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception("Error reading pdf file: " + str(e))
    elif file_name.endswith(".txt"):
        try:
            return file.read().decode("utf-8")
        except Exception as e:
            raise Exception("Error reading txt file: " + str(e))
    elif file_name.endswith(".json"):
        try:
            file_content = file.read().decode("utf-8")
            return json.loads(file_content)
        except Exception as e:
            raise Exception("Error reading json file: " + str(e))
    else:
        raise Exception("Unsupported file format")



def get_table_data(quiz):
    try:
        quiz_dict=json.loads(quiz)
        quiz_table=[]
        

        for key,value in quiz_dict.items():
            mcq=value["mcq"]
            options=" || ".join([


                f"{option}-> {option_value}" for option , option_value in value["options"].items() 


            ]) 
            correct=value["correct"]
            quiz_table.append({"MCQ":mcq,"Choices":options, "Correct":correct})

        return quiz_table
    except Exception as e:
        traceback.print_exception(type(e),e,e.__traceback__)
        return False
    