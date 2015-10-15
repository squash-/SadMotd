# SadMotd
Add a MOTD to your server inspired by http://twitter.com/SadServer

Note: This only works for CentOS and any other linux distribution that uses /etc/motd for it's SSH motd.
I will try and update it in the future for other distributions such as ubuntu, etc. as I have time.

## Configuration

You will need to edit sadmotd.py to include the API keys needed to fetch the
SadServer tweets.

Inside sadmotd.py you'll find 4 variables:

```
c_key = '<replace with consumer key>'
c_secret = '<replace with consumer secret>'
axx_token = '<replace with access token key>'
axx_secret = '<replace with access token secret>'
```

A little background:

* `c_key` is the consumer key you get when you create an app with [Twitter}(http://developer.twitter.com/), once you've done that you can get your consumer key.
* `c_secret` you can get the same way you can get the consumer key.
* `axx_token` is the access token key you generate from your new twitter app.
* `axx_secret` you can get this the same way as the access token key

## Running

You can run this python script by simply running:

```
sudo ./sadmotd.py
```

or

```
sudo python sadmotd.py
```

## Requirements

Uses the following Python libraries (and their dependencies):

* [python-twitter](https://github.com/bear/python-twitter)

`python-twitter` can easily be installed with pip by running:
```
pip install python-twitter
```

Notes:

If you run into python throwing an InsecurePlatformWarning just run:
```
pip install requests[security]
```
