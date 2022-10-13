# Chatbot mit Rasa - Setup


# MacOS (funktioniert **nicht** auf Apple Silicon)

1. Miniconda herunterladen und installieren:
   https://docs.conda.io/en/latest/miniconda.html#macos-installers -> 	Miniconda3 macOS Intel x86 64-bit pkg
2. Virtuelle Umgebung erzeugen und aktivieren
   ```
   conda create -n rasaenv python=3.9
   ```
   Bei der Frage, ob forgefahren werden soll, mit 'y'es bestätigen.
   ```
   conda activate rasaenv
   ```
3. Installiere Rasa
   ```
   pip install rasa
   ```
4. Initialisieren von Rasa
   ```
   rasa init
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
   https://docs.conda.io/en/latest/miniconda.html#macos-installers -> 	Miniconda3 macOS Apple M1 64-bit pkg
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
   conda env create -v --name rasaenv -f env.yml
   ```
7. Aktivieren des Virtuellen Environments:
   ```
   conda activate rasaenv
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

### Extra Schritt für Git Bash
Conda für bash initialisieren:
```
conda init bash
```
Wenn Powershell verwendet wird, dann die Powershell schließen und wieder öffnen. Das Prompt sollte etwa so aussehen
```(base) PS C:\Users\...>```

1. Virtuelle Umgebung erzeugen und aktivieren
```
conda create -n rasaenv python=3.9
```
Bei der Frage, ob forgefahren werden soll, mit 'y'es bestätigen.
```
conda activate rasaenv
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

# Responses/Utterances/Templates
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

# Deployment via Docker

## Actions Server Image erstellen:
1. Dockerfile erstellen:

```Dockerfile
# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:undefined

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
# RUN pip install -r requirements-actions.txt

# Copy actions folder to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1001
```

Das ```undefined``` des Image-tags muss ersetzt werden durch die gewünschte
Versionsnummer des Images. Weglassen für neuestes Image

2. Actions-Server Image bauen:
```
docker build . -t <account_username>/<repository_name>:<custom_image_tag>
```

```account_username``` und ```repository_name``` sind die Daten
des Images auf Dockerhub, falls es dort gehostet sind. Ansonsten
kann man sich etwas ausdenken. Ist aber dann nur lokal und andere
User müssen das Image erst selbst bauen. ```custom_image_tag```
enthält üblicherweise eine Versionsnummer des Images.


3. Lokal Starten:

```
docker-compose up
```

4. Requests an Rasa schicken (Postman empfiehlt sich: https://www.postman.com/downloads/)

Methode: POST
Header: ```application/json```

Payload:
```
{"sender": "test", "message": "hello"}
```

Wenn alles funktioniert, liefert Rasa ein JSON zurück.

Original Rasa-Docs zu diesem Thema: 
- https://rasa.com/docs/rasa/docker/deploying-in-docker-compose/
- https://rasa.com/docs/action-server/deploy-action-server/#manually-building-an-action-server

## Depolyment

TODO
