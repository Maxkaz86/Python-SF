import os
from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
non_valid_email = os.getenv('non_valid_email')
non_valid_password = os.getenv('non_valid_password')