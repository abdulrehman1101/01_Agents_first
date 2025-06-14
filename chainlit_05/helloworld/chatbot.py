import chainlit as cl
from assistant import handle_user_input

@cl.on_message
async def main(message: cl.Message):
    reply = await handle_user_input(message.content)
    await cl.Message(content=reply).send()
