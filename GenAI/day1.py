from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "tgp_v1_wbmaz5Y_CYm70tbNpXrNoLyT_JGdaKodm4kQ08JjQfw"
os.environ["OPENAI_API_BASE"] = "https://api.together.xyz/v1"
llm = ChatOpenAI(model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",temperature=0)

prompt = "You are a wise mentor. Help me learn faster using . Give me three tips"
print(llm.invoke(prompt).content)