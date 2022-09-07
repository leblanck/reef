<p align="center"><img width=40% src="https://raw.githubusercontent.com/leblanck/reef/main/resources/reef.png"></p>

<div align="center">

<a href="">![GitHub issues](https://img.shields.io/github/issues-raw/leblanck/reef.svg)</a>
<a href="">![made-with-python](https://img.shields.io/badge/Made%20With-Python-yellow.svg)</a>
<a href="">![req-python-ver](https://img.shields.io/badge/python-v3.10-blue.svg)</a>

</div>

# REEF

## Digital Ocean System Status Bot for Discord

### Install in Discord
[Add Bot To Discord](https://discord.com/api/oauth2/authorize?client_id=1015266420034125844&permissions=3072&scope=bot)

### Install/Run Locally

1. `$ pip install -r requirements.txt`
2. Place Discord Application Developer Token into `discordtoken.py` 
3. Run `python3 bot.py`
4. If succesfull you will see the following output:

```bash
INFO     discord.client logging in using static token
INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: ).
Logged on as DigitalOcean Reef!
```

---

### Usage

#### Getting General System Status
Command: `$reef`

```
DigitalOcean Reef BOT — Today at 9:52 AM
✅ All Systems Operational 
Updated at 2022-09-07T08:13:41.180Z, Etc/UTC
```
This will report if there are any outages in the Digital Ocean environment.  This is more of a general check. 

#### Getting Scheduled Maintenance
Command: `$reef-m`

```
DigitalOcean Reef BOT — 09/02/2022
✅ No Maintenance is Scheduled. All good!
```
This will report if there are any *scheduled & upcoming* maintenance windows.

#### Getting Individual Component Status
Command: `$reef-c componentName` e.g. `$reef-c API`

```
DigitalOcean Reef BOT — Today at 2:02 PM
✅  API is in a operational state
Updated at 2022-07-14T23:18:26.904Z
```
This will report the current status of the supplied component (API, VPC, Billing, etc). Components can be found on the [Digital Ocean Status Page](https://status.digitalocean.com).