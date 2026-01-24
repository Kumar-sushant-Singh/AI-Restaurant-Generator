import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

#load your .env file
load_dotenv()

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.8
)

def generate_restaurant_name_and_items(cuisine):
    name_prompt=PromptTemplate.from_template(
        "Suggest one fancy name for a {cuisine} restaurant."
    )
    menu_prompt=PromptTemplate.from_template(
        "List 5 menu items for {restaurant_name}. Return as comma seperated list"
    )
    #Build simple chains
    name_chain=name_prompt | llm | StrOutputParser()
    menu_chain=menu_prompt | llm | StrOutputParser()

    #get results
    restaurant_name=name_chain.invoke({"cuisine":cuisine}).strip()
    menu_items=menu_chain.invoke({"restaurant_name":restaurant_name}).strip()

    return{
        "restaurant_name":restaurant_name,
        "menu_items":menu_items
    }
if __name__ == "__main__":
    print("---2026 Environment Check (Conda+ Python 3.10)---")
    try:
        res=llm.invoke("Are you there?")
        print(f"✅ Success! AI says: {res.content}")
    except Exception as e:
        print(f"❌ Error: {e}")