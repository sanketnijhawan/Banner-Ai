import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Check response status and content for errors
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content[:200]}...")  # Print the first 200 characters

    if response.status_code == 200:
        return response.content
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

image_bytes = query({
    "inputs": "dog with blanket as costume and glasses riding a horse between valley of mountains",
})

if image_bytes:
    try:
        image = Image.open(io.BytesIO(image_bytes))
        image.show()  # Display the image
        image.save("generated_image.png")  # Save the image
        print("Image saved as 'generated_image.png'")
    except Exception as e:
        print(f"Failed to open image: {e}")
else:
    print("No valid image bytes received.")
