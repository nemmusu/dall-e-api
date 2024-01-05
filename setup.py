import sys
from cx_Freeze import setup, Executable

# Specifica i moduli necessari
include_modules = [
    'PyQt5',
    'openai',
    'configparser',
    'threading',
    'requests',
    'PyQt5.QtWidgets',
    'PyQt5.QtGui',
    'PyQt5.QtCore',
]

# Crea l'eseguibile
executables = [Executable('dall-e_ui.pyw', base="Win32GUI")]

# Configurazione per la build
build_options = {
    'includes': include_modules,
    'include_files': [
        ('config.ini'),  # Includi il file di configurazione
        # Aggiungi eventuali altri file necessari
    ],
}

# Impostazioni per la build
setup(
    name='Dall-e API interface',
    version='1.0',
    description='API Interface for Dall-e',
    options={'build_exe': build_options},
    executables=executables
)