from sqlalchemy import create_engine
import pandas as pd
import openai
from langchain.chains import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables (OpenAI API key and Database URL)
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_MODEL = os.getenv('OPENAI_API_MODEL')

openai.api_key = OPENAI_API_KEY

# Create the engine for PostgreSQL
engine = create_engine("postgresql://customer-feedback:admin@localhost:5432/customer-feedback")

# LLM Setup: Use LangChain's OpenAI class for the language model
llm = OpenAI(model=OPENAI_API_MODEL, openai_api_key=OPENAI_API_KEY)

# Wrap the engine with the SQLDatabase class from LangChain
db = SQLDatabase(engine)

# Create the SQLDatabaseChain
sql_chain = SQLDatabaseChain(llm=llm, database=db)

# LangChain SQL generation template
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="Translate the following natural language query into a valid SQL query:\n\nQuestion: {question}\n\nSQL Query:"
)

def get_sql_query_from_nl(question: str) -> str:
    """Takes a natural language question and returns a SQL query."""
    # Use LangChain to convert the question to an SQL query
    result = sql_chain.run(question)
    return result
