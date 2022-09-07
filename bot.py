import discord
import requests
import json
from discordtoken import discord_token

def get_status():
    response = requests.get('https://status.digitalocean.com/api/v2/status.json')
    json_data = json.loads(response.text)
    desc = json_data['status']['description']
    timeZ = json_data['page']['time_zone']
    timeU = json_data['page']['updated_at']
    indicator = json_data['status']['indicator']

    if indicator == 'minor':
        icon = ':grey_exclamation:'
    elif indicator == 'major':
        icon = ':warning:'
    elif indicator == 'critical':
        icon = ':sos:'
    else:
        icon = ':white_check_mark:'

    status = f'{icon} {desc} \n> Updated at {timeU}, {timeZ}'
    return status

def get_maintenance():
    response = requests.get('https://status.digitalocean.com/api/v2/scheduled-maintenances/upcoming.json')
    json_data = json.loads(response.text)
    schedule = json_data['scheduled_maintenances']
    icon = ':tools:'
    maintenance = f'{icon} Loading Scheduled Maintenance... \n {schedule}'

    if not 'scheduled_maintenance' in json_data or len(json_data['scheduled_maintenance']) == 0:
        icon =  ':white_check_mark:'
        maintenance = f'{icon} No Maintenance is Scheduled. All good!'
    else:
        maintenance = f'{icon} Loading Scheduled Maintenance... \n {schedule}'

    return maintenance

def get_component(component):
    response = requests.get('https://status.digitalocean.com/api/v2/components.json')
    json_data = json.loads(response.text)
    component = component[8:]
    #Print statments used for debugging. Either remove or comment out later.
    print('+'*10)
    print(f'Currently component is set to this on line 43: {component}')
    print('+'*10)
    print(type(json_data))

    for c in json_data['components']:
        if c['name'].lower() == component.lower():
            status = 'We Found it!'
            return status
            break
        else:
            status = f'{component} was not found. Please try a different component name...'
            return status

class ThisClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$reef-m'):
            await message.channel.send(get_maintenance())
        elif message.content.startswith('$reef-c'):
            data = message.content
            await message.channel.send(get_component(data))
        elif message.content.startswith('$reef'):
            await message.channel.send(get_status())


intents = discord.Intents.default()
intents.message_content = True

client = ThisClient(intents=intents)
client.run(discord_token) #DISCORD APP DEV TOKEN CALLED FROM token.py