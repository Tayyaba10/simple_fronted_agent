import os 
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

set_tracing_disabled(True)

provider = AsyncOpenAI(api_key=gemini_api_key,base_url="https://generativelanguage.googleapis.com/v1beta/openai")

model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=provider)

agent = Agent(name="fronted Agent",instructions="You are a frontend agent.Your goal is to handle all frontend tasks including HTML, CSS, JavaScript, and UI frameworks.",model=model)
user_question = input("Please enter your question: ")

result = Runner.run_sync(agent,user_question)
print(result.final_output)

