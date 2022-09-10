Activate virtual environment:
	
	source .venv/bin/activate

#######################################
(for example in pizza-order-bot:)
Start Server with:
	
	rasa run -m models --enable-api --cors "*" --debug

#######################################

Action Server: 
Uncomment in endpoints.yml:
---
action_endpoint:
  url: "http://localhost:5055/webhook"
---

Start Action Server in parallel terminal:

	rasa run actions

#######################################

For rasa example messager (right-bottom chat icon in frontend): 

uncomment socketio in credentials.yml and name user & bot as follows:
socketio:
	user_message_evt: user_uttered
	bot_message_evt: bot_uttered
	session_perssistence: true/false

#######################################

Locale Rasa Server Adresse: 0.0.0.0:5005/webhooks/rest/webhook

#######################################

Navigate into /frontend for testing:
	firefox index.html

#######################################
