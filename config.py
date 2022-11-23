import os
import ProxyCloud

BOT_TOKEN = '5752454871:AAEcgcmVRwUw6vTdwotvhRzuEsFd3MU9Qcs' #Aqui va el token del bot
API_ID =  14169350 #Tu api id de telegram
API_HASH = 'c0a4d9a7e42a2bf949e227bfbf59f8cf' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','lil_l4chy').split(';')

static_proxy = 'socks5h://KKGGJFYDJFLJFJYFDHGIYIJKKDFHRJEKLDDILG' #agrega si kieres tener un proxy statico Con @raydel0307 si kieres comprar un proxy
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['lil_l4chy'] = 0
