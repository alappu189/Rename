import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "")

API_HASH = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5999105365:AAGHarGuzulh9f9HxX23PM4eTCgZIZAcwCQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "MLZ_BOTZ") 

DB_NAME = os.environ.get("DB_NAME","sui:sui")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://sui:sui@cluster0.fmobrpu.mongodb.net/?retryWrites=true&w=majority")

FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1833209093 5845960615 5596825598').split()]

PORT = os.environ.get('PORT', '8080')
