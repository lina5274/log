
import logging
import requests as rq
import logging.config
from log_settings import log_config

logging.config.dictConfig(log_config)
logger = logging.getLogger("success")
logger2 = logging.getLogger("bad")
logger3 = logging.getLogger("blocked")




sites = ['https://www.youtube.com/','https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            logger.info(f'\'{site}\', response - 200')
        else:
            logger2.warning(f'\'{site}\', response - {response.status_code}')
    except rq.exceptions.ConnectionError:
        logger3.error(f'\'{site}\', NO CONNECTION')
    except rq.exceptions.ReadTimeout:
        logger3.error(f'\'{site}\', READ TIMEOUT')



