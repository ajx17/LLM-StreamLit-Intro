from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

def generate_location(temp, continent):
    llm = OpenAI(temperature= 0.5)

    promp_name = PromptTemplate(
        input_variables = ['temp' , 'continent'],
        template= "I want to live somewhere that is typically {temp}, and is located in {continent}. Suggest me 5 good places to live, as a list and without an explanation of why."
    )

    name_chain = LLMChain(llm=llm, prompt=promp_name)
    response = name_chain({'temp':temp, 'continent':continent})
    return response

if __name__ == "__main__":
    print(generate_location('Hot', 'North America'))