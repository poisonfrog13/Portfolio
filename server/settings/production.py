from server.settings.base import *
from os import getenv


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [getenv("ALLOWED_HOSTS")]


print("Running Django with production settings")
print(f"this is a secret a key {SECRET_KEY}\nand this is your HOST {ALLOWED_HOSTS}")
