# Starten der Demo

Aktivieren der virtuellen Umgebung und darauf:


1. Rasa actions server starten
```
rasa run actions
```

2. Rasa trainieren und starten
```
rasa train
rasa shell
```

bzw. um den Bot zu debuggen und einen GraphViz dot output live zu erhalten:
```
rasa interactive
```

# TODOs:
- [ ] Mehrere Stories nötig

# Fragen

- Wie triggert das **simple_pizza_form** die korrekte Action in actions.py? Es scheint,
  dass allein die korrekte Benamung ausreicht, bin mir aber nicht sicher.

- Wann müssen paths in stories.yml und wann in rules.yml?

# Hinweise

## Utterances

Durch die Richtige Benamung der Utterances ist es oft nicht nötig
explizit eine Story anzulegen. Beispiel:
Die Nutzerin bzw. der Nutzer sagt, sie/er möchte eine Pizza bestellen, wodurch das
```simple_pizza_form``` gestartet wird. In der Story tauchen aber
die Fragen des Bots ```utter_ask_pizza_size``` und ```utter_ask_pizza_type``` nicht
explizit auf. Durch die Naming convention ```utter_ask``` + dem key des Slots
triggert das Form die utterance ```utter_ask_pizza_size``` automatisch. Besser gesagt kann Rasa zur Trainingszeit diese
utterance nutzen. 


# Quelle:

- https://youtu.be/YYh1ECnlw9o