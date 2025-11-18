import requests

HOST = "http://localhost:11434"

data = {
    "model": "llama3:latest",
    "prompt": "Explain remediation in digital media in two sentences.",
    "stream": False,  # ← this is the important bit
}

r = requests.post(f"{HOST}/api/generate", json=data, timeout=300)

# Now the response is a single JSON object
data = r.json()
print(data["response"])