# This example uses an alternative frontend:
This branch uses the frontend from: https://github.com/JiteshGaikwad/Chatbot-Widget
as it is capable of displaying and playing embedded videos. See the ```utter_annoy_user_with_ad```
Utterance in ```domain.yml```.

To use it copy the ```static``` folder from this repo into your own project folder.
Also copy ```index.html``` (and overwrite the existing one, if presesnt).
Then, start rasa (and optionally rasa actions).

Some links to other frontends in this Rasa Forum Thread: https://forum.rasa.com/t/rasa-3-chatbot-integration-with-website/50193/2

The example works like the mvg-bot but will ussue another action that displays
an embedded YouTube video inside the chat window.

Additionally, the user is being greeted upon opening the chatwindow.

