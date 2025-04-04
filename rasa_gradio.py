from rasa.core.agent import Agent
from rasa.shared.utils.io import json_to_string
import gradio as gr
import asyncio

# Initialize Rasa agent
agent = Agent.load("models")  # Replace with your model path

async def handle_message(message: str, conversation_id: str = "default"):
    """Handle incoming message and get bot response."""
    responses = await agent.handle_text(message, sender_id=conversation_id)
    return "\n".join([response.get("text", "") for response in responses if response.get("text")])

def chat_interface(message: str, history: list):
    """Gradio chat interface function."""
    # Run the async function in the event loop
    response = asyncio.run(handle_message(message))
    return response

# Create Gradio interface
iface = gr.ChatInterface(
    fn=chat_interface,
    title="Jigarkumar Portfolio Chatbot(RASA)",
    description="Interact with Story and rules based Rasa chatbot",
    examples=['skills', 'education', 'projects', 'experience', 'patents']
)

# Start the Gradio app
if __name__ == "__main__":
    iface.launch(share=True)
