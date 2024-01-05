# Readme
[README: Italiano](./README_IT.md)

[README: English](./README.md)

# Script di Generazione Immagini con DALL-E di OpenAI

Questo è uno script Python che ti permette di generare immagini utilizzando il modello DALL-E di OpenAI. Puoi specificare il prompt di input, la chiave API di OpenAI, le dimensioni dell'immagine, il modello da utilizzare, la qualità dell'immagine e utilizza anche un'interfaccia grafica fornita dal file `dall-e_ui.pyw`.

## Installazione

Per utilizzare lo script, segui questi passaggi:

1. Assicurati di avere Python installato sul tuo sistema.
2. Apri il terminale o la riga di comando.
3. Esegui il seguente comando per installare le dipendenze necessarie:

```shell
pip install openai argparse configparser pyqt5
```

## Configurazione

Prima di utilizzare lo script, devi configurare le seguenti opzioni nel file `config.ini`:

- `prompt`: il prompt di input per generare l'immagine.
- `api_key`: la chiave API di OpenAI.
- `size`: le dimensioni dell'immagine desiderate (es. 512x512).
- `model`: il modello da utilizzare (es. dall-e-3).
- `quality`: la qualità dell'immagine (es. standard).

## Utilizzo

Una volta completata l'installazione e la configurazione, puoi utilizzare lo script in due modi:

### Modalità da riga di comando

Esegui il seguente comando per utilizzare lo script da riga di comando:

```shell
python dall-e.py --prompt "Il tuo prompt qui" --api-key "La tua chiave API qui" --size "Dimensioni dell'immagine qui" --model "Modello qui" --quality "Qualità qui"
```

Puoi anche omettere gli argomenti e lo script utilizzerà i valori di default specificati nel file `config.ini`.

Ad esempio, se vuoi generare un'immagine con il prompt "Un gatto nero su uno sfondo bianco", esegui il seguente comando:

```shell
python dall-e.py --prompt "Un gatto nero su uno sfondo bianco"
```

Se vuoi utilizzare un'immagine di dimensioni diverse, aggiungi l'argomento `--size` seguito dalle dimensioni desiderate (es. `--size 1024x1024`).

### Modalità con interfaccia grafica

Esegui il seguente comando per utilizzare lo script con l'interfaccia grafica:

```shell
python dall-e_ui.pyw
```

L'interfaccia grafica ti permetterà di inserire il prompt di input, la chiave API di OpenAI, le dimensioni dell'immagine, il modello da utilizzare e la qualità dell'immagine. Premi il pulsante "Genera Immagine" per avviare la generazione dell'immagine, l'immagine verrà inoltre scaricherà dentro la cartella `img/`.

## Risultati

Lo script genererà un'immagine utilizzando il prompt specificato e la visualizzerà nella console insieme all'URL dell'immagine generata da DALL-E.

# Compilazione
Per creare l'eseguibile del programma `dall-e_ui.pyw`, è necessario utilizzare cx_Freeze, un modulo Python che consente di creare pacchetti eseguibili a partire da script Python.

Prima di tutto, è necessario installare cx_Freeze utilizzando pip. Puoi eseguire il seguente comando nel tuo terminale:

```
pip install cx_Freeze
```

Una volta installato cx_Freeze, puoi procedere con la creazione dell'eseguibile del programma.
Esegui il seguente comando per creare l'eseguibile:

```
python setup.py build
```

Questo comando utilizzerà cx_Freeze per creare l'eseguibile del programma. L'eseguibile verrà creato nella directory `build` all'interno della directory corrente.

Una volta completata la creazione dell'eseguibile, puoi eseguirlo semplicemente facendo doppio clic sul file `dall-e_ui.exe`.

# Uso del modulo
Esempio d'uso del modulo ImageGenerator di dall-e.py
```python
from dall-e import ImageGenerator

# Inizializza ImageGenerator senza passare argomenti (utilizzerà i valori di default da config.ini)
generator = ImageGenerator()

# Genera un'immagine utilizzando i valori di default
response = generator.generate_image()
print(response)

# Oppure, puoi passare argomenti specifici per l'immagine che desideri generare
prompt = "Il prompt per l'immagine"
api_key = "La tua chiave API"
size = "512x512"
model = "dall-e-3"
quality = "standard"

generator_with_params = ImageGenerator(prompt=prompt, api_key=api_key, size=size, model=model, quality=quality)
response = generator_with_params.generate_image() #L'url di risposta con l'immagine
print(response)
```

# Screenshot

![Screenshot](https://github.com/nemmusu/dall-e-interface/blob/main/screenshots/interface_example.png)