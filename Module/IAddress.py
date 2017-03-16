from Module import Config

prefix = ''
if Config.env == 'Internal':
    Login = 'https://neibulogin.kongfz.com/Interface/Sign/login'
if Config.env == 'External':
    Login = 'https://login.kongfz.com/Interface/Sign/login'
