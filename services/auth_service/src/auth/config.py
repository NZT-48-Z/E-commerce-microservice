from authx import AuthXConfig
import os

config = AuthXConfig()
config.JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
config.JWT_ACCESS_COOKIE_NAME = 'auth_access_token'
config.JWT_TOKEN_LOCATION = ['cookies']
