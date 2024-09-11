document.getElementById('bannerForm').addEventListener('submit', async function (event) {
  event.preventDefault();
  
  const bannerText = document.getElementById('bannerText').value;
  const productImage = document.getElementById('productImage').files[0];
  const theme = document.getElementById('theme').value;

  const formData = new FormData();
  formData.append('bannerText', bannerText);
  formData.append('productImage', productImage);
  formData.append('theme', theme);

  try {
    // Send form data to your Gemini API endpoint
    const response = await fetch('YOUR_GEMINI_API_ENDPOINT', {
      method: 'POST',
      body: formData
    });

    const result = await response.json();
    // Assuming the response contains a URL of the generated banner
    document.getElementById('bannerImage').src = result.bannerImageUrl;
    document.getElementById('bannerImage').style.display = 'block';
  } catch (error) {
    console.error('Error generating banner:', error);
  }
});
