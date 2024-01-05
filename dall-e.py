import openai
import argparse
import configparser

class ImageGenerator:
    def __init__(self, prompt=None, api_key=None, size=None, model=None, quality=None):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.prompt = prompt if prompt else self.config['OPENAI']['prompt']
        self.api_key = api_key if api_key else self.config['OPENAI']['api_key']
        self.size = size if size else self.config['OPENAI']['size']
        self.model = model if model else self.config['OPENAI']['model']
        self.quality = quality if quality else self.config['OPENAI']['quality']

    def generate_image(self):
        client = openai.OpenAI(api_key=self.api_key)
        response = client.images.generate(
            model=self.model,
            prompt=self.prompt,
            size=self.size,
            quality=self.quality,
            n=1
        )

        image_url = response.data[0].url if response.data else None

        if image_url:
            return image_url
        else:
            return None

def main():
    parser = argparse.ArgumentParser(description='Genera un\'immagine utilizzando DALL-E di OpenAI.')
    parser.add_argument('--prompt', required=False, help='Prompt per generare l\'immagine')
    parser.add_argument('--api-key', required=False, help='API Key di OpenAI')
    parser.add_argument('--size', required=False, help='Dimensioni dell\'immagine (es. 512x512)')
    parser.add_argument('--model', required=False, help='Modello da utilizzare (es. dall-e-3)')
    parser.add_argument('--quality', required=False, help='Qualità dell\'immagine (es. standard)')

    args = parser.parse_args()

    generator = ImageGenerator(
        prompt=args.prompt,
        api_key=args.api_key,
        size=args.size,
        model=args.model,
        quality=args.quality
    )
    image = generator.generate_image()
    print(f"Ecco l'immagine generata da DALL-E: {image}")
    
if __name__ == "__main__":
    main()
