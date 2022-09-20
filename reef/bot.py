import discord
import requests
import json
from reef.discordtoken import discord_token

def get_status():
    response = requests.get('https://status.digitalocean.com/api/v2/status.json')
    json_data = json.loads(response.text)
    desc = json_data['status']['description']
    timeZ = json_data['page']['time_zone']
    timeU = json_data['page']['updated_at']
    indicator = json_data['status']['indicator']
    helper = 'Run `$reef-i` for more info on current incidents.'

    if indicator == 'minor':
        icon = ':grey_exclamation:'
    elif indicator == 'major':
        icon = ':warning:'
    elif indicator == 'critical':
        icon = ':sos:'
    else:
        icon = ':white_check_mark:'
        helper = ''

    status = f'{icon} {desc} {helper}\n> *Updated at: {timeU}, {timeZ}*'
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

def get_incident():
    response = requests.get('https://status.digitalocean.com/api/v2/incidents/unresolved.json')
    json_data = json.loads(response.text)
    status = 'No Incidents were found! Nice!'

    for i in json_data['incidents']:
        if i['name'] != '':
            inc_name = i['name']
            inc_state = i['status']
            inc_time = i['updated_at']
            inc_desc = i['incident_updates']
            status = f'**Current Outage:** {inc_name} with status of: {inc_state.upper()}...\n> *Updated at: {inc_time}* '

    return status

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
        print(c)
        if c['name'].upper() == component.upper():
            updated_c = c['updated_at']
            indicator_c = c['status']
            if indicator_c == 'degraded_performance':
                icon_c = ':grey_exclamation:'
            elif indicator_c == 'partial_outage':
                icon_c = ':warning:'
            elif indicator_c == 'major_outage':
                icon_c = ':sos:'
            else:
                icon_c = ':white_check_mark:'

            status = f'{icon_c} {component.upper()} is in a **{indicator_c}** state\n> *Updated at: {updated_c}*'

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
        elif message.content.startswith('$reef-i'):
            await message.channel.send(get_incident())
        elif message.content.startswith('$reef-c'):
            data = message.content
            await message.channel.send(get_component(data))
        elif message.content.startswith('$reef'):
            await message.channel.send(get_status())


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    client = ThisClient(intents=intents)
    client.run(discord_token) #DISCORD APP DEV TOKEN CALLED FROM discordtoken.py