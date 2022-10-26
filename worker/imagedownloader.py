import gdown
from datetime import datetime

url = <string-of-drive-url-folder>

filename = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
gdown.download_folder(url, quiet=True, use_cookies=False) 
