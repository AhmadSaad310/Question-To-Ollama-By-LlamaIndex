from llama_index.llms.ollama import Ollama

llm = Ollama(model='llama3.2')

reponse = llm.stream_complete('give me top 10 germnay movie in history , return data as json')

for i in reponse:
    print(i.delta,end="")