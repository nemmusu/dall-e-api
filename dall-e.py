import openai
import argparse
import configparser

def generate_image(prompt, api_key, size, model, quality):
    client = openai.OpenAI(api_key=api_key)
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=1
    )

    image_url = response.data[0].url

    if image_url:
        print(f"Ecco l'immagine generata da DALL-E: {image_url}")
    else:
        print("Si è verificato un errore nella richiesta.")

def main():
    parser = argparse.ArgumentParser(description='Genera un\'immagine utilizzando DALL-E di OpenAI.')
    parser.add_argument('--prompt', required=False, help='Prompt per generare l\'immagine')
    parser.add_argument('--api-key', required=False, help='API Key di OpenAI')
    parser.add_argument('--size', required=False, help='Dimensioni dell\'immagine (es. 512x512)')
    parser.add_argument('--model', required=False, help='Modello da utilizzare (es. dall-e-3)')
    parser.add_argument('--quality', required=False, help='Qualità dell\'immagine (es. standard)')

    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read('config.ini')

    prompt = args.prompt
    api_key = args.api_key
    size = args.size
    model = args.model
    quality = args.quality

    if not prompt:
        prompt = config['OPENAI']['prompt']

    if not api_key:
        api_key = config['OPENAI']['api_key']

    if not size:
        size = config['OPENAI']['size']

    if not model:
        model = config['OPENAI']['model']

    if not quality:
        quality = config['OPENAI']['quality']

    generate_image(prompt, api_key, size, model, quality)

if __name__ == "__main__":
    main()