# Weather

Constructs a plain-language summary of the day’s weather, eg:

> Slightly colder than yesterday. Light rain in the afternoon.

Or:

> Same temperature as yesterday. Heavy rain between 4pm and 5pm. Windy.

Using XML data from yr.no, eg:

http://www.yr.no/place/United_Kingdom/England/Liverpool/forecast_hour_by_hour.xml

Maybe at some point it might also do something with the yr.no meteogram image:

http://www.yr.no/place/United_Kingdom/England/Liverpool/meteogram.png


## Installation

1. Requires Python and virtualenv.
2. Create and activate a virtualenv. I call mine `weather` and I use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/) and [this clever script](https://gist.github.com/clneagu/7990272) to make entering the virtualenv as simple as `cd`-ing into the right directory.
3. `pip install -r requirements.txt`

If you set the script to run via a Cron command, remember that Cron will need to activate the virtualenv too.

The script uses `requests` to pull in XML data from yr.no, and `requests-cache` to ensure yr.no is only called once every 10 minutes, in line with their terms of use.
