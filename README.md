# Readme
[README: Italian](./README_IT.md)

[README: English](./README.md)

## Table of Contents

- [Readme](#readme)
    - [README: Italiano](./README_IT.md)
    - [README: English](./README.md)
- [DALL-E Image Generation Script](#dall-e-image-generation-script)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [Command-line mode](#command-line-mode)
    - [GUI mode](#gui-mode)
    - [Module usage](#module-usage)
  - [Results](#results)
- [Compilation](#compilation)
- [Executable](#executable)
- [Screenshot](#screenshot)


# DALL-E Image Generation Script

This is a Python script that allows you to generate images using the DALL-E model by OpenAI. You can specify the input prompt, the OpenAI API key, the image dimensions, the model to use, and the image quality. It also provides a graphical user interface (GUI) provided by the `dall-e_ui.pyw` file.

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
- `size`: the desired image dimensions (e.g., 512x512).
- `model`: the model to use (e.g., dall-e-3).
- `quality`: the image quality (e.g., standard).

## Usage

Once installation and configuration are completed, you can use the script in two ways:

### Command-line mode

Run the following command to use the script in command-line mode:

```shell
python dall-e.py --prompt "Your prompt here" --api-key "Your API key here" --size "Image dimensions here" --model "Model here" --quality "Quality here"
```

You can also omit the arguments, and the script will use the default values specified in the `config.ini` file.

For example, if you want to generate an image with the prompt "A black cat on a white background," run the following command:

```shell
python dall-e.py --prompt "A black cat on a white background"
```

If you want to use an image with different dimensions, add the `--size` argument followed by the desired dimensions (e.g., `--size 1024x1024`).

### GUI mode

Run the following command to use the script with the graphical user interface:

```shell
python dall-e_ui.pyw
```

The GUI allows you to enter the input prompt, OpenAI API key, image dimensions, model to use, and image quality. Press the "Generate Image" button to start image generation, and the image will also be downloaded to the `img/` folder.

### Module usage
Example usage of the ImageGenerator module from dall-e.py without passing arguments (uses default values from config.ini):

```python
from dall-e import ImageGenerator

# Initialize ImageGenerator without passing arguments (uses default values from config.ini)
generator = ImageGenerator()

# Generate an image using the default values
response = generator.generate_image()
print(response)
```

Example usage of the ImageGenerator module from dall-e.py by passing arguments:

```python
from dall-e import ImageGenerator
# You can pass specific arguments for the image you want to generate
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

The script will generate an image using the specified prompt and display the URL of the image generated by DALL-E.

# Compilation
To create the executable of the `dall-e_ui.pyw` program, you need to use cx_Freeze, a Python module that allows you to create executable packages from Python scripts.

First, you need to install cx_Freeze using pip. You can run the following command in your terminal:

```
pip install cx_Freeze
```

Once cx_Freeze is installed, you can proceed with creating the executable of the program.
Run the following command to create the executable:

```
python setup.py build
```

This command will use cx_Freeze to create the program's executable. The executable will be created in the `build` directory within the current directory.

Once the executable creation is complete, you can run it simply by double-clicking the `dall-e_ui.exe` file.

# Executable

In the `build` folder, there is a zip file that contains an executable version of the program (already compiled and ready to use).

# Screenshot

![Screenshot](https://github.com/nemmusu/dall-e-interface/blob/main/screenshots/interface_example.png)