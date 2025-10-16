import requests

BASE_URL = "http://localhost:8000"

def generate_essay(topic):
    """Call the essay endpoint to generate a 200-word essay."""
    url = f"{BASE_URL}/essay/invoke"
    payload = {"input": {"topic": topic}}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["output"]
    else:
        return f"Error {response.status_code}: {response.text}"

def generate_poem(topic):
    """Call the poem endpoint to generate a 200-word poem."""
    url = f"{BASE_URL}/poem/invoke"
    payload = {"input": {"topic": topic}}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["output"]
    else:
        return f"Error {response.status_code}: {response.text}"

if __name__ == "__main__":
    print("=== LangChain + Ollama Offline Client ===")
    topic = input("Enter a topic: ")

    print("\n--- Essay ---")
    print(generate_essay(topic))

    print("\n--- Poem ---")
    print(generate_poem(topic))
