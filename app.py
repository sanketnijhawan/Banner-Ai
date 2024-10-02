from flask import Flask, render_template, request
import requests
import io
from PIL import Image

app = Flask(__name__)

# Hugging Face API configuration
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
headers = {"Authorization": "Bearer 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"}  # Replace with your token

def query_huggingface_api(prompt):
    # Function to query the Hugging Face API with the user's prompt
    payload = {
        "inputs": prompt,
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    # Check the response status
    if response.status_code == 200:
        return response.content  # Return image bytes
    else:
        print(f"Error: {response.status_code} - {response.text}")  # Log error details
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user prompt from the form
        prompt = request.form["prompt"]
        
        # Call the Hugging Face API
        image_bytes = query_huggingface_api(prompt)
        
        if image_bytes:
            # Open and save the image
            image = Image.open(io.BytesIO(image_bytes))
            image.save("static/generated_image.png")  # Save the image in the static folder

            # Display the generated image
            return render_template("index.html", image_url="generated_image.png", prompt=prompt)
        else:
            # If the image generation failed, show an error
            return render_template("index.html", error="Failed to generate image.")
    
    # Render the form initially
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
