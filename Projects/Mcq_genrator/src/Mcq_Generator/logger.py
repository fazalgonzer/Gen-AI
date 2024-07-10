import logging 
import os 
from datetime import datetime

Log_File=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
Log_path=os.path.join(os.getcwd(),"logs")
os.makedirs(Log_path,exist_ok=True)
Log_FilePath=os.path.join(Log_path,Log_File)

logging.basicConfig(level=logging.INFO,
                    filename=Log_FilePath,
                    format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]")
