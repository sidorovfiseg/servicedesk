
from langchain_core.messages import SystemMessage, HumanMessage
from external.llm.gigachat import giga_chat_llm
from external.api import BaseAPI

class GigaChatAPI(BaseAPI):
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    async def send_message(self, prompt: str, context: str = None) -> str:
        messages = [SystemMessage(content=self.system_prompt)]
        if context:
            messages.append(HumanMessage(content=f'Report fragment:\n{context}\nQuestion:\n{prompt}'))
        else:
            messages.append(HumanMessage(content=prompt))
        
        output = await giga_chat_llm.ainvoke(messages)
        return output.content
