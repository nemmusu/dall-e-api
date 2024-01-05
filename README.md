# Readme
[README: Italiano](./README_IT.md)

[README: English](./README.md)

# DALL-E by OpenAI Image Generation Script 

This is a Python script that allows you to generate images using the DALL-E model by OpenAI. You can specify the input prompt, OpenAI API key, image dimensions, model to use, image quality, and also use a graphical interface provided by the `dall-e_ui.pyw` file.

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

Once the installation and configuration are complete, you can use the script in two ways:

### Command-line Mode

Run the following command to use the script in the command-line mode:

```shell
python dall-e.py --prompt "Your prompt here" --api-key "Your API key here" --size "Image dimensions here" --model "Model here" --quality "Quality here"
```

You can also omit the arguments and the script will use the default values specified in the `config.ini` file.

For example, if you want to generate an image with the prompt "A black cat on a white background", run the following command:

```shell
python dall-e.py --prompt "A black cat on a white background"
```

If you want to use an image with different dimensions, add the `--size` argument followed by the desired dimensions (e.g. `--size 1024x1024`).

### GUI Mode

Run the following command to use the script with the graphical interface:

```shell
python dall-e_ui.pyw
```

The graphical interface will allow you to enter the input prompt, OpenAI API key, image dimensions, model to use, and image quality. Press the "Generate Image" button to start generating the image, and the image will also be downloaded in the `img/` folder.

### Module Usage
Example usage of the `ImageGenerator` module in `dall-e.py`:

```python
from dall-e import ImageGenerator

# Initialize ImageGenerator without passing any arguments (will use default values from config.ini)
generator = ImageGenerator()

# Generate an image using default values
response = generator.generate_image()
print(response)

# Alternatively, you can pass specific arguments for the image you want to generate
prompt = "The prompt for the image"
api_key = "Your API key"
size = "512x512"
model = "dall-e-3"
quality = "standard"

generator_with_params = ImageGenerator(prompt=prompt, api_key=api_key, size=size, model=model, quality=quality)
response = generator_with_params.generate_image() # The response URL with the generated image
print(response)
```

## Results

The script will generate an image using the specified prompt and display it in the console along with the URL of the image generated by DALL-E.

# Compilation
To create the executable of the `dall-e_ui.pyw` program, you need to use cx_Freeze, a Python module that allows creating executable packages from Python scripts.

First, you need to install cx_Freeze using pip. You can run the following command in your terminal:

```
pip install cx_Freeze
```

Once cx_Freeze is installed, you can proceed with creating the executable of the program.
Run the following command to create the executable:

```
python setup.py build
```

This command will use cx_Freeze to create the executable of the program. The executable will be created in the `build` directory inside the current directory.

Once the creation of the executable is complete, you can simply double-click the `dall-e_ui.exe` file to run it.

# Screenshot

![Screenshot](https://github.com/nemmusu/dall-e-interface/blob/main/screenshots/interface_example.png)