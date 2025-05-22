from flask import Flask, request
import base64
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Dictionary to hold file buffers by unique ID
file_buffers = {}

@app.route('/testexf/<path:encoded_data>', methods=['GET'])
def receive_chunk(encoded_data):
    try:
        # Decode base64 data
        decoded = base64.urlsafe_b64decode(encoded_data.encode()).decode()
        
        # Extract unique_id and chunk data
        # Format expected: "<unique_id>:<chunk_data>"
        unique_id, chunk = decoded.split(':', 1)

        # Append chunk to the corresponding file buffer
        if unique_id not in file_buffers:
            file_buffers[unique_id] = []
        file_buffers[unique_id].append(chunk)

        # Optional: You can flush to file periodically or on a special request

        return f"Chunk received for {unique_id}", 200
    except Exception as e:
        return f"Error processing chunk: {e}", 400

@app.route('/finalize/<unique_id>', methods=['GET'])
def finalize_file(unique_id):
    try:
        chunks = file_buffers.get(unique_id, [])
        if not chunks:
            return "No data found for this ID", 404

        filepath = os.path.join(UPLOAD_FOLDER, f"{unique_id}.txt")
        with open(filepath, 'w') as f:
            f.write(''.join(chunks))
        
        del file_buffers[unique_id]
        return f"File written to {filepath}", 200
    except Exception as e:
        return f"Error writing file: {e}", 500

if __name__ == '__main__':
    app.run()
