# Chatbot mit Rasa Intro.

## Setup


1. Virtual Environment erstellen und aktivieren
#### MacOS (funktioniert **nicht** auf Apple Silicon,  TODO: M1, M2 Mac)
```
python -m venv rasa-venv
source rasa-venv/bin/activate
```
#### Windows (Git Bash)
```
python3 -m venv rasa-venv
rasa-env\Scripts\activate.bat
```
#### Windows (CMD)
```
python3 -m venv rasa-venv
./rasa-env/Scripts/activate
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





