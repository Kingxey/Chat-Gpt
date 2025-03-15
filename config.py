from os import environ
import re

id_pattern = re.compile(r'^.\d+$')

# bot
API_ID = int(environ.get('API_ID', '24817837'))
API_HASH = environ.get('API_HASH', 'acd9f0cc6beb08ce59383cf250052686')
BOT_TOKEN = environ.get('BOT_TOKEN', '7853679227:AAGMpocOTQmyqcUN4-phC0u97qNmQIzf5sc')
ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in environ.get('ADMINS', '1867106198').split()]

# bs
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002376378205'))
fsub_eid = environ.get('FSUB_ID')
FSUB_ID = int(fsub_eid) if fsub_eid and id_pattern.search(fsub_eid) else None

# database

DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://Aniflix:Lipun123@aniflix.q2wina5.mongodb.net/?retryWrites=true&w=majority&appName=Aniflix')
