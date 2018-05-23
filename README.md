# BotDeMerde
Basé sur solution décrite [ici](www.fullstackpython.com/blog/build-first-slack-bot-python.html)

Pour le faire tourner : 
1. Cloner le repo
`git clone https://github.com/GuillaumeCz/BotDeMerde.git`
2. S'y rendre
`cd BotDeMerde`
#### Optionnel -Debut
- Créer un [virtualenv](https://virtualenv.pypa.io/en/stable/). C'est plus pratique...
`virtualenv ENV`
- L'activer
`source ENV/bin/activate`
#### Optionnel -Fin
3. Installer les modules necessaires
`pip install -r requirements.txt`
4. Créer un bot sur Slack (comme [ici](www.fullstackpython.com/blog/build-first-slack-bot-python.html)) (partie "Slack APIs and App Configuration")
5. Exporter son Token d'authentification en variable d'environnement (On ne va pas quand même la publier sur Git ;P) 
`export SLACK_BOT_TOKEN='mon bot user access token ici'`
6. Le lancer
`python bot.py`

