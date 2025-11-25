
import requests
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from rich.console import Console
from rich.panel import Panel
import sys

# Using Ollama Model
OLLAMA_MODEL = "qwen2.5-coder:0.5b"

console = Console()
history = InMemoryHistory()

# Rules

def rule_based_filter(text):
    t = text.lower()

    sensitive_rules = {
        "government": "No data available related to Government and Sensitive data.",
        "politics": "Political information is restricted.",
        "hacking": "I cannot provide hacking-related help.",
        "religion": "Sensitive religious discussions are not allowed.",
        "kill": "Violent data is not being showed.",
        "bomb": "Weapons or explosive-related information is restricted.",
        "sex": "Sexual content is not allowed.",
        "sexual": "Sexual content is restricted.",
        "porn": "Adult content is strictly prohibited.",
        "nude": "Explicit content cannot be provided.",
        "terrorist": "Extremism-related topics cannot be discussed.",
        "hate speech": "Hate speech is strictly prohibited.",

    }

    for k, v in sensitive_rules.items():
        if k in t:
            return v

    return None


# OLLAMA LLM Call
def call_ollama(prompt_text):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt_text,
                "stream": False
            }
        )
        data = response.json()
        return data.get("response", "Error: No response from model")




# Terminal chat
def chatbot_ui():
    console.print(Panel(
        "[bold red] AI ChatBot [/bold red]\n Press ctrl + C to quit",
        border_style="cyan"
    ))

    while True:
        try:

            user_input = prompt("> You: ", history=history)

            if user_input.lower().strip() in ["exit", "quit"]:
                console.print("\n[bold yellow]Goodbye![/bold yellow]")
                break

            # Rule check
            rule_response = rule_based_filter(user_input)
            if rule_response:
                console.print(Panel(rule_response, title=f"{OLLAMA_MODEL}", border_style="red"))
                continue

            # AI reply
            ai_reply = call_ollama(user_input)
            console.print(Panel(ai_reply, title=f"{OLLAMA_MODEL}", border_style="green"))
        except KeyboardInterrupt:
           console.print("\n[bold red]Exiting...[/bold red]")
           break



if __name__ == "__main__":
    chatbot_ui()
