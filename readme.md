# UPDATER

A stupid (far-too-heavy-to-be-sensible) way to check whether a specific website has been changed on the hour. [Currently, it is looking at the DC Circuit's daily opinion page]. 

It's stupidly simple to install: `git clone https://github.com/vzvenyach/updater.git && cd updater && ./setup.sh`, and it will start running. It'll even add a crontab entry for you. You'll need to have a [pushover](https://pushover.net/) account and an application token set up (again, way-too-heavy).