import os
import ProxyCloud

BOT_TOKEN = '5361466307:AAEK0I-MkftidkXU8fmVHu1OKO0MeATkrSs' #Aqui va el token del bot
API_ID =  16643256 #Tu api id de telegram
API_HASH = '000d66c8f9c490c81dd64d7a48f55d1d' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','nuevoss01').split(';')

static_proxy = 'socks5://KDDKKGYJJIJFGFYIJFGJGGYFJEJIKKRGDJLKDFLH' #agrega si kieres tener un proxy statico Con @raydel0307 si kieres comprar un proxy
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['nuevoss01'] = 0
