# Chatbot mit Rasa - Setup


# MacOS (funktioniert **nicht** auf Apple Silicon)
```
python -m venv rasa-venv
source rasa-venv/bin/activate
```

# MacOS mit Apple Silicon

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
5. Die Datei [env.yml](./macos/env.yml) aus diesem Repository in den Ordner kopieren, in dem Rasa
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
9. Rasa initialisieren und starten:
   ```
   python -m rasa init
   python -m rasa train
   python -m rasa shell
   ```

# Windows

**Achtung**: Rasa läuft offiziell mit Python Version >= 3.7 und < 3.10. Ich selbst habe
es nur mit Version 3.9 auf zwei verschiedenen Windows PCs zum Laufen gebracht!
Die Version 3.9 wird mit der virtuellen Umgebung eingestellt, siehe unten.

Miniconda installieren: https://docs.conda.io/en/latest/miniconda.html -> Miniconda3 Windows 64-bit

Bei der Installation auswählen, dass nur für den **aktuellen User** installiert wird und
im nächsten Dialogfenster die Option zum Setzen der **PATH** Systemvariable aktivieren.

## Git Bash & CMD

1. Virtuelle Umgebung erzeugen und aktivieren
```
conda create -n rasa-venv python=3.9
```
Bei der Frage, ob forgefahren werden soll, mit 'y'es bestätigen.
```
conda activate rasa-venv
```

2. Installiere Rasa
```
pip install rasa
```

3. Initialisieren von Rasa
```
rasa init
```

Git-Bash verhindert manchmal das Anlegen eines virtuellen environments. Hier ein paar links
die helfen könnten:
https://discuss.codecademy.com/t/setting-up-conda-in-git-bash/534473

# Erster Start des Chatbots
```
rasa shell
```

Starten des Chatbots mit Debug Info des Modell-Output:
```
rasa shell nlu
```

# Netz trainieren
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

Stories werden für das Training des Netzes benötigt. Der Bot kann nicht gut generalisieren,
wenn es nicht für ähnliche Konversationspfade mehrere stories gibt. 

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

Im Prinzip eine Map. Bilden Strings oder andere Typen (Strings werden häufig genutzt) auf eigene Datentypen ab, 
das können selbst definierte **Entities** sein.
Wird in **Forms** genutzt um beispielsweise Abfragen zu erstellen: Ein Form (s.u.)
hat ein oder mehrere Slots, welche nach und nach während der Kommunikation mit dem Bot
gefüllt werden. 

# Forms

Forms dienen zur Abfrage von Slots. Ein Form bleibt im Zustand **active** bis alle Slots
durch den User "ausgefüllt" wurden. Beispiele: Bestellvorgang bei einer Pizzeria (welche Pizza,
welche Toppings, Getränk?, etc.), Flugbuchung (von, nach, First- Business- oder Economyclass, extra Fußraum, etc.).
Sobald alles Slots bedient wurden, wechselt das Form in den **inactive** Zustand und eine konkrete
**Action** kann getriggert werden, z.B. eine custom action, die einen GET-Request an den Lieferdienst
schickt und die Bestellung aufgibt.
Solange die Slots noch nicht vollständig ausgefüllt wurden, spricht man
von einer **loop**.
