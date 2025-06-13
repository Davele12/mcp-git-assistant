from dotenv import load_dotenv
from pathlib import Path
from logging import Logger
from Logger import Project_Logger

# Usando pathlib.Path(__file__) Le digo a pathlib 
# que obtenga la Ruta (Path) Absoluta de el archvio de python ejecutado (Main)
# Y luego con .parent me devuelvo a la carpeta Padre (mcp-git-assistant) en mi caso # Sebaxsus
BASE_DIR = Path(__file__).absolute().parent

# Aqui estoy uniendo la Ruta Base (Path) con la ruta "\Logs" que es la carpeta de los Logs
# Para mas info sobre pathlib --> https://docs.python.org/3/library/pathlib.html#basic-use
LOGS_DIR = BASE_DIR / "Logs"

LOGGER = Project_Logger(LOGS_DIR)

def get_Logger() -> Logger:
        """
        Devuelve el objeto `(object logging.Logger)`, 
        ya instanciado de la calase `(class logging.Logger)`

        **Parametros:**
            `None`
        
        **Retorna:**
            `(object logging.Logger)`
        """
        return LOGGER

# def load_env():
#     load_dotenv()
