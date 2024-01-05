import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QTextEdit, QProgressBar, QComboBox
from PyQt5.QtGui import QPixmap
from openai import OpenAI
import configparser
import threading
import requests
from PyQt5.QtCore import QThread, pyqtSignal, QTimer, QSize
from datetime import datetime
import os

class ImageGeneratorThread(QThread):
    image_generated = pyqtSignal(str)

    def __init__(self, prompt, api_key, size, model, quality):
        super().__init__()
        self.prompt = prompt
        self.api_key = api_key
        self.size = size
        self.model = model
        self.quality = quality

    def run(self):
        client = OpenAI(api_key=self.api_key)
        response = client.images.generate(
            model=self.model,
            prompt=self.prompt,
            size=self.size,
            quality=self.quality,
            n=1
        )

        image_url = response.data[0].url if response.data else None

        self.image_generated.emit(image_url)
        self.quit()

class ImageDownloaderThread(QThread):
    image_downloaded = pyqtSignal(bool)

    def __init__(self, image_url, prompt):
        super().__init__()
        self.image_url = image_url
        self.prompt = prompt
        self.file_name = None  

    def run(self):
        if self.image_url:
            response = requests.get(self.image_url)
            if response.status_code == 200:
                current_time = datetime.now().strftime("%d.%m.%Y-%H.%M.%S")
                folder_path = 'img/'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                clean_prompt = "".join(x for x in self.prompt if x.isalnum() or x in (' ', '_', '-'))
                clean_prompt = clean_prompt[:60]
                self.file_name = f"{folder_path}[{current_time}-{clean_prompt}].png" 
                with open(self.file_name, "wb") as file:
                    file.write(response.content)
                self.image_downloaded.emit(True)
            else:
                self.image_downloaded.emit(False)
        self.quit()

class DALL_E_Interface(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DALL-E Interface")
        self.setGeometry(100, 100, 400, 400)

        self.default_size = QSize(400, 400)

        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.prompt_label = QLabel("Prompt:")
        self.prompt_input = QTextEdit(self.config['OPENAI']['prompt'])
        self.layout.addWidget(self.prompt_label)
        self.layout.addWidget(self.prompt_input)

        self.api_key_label = QLabel("API Key:")
        self.api_key_input = QLineEdit()
        self.api_key_input.setEchoMode(QLineEdit.Password)
        self.api_key_input.setText(self.config['OPENAI']['api_key'])
        self.layout.addWidget(self.api_key_label)
        self.layout.addWidget(self.api_key_input)

        self.model_label = QLabel("Modello:")
        self.model_options = ['dall-e-2', 'dall-e-3']
        self.model_combo_box = QComboBox()
        self.model_combo_box.addItems(self.model_options)
        self.model_combo_box.setCurrentText(self.config['OPENAI']['model'])
        self.layout.addWidget(self.model_label)
        self.layout.addWidget(self.model_combo_box)

        self.size_label = QLabel("Dimensioni (es. 512x512):")
        self.size_options_dall_e_2 = ['1024x1024', '1024x1792', '1792x1024', '256x256', '512x512']
        self.size_options_dall_e_3 = ['1024x1024', '1024x1792', '1792x1024']
        self.size_combo_box = QComboBox()
        if self.config['OPENAI']['model'] == 'dall-e-2':
            self.size_combo_box.addItems(self.size_options_dall_e_2)
        else:
            self.size_combo_box.addItems(self.size_options_dall_e_3)
        self.size_combo_box.setCurrentText(self.config['OPENAI']['size'])
        self.layout.addWidget(self.size_label)
        self.layout.addWidget(self.size_combo_box)

        self.quality_label = QLabel("Qualità:")
        self.quality_options = ['standard', 'hd']
        self.quality_combo_box = QComboBox()
        self.quality_combo_box.addItems(self.quality_options)
        self.quality_combo_box.setCurrentText(self.config['OPENAI']['quality'])
        self.layout.addWidget(self.quality_label)
        self.layout.addWidget(self.quality_combo_box)

        self.generate_button = QPushButton("Genera e Scarica Immagine")
        self.generate_button.clicked.connect(self.generate_image)
        self.layout.addWidget(self.generate_button)

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

        self.url_text_edit = QTextEdit()
        self.url_text_edit.setReadOnly(True)
        self.layout.addWidget(self.url_text_edit)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 3)  
        self.layout.addWidget(self.progress_bar)

        self.central_widget.setLayout(self.layout)

        self.autosave_configuration()

    def autosave_configuration(self):
        def save_config():
            self.config['OPENAI']['prompt'] = self.prompt_input.toPlainText()
            self.config['OPENAI']['api_key'] = self.api_key_input.text()
            self.config['OPENAI']['model'] = self.model_combo_box.currentText()
            self.config['OPENAI']['size'] = self.size_combo_box.currentText()
            self.config['OPENAI']['quality'] = self.quality_combo_box.currentText()

            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)

        self.prompt_input.textChanged.connect(save_config)
        self.api_key_input.textChanged.connect(save_config)
        self.model_combo_box.currentTextChanged.connect(self.update_size_options)
        self.quality_combo_box.currentTextChanged.connect(save_config)

    def update_size_options(self):
        if self.model_combo_box.currentText() == 'dall-e-2':
            self.size_combo_box.clear()
            self.size_combo_box.addItems(self.size_options_dall_e_2)
        else:
            self.size_combo_box.clear()
            self.size_combo_box.addItems(self.size_options_dall_e_3)

    def update_image_list(self, url):
        self.url_text_edit.setPlainText(url)

    def generate_image(self):
        self.image_label.clear()
        self.url_text_edit.clear()
        #QApplication.processEvents()
        #self.resize(self.default_size)  # Ripristino le dimensioni predefinite della finestra
        prompt = self.prompt_input.toPlainText()
        api_key = self.api_key_input.text()
        size = self.size_combo_box.currentText()
        model = self.model_combo_box.currentText()
        quality = self.quality_combo_box.currentText()

        self.progress_bar.setValue(1)  
        self.generator_thread = ImageGeneratorThread(prompt, api_key, size, model, quality)
        self.generator_thread.image_generated.connect(self.update_image_list)
        self.generator_thread.image_generated.connect(self.download_image) 
        self.generator_thread.start()

    def download_image(self, image_url):
        if image_url:
            self.progress_bar.setValue(2)  

            self.downloader_thread = ImageDownloaderThread(image_url, self.prompt_input.toPlainText())
            self.downloader_thread.image_downloaded.connect(self.download_complete)
            self.downloader_thread.start()
        else:
            QMessageBox.warning(self, "Errore", "Genera prima un'immagine.")

    def download_complete(self, success):
        self.progress_bar.setValue(3)  

        if success:
            pixmap = QPixmap(self.downloader_thread.file_name)  
            self.image_label.setPixmap(pixmap.scaled(self.default_size))  
        else:
            QMessageBox.warning(self, "Errore", "Impossibile scaricare l'immagine.")

    def resizeEvent(self, event):
        self.resize(self.default_size)  

def run_gui():
    app = QApplication(sys.argv)
    window = DALL_E_Interface()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_gui()
