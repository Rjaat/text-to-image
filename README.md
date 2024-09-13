# Text to Image Generator

This AI based Text-to-Image Generator is a powerful and user-friendly web application that leverages [state-of-the-art AI models](https://huggingface.co/black-forest-labs) to generate stunning images from text prompts. Built with Streamlit and integrated with Hugging Face's model hub, this application allows users to create unique, high-quality images with ease.

## Features


- Two AI models to choose from: [FLUX RealismLora](https://huggingface.co/black-forest-labs/FLUX.1-dev) and [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell)

- Adjustable creativity and image quality settings

- Real-time image generation

- Downloadable high-resolution output

## Installation

1. Clone this repository:

   ```

   git clone https://github.com/Rjaat/text-to-image.git

   cd text-to-image

   ```

2. Install the required dependencies:

   ```

   pip install -r requirements.txt

   ```

3. Set up your Hugging Face API key:

   - Create a .env file in the project root

   - Add your API key: HUGGINGFACE_API_KEY=your_api_key_here

## Usage

1. Run the Streamlit app:

   ```

   streamlit run app.py

   ```

2. Open your web browser and go to `http://localhost:8501`

3. Choose an AI model, enter your prompt, adjust the creativity and image quality settings, and click "Generate Image"

4. View your generated image and download it if desired

## Example Generated Images

Here are some example images generated using this application:

1. Prompt: "A futuristic cityscape with flying cars"
![A futuristic cityscape with flying cars](https://github.com/user-attachments/assets/89d4aba4-31d0-4211-a2e9-a6c844207d11)

   

2. Prompt: "A serene forest lake at sunset"

   ![A serene forest lake at sunset](https://github.com/user-attachments/assets/b43e7e27-7bfc-432e-a904-677d41001d79)


3. Prompt: "An alien marketplace on a distant planet"
![An alien marketplace on a distant planet](https://github.com/user-attachments/assets/ac9f43a3-d3f2-4583-899c-224964888874)

   

4. Prompt: "A cyberpunk-style portrait of a robot"
![A cyberpunk-style portrait of a robot](https://github.com/user-attachments/assets/c901bbd7-7c9d-4ed0-8cab-43a536896567)

   

## Acknowledgements

- [Streamlit](https://streamlit.io/) 

- [Hugging Face](https://huggingface.co/) 

- [BlackForestLabs.ai](https://blackforestlabs.ai/) -- The creators of the FLUX RealismLora and FLUX.1-schnell models 
