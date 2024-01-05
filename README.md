# Readme
[README: Italian](./README_IT.md)

[README: English](./README.md)

# DALL-E Image Generation Script by OpenAI

This is a Python script that allows you to generate images using the DALL-E model by OpenAI. You can specify the input prompt, the OpenAI API key, the image dimensions, the model to use, the image quality, and it also uses a graphical interface provided by the `dall-e_ui.pyw` file.

## Installation

To use the script, follow these steps:

1. Make sure you have Python installed on your system.
2. Open the terminal or command line.
3. Run the following command to install the necessary dependencies:

```shell
pip install openai argparse configparser pyqt5
```

## Configuration

Before using the script, you need to configure the following options in the `config.ini` file:

- `prompt`: the input prompt to generate the image.
- `api_key`: the OpenAI API key.
- `size`: the desired image dimensions (e.g. 512x512).
- `model`: the model to use (e.g. dall-e-3).
- `quality`: the image quality (e.g. standard).

## Usage

Once installation and configuration are complete, you can use the script in two ways:

### Command-line Mode

Run the following command to use the script in command-line mode:

```shell
python dall-e.py --prompt "Your prompt here" --api-key "Your API key here" --size "Image dimensions here" --model "Model here" --quality "Quality here"
```

You can also omit the arguments, and the script will use the default values specified in the `config.ini` file.

For example, if you want to generate an image with the prompt "A black cat on a white background", run the following command:

```shell
python dall-e.py --prompt "A black cat on a white background"
```

If you want to use an image of different dimensions, add the `--size` argument followed by the desired dimensions (e.g. `--size 1024x1024`).

### Graphical Interface Mode

Run the following command to use the script with the graphical interface:

```shell
python dall-e_ui.pyw
```

The graphical interface allows you to enter the input prompt, the OpenAI API key, the image dimensions, the model to use, and the image quality. Press the "Generate Image" button to start the image generation, and the image will also be downloaded into the `img/` folder.

## Results

The script will generate an image using the specified prompt and display it in the console along with the URL of the image generated by DALL-E.

# Screenshot

![Screenshot](https://github.com/nemmusu/dall-e-interface/blob/main/screenshots/interface_example.png)