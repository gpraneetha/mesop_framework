import random
import time

import mesop as me
import mesop.labs as mel

MODEL = 'llama2'
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings

model = Ollama(model=MODEL)
embeddings = OllamaEmbeddings()

def on_load(e: me.LoadEvent):
  me.set_theme_mode("system")


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/chat",
  title="Chatbot",
  on_load=on_load,
)
def page():
  mel.chat(transform, title="Question Bot", bot_user="Mesop Bot")


def transform(input: str, history: list[mel.ChatMessage]):
    result = model.invoke(input)
    yield result
