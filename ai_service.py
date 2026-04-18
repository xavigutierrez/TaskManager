import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):
    
    if not client.api_key:
        return ["Error: OpenAI API Key is not configured properly."]
    
    try:
        
        prompt = f"""Decompose the following complex task in 3-5 simple, actionable subtasks.

    Task: {description}

    Response format:
    - Subtask 1 
    - Subtask 2
    - Subtask 3
    - etc.

    Respond with just the list of tasks, one task per line and each line starting with a hyphen."""
        
        params = {
            "model": "gpt-5.2",
            "messages": [
                {"role": "system", "content": "You are an assitant who is an expert in taking complex tasks and decomposing them into simple, actionable subtasks"},
                {"role": "user", "content": prompt}
            ],
            "max_completion_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "minimal"
        }

        response = client.chat.completions.create(**params)

        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)

        return subtasks if subtasks else "Error: Uable to generate subtasks."


    except Exception:
        return ["Error: Unable to connect to OpenAI."]