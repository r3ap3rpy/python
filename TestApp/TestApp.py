import os
import logging

from logging.handlers import RotatingFileHandler

CWD = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])
Logs = os.path.sep.join([CWD, 'Logs'])
Config = os.path.sep.join([CWD, 'Config'])
LogFile = os.path.sep.join([Logs,'App.log'])

logging.basicConfig(format = "%(asctime)s %(levelname)s :: %(message)s", level=logging.DEBUG)
logger = logging.getLogger("TestApp")
handler = RotatingFileHandler(LogFile, maxBytes=1000000, backupCount=100, encoding='utf-8', delay=0)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

for folder in [Logs, Config]:
    if os.path.isdir(folder):
        logger.info(f"Folder is good: {folder}")
    else:
        logger.critical("Missing folder, aborting execution!")
        raise SystemExit

