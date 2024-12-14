# blogs2RSS
Some of my favorite small blogs don't have RSS. I hate that fact. Let me simply fix that.

# Dependencies
* flask
* feedgen
* requests
* beautifulsoup4
* gunicorn

# Installation

* ` pip install -r requirements.txt`

# Running
1. `python3 updateFeed.py && python3 create_kasparek_feed.py`
1. Set cron file for feedcreation (could be hourly) to run command in 1st step periodically. Suggest `2>&1 | tee output.log` to store logs
2. `gunicorn wsgi:app -b 0.0.0.0:80 --reload --reload-extra-file kasparek-rss.xml --reload-extra-file kasparek-atom.xml` (the kasparek file gets updated last, so we don't need to reload flask every single time)
3. Visit localhost and grab the rss link
4. Voilá

## Honesty
In real world, you would need to host this app (something like ngrok or own domain/local domain). 

# Let me know about other cool blogs so I can add RSS to them!
