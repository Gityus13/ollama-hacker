import requests
import json

def get_analysis(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "hacker-ai", # This is the custom model you just created
        "prompt": prompt,
        "stream": False # Get the full response at once
    }
    try:
        response = requests.post(url, json=payload, timeout=300) # Added timeout
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()['response']
    except requests.exceptions.RequestException as e:
        return f"Error communicating with Ollama: {e}"

# Load target data from target.txt
try:
    with open("target.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("Error: target.txt not found. Create target.txt with your input data.")
    exit()

# Define your task - MODIFY THIS LINE FOR YOUR SPECIFIC OBJECTIVE
task = f"Analyze the following architecture for critical vulnerabilities and provide a step-by-step exploitation plan: {data}"

# Execute and get the result
print("Executing analysis. This may take a moment...")
result = get_analysis(task)

# Write the output to output.txt
with open("output.txt", "w") as f:
    f.write(result)
print("Analysis complete. Check output.txt for results.")

