# Readme
[README: Italian](./README_IT.md)

[README: English](./README.md)

# DALL-E Image Generation Script by OpenAI

This is a Python script that allows you to generate images using the DALL-E model by OpenAI. You can specify the input prompt, OpenAI API key, image dimensions, model to use, image quality, and it also uses a graphical user interface provided by the `dall-e_ui.pyw` file.

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

Once you have completed the installation and configuration, you can use the script in two ways:

### Command Line Mode

Run the following command to use the script in command line mode:

```shell
python dall-e.py --prompt "Your prompt here" --api-key "Your API key here" --size "Image dimensions here" --model "Model here" --quality "Quality here"
```

You can also omit the arguments and the script will use the default values specified in the `config.ini` file.

For example, if you want to generate an image with the prompt "A black cat on a white background", run the following command:

```shell
python dall-e.py --prompt "A black cat on a white background"
```

If you want to use an image with different dimensions, add the `--size` argument followed by the desired dimensions (e.g. `--size 1024x1024`).

### Graphical User Interface Mode

Run the following command to use the script with the graphical user interface:

```shell
python dall-e_ui.pyw
```

The graphical user interface allows you to enter the input prompt, OpenAI API key, image dimensions, model to use, and image quality. Press the "Generate Image" button to start the image generation process, and the image will also be downloaded inside the `img/` folder.

## Results

The script will generate an image using the specified prompt and display it in the console along with the DALL-E generated image URL.

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

This command will use cx_Freeze to create the program's executable. The executable will be created in the `build` directory inside the current directory.

Once the executable creation is complete, you can run it simply by double-clicking the `dall-e_ui.exe` file.

# Screenshot

![Screenshot](https://github.com/nemmusu/dall-e-interface/blob/main/screenshots/interface_example.png)