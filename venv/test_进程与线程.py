import logging
from time import sleep,ctime
logging.basicConfig(level=logging.INFO)
def loop0():
    logging.info("staart loop0 at "+ ctime())
    sleep(4)
    logging.info("end loop0 at " + ctime)
