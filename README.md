# Chatbot mit Rasa - Setup


1. Virtual Environment erstellen und aktivieren
#### MacOS (funktioniert **nicht** auf Apple Silicon)
```
python -m venv rasa-venv
source rasa-venv/bin/activate
```

#### MacOS mit Apple Silicon

Achtung: Es muss **mindestens MacOS Version 12.0** installiert sein, da es keine
vorkompilierten Pakete von TensorFlow für frühere Versionen von MacOS+Apple Silicon gibt!

1. Homebrew installieren. Dazu dieser Anleitung folgen:
   https://brew.sh/index_de
2. Dependencies mit brew installieren:
   ```
   brew install libpq libxml2 libxmlsec1 pkg-config postgresql
   ```
3. Miniconda herunterladen und installieren:
   https://docs.conda.io/en/latest/miniconda.html -> 	Miniconda3 macOS Apple M1 64-bit pkg
4. Im Ordner, in dem Rasa installiert werden soll, sicherstellen, dass keine virtuelle Umgebung
   aktiv ist:
   ```
   conda deactivate
   ```
   Der Command prompt sollte ungefähr so aussehen:
   ```
   michaeleggers@mbair chatbot %
   ```
   und **nicht** so:
   ```
   (base) michaeleggers@mbair chatbot % 
   ```
5. Die Datei [env.yml](./env.yml) aus diesem Repository in den Ordner kopieren, in dem Rasa
   installiert werden soll.

6. Die Virtuelle Umgebung starten und Dependencies herunterladen:
   ```
   conda env create -v --name myrasabot -f env.yml
   ```
7. Aktivieren des Virtuellen Environments:
   ```
   conda activate myrasabot
   ```
8. Einige Dependencies müssen manuell heruntergeladen und installiert werden:
   ```
   pip install git+https://github.com/vpol/text.git --no-deps
   pip install git+https://github.com/RasaHQ/rasa-sdk@3.0.2 --no-deps
   pip install git+https://github.com/RasaHQ/rasa.git@3.0.4 --no-deps
   ```
9.  Rasa initialisieren und starten:
   ```
   python -m rasa init
   python -m rasa train
   python -m rasa shell
   ```

#### Windows (CMD)
```
python3 -m venv rasa-venv
rasa-venv\Scripts\activate.bat
```
#### Windows (Git Bash)
```
python3 -m venv rasa-venv
source ./rasa-venv/Scripts/activate
```

2. Installiere Rasa
```
python -m pip install rasa
```

3. Initialisieren von Rasa
```
python -m rasa init
```
Bei Frage nach Projektpfad ```Yes```  (aktueller Pfad).
Bei Frage, ob ein initiales Modell trainiert worden, ebenfalls ```Yes```.

## Erster Start des Chatbots
```
rasa shell
```

Starten des Chatbots mit Debug Info des Modell-Output:
```
rasa shell nlu
```

### Netz trainieren
```
rasa train
```
(später interessant, wenn die Config-files geändert werden)

# Die wichtigsten Config-files

## nlu.yml

Enthält **Intents** und **Examples**. Fürs Erste: Intents sind Gruppen von
Aufforderungen bzw. Fragen des Users an den Chatbot. Zum Beispiel:

```yml
- intent: mood_great
  examples: |
    - perfect
    - great
    - amazing
    - feeling like a king
    - wonderful
    - I am feeling very good
    - I am great
    - I am amazing
    - I am going to save the world
    - super stoked
    - extremely good
    - so so perfect
    - so good
    - so perfect
```

## stories.yml

Stellt man sich die **Intents** als Legosteine vor, dann besteht eine **Story**
aus mehreren Steinen: Intents werden aufeinandergesteckt, wodurch eine
Sequenz aus **Intents** und **Actions** entsteht. Bsp:

```yml
- story: happy path
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_great
  - action: utter_happy
```
# Utterances
Text der direkt vom Chatbot zurückgegeben wird.

# Action
Triggert ein selbst programmiertes Action-Event. Diese Actions werden beispielsweise
in der Datei ```actions.py``` abgelegt. Die Datei wird dann beim Starten des 
**Rasa Actions Server** als Modul(?) dazugeladen.

# Entities

Eine **Entity** hat einen _Namen_ und einen _Type_. Bsp:
```yml
[Michael](student_name)

[Michael] -> Name
(student_name) -> Type
```

# Slots

Ein Slot ist wie eine Entity, aber **'long lived'**.


