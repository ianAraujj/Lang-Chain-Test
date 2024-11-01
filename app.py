from decouple import config
from langchain_anthropic import ChatAnthropic

ANTHROPIC_APP_KEY = config('ANTHROPIC_APP_KEY')

chat_model = ChatAnthropic(
    model='claude-3-5-sonnet-20241022',
    temperature=0,
    api_key=ANTHROPIC_APP_KEY
)

print(chat_model.invoke("Why are bees become extinct?"))

