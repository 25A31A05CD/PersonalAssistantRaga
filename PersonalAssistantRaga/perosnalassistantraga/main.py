import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# 1. Load environment variables (API keys)
load_dotenv()

# TIP: You can set your key here temporarily for testing, 
# but in production, use a .env file!
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = "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" # Replace with your actual OpenAI Key

# 2. Initialize the Model
# We use a low temperature for more predictable results
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.8)

# 3. Create a Prompt Template
# This tells the AI how to behave
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that helps to improve my technical skills."),
    ("user", "{topic}")
])

# 4. Create the Chain
# This connects the Prompt -> Model -> Output Parser
chain = prompt | model | StrOutputParser()

# 5. Run the Chain
response = chain.invoke({"topic": "Explain how to write code in c language"})

print("🚀 Captain's Log:")
print(response)