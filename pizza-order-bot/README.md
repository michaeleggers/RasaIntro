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