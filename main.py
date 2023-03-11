from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
from pathlib import Path


# evn path and variables
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

ENV_VARIABLE=os.getenv('ENV_VARIABLE')

print(ENV_VARIABLE)