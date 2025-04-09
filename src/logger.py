import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE) #giveing a path for the log file
os.makedirs(logs_path,exist_ok=True) #if the directory is not present it will create a new directory

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) #this will give us the path of the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d:%(name)s:%(levelname)s:%(message)s",
    level= logging.INFO
    )

if __name__ == "__main__":
    logging.info("Logging has started")
    logging.info("Logging has ended")