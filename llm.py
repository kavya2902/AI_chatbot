import subprocess

def ask_llm(prompt):

    result = subprocess.run(
        ["ollama", "run", "llama2"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout
