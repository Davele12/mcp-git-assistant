import logging, pathlib

class Project_Logger:
    """
    Inicializa un objeto tipo `(logger)` que escucha los Eventos desde el Nivel de Gravedad `logger.DEBUG`,

    Tambien establece dos objetos `(logger)` del tipo `Handler`:
    1. **ConsoleLogger:**
        - Se encarga de Loggear en la Consola los logs del Nivel de Gravedad `logger.DEBUG` o Mayor.
    2. **FileLogger:**
        - Se encarga de Loggear en el Archivo `Logs.log` todos los logs desde el Nivel de Gravedad `logger.INFO` hacia arriba.

    El Formato en el que Genera los Logs es `Mes-Dia Hora:Minuto AM/PM - Logger.root.name - Type: [Logger.levelname] - Text: Log.text`

    **Metodos:**
        **get_logger():**
            **Parametros/Argumentos:**
                `None`
            **Devuelve/Retorna:**
                `(object logging.Logger)`
    """

    def __init__(self, LOGS_DIR: pathlib.Path) -> logging.Logger:
        # Inicializando un Logger
        self.logger = logging.getLogger(__name__)

        # En caso de querer cambiar como muetra el logger los mensajes Toca cambiar el formatter
        # fmt --> El formato del Mensaje
        # datefmt -->  El formato en el cual la misma Libreria va a manejar las fechas y Horas
        self.formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - [%(levelname)s] - %(message)s', datefmt='%m-%d %I:%M %p')

        # Estableciendo el Nivel minimo de Escucha de el logger
        self.logger.setLevel(level=logging.DEBUG)

        # En caso de que no exista La carpeta "Logs" creala
        # parents=True -- Si dentro de el directorio padre ("\mcp-git-assistant") no existe "\Logs" lo crea
        # exist_ok=True -- Si ya existe, Evita la exepcion FileExistsError
        # Es lo mismo que hacer if not self.LogPath.exist():
        self.LogPath.mkdir(parents=True, exist_ok=True)

        # Creando el (Logger Handler) para mostrar mensajes
        # Con nivel de Gravedad Mayor o Igual a DEBUG,
        # Estos **SE MOSTRARAN EN CONSOLA PERO NO SE GUARDARAN EN EL Logs.log**.
        ConsoleLogger = logging.StreamHandler()
        ConsoleLogger.setLevel(logging.DEBUG)
        ConsoleLogger.setFormatter(self.formatter)

        # Creando el (Logger Handler) para Guardar los Mensajes (Logs)
        # Con nivel de Gravedad Mayor o Igual a INFO,
        # Estos Mensajes **SE MOSTRARAN EN CONSOLA Y SE GUARDARAN EN Logs.log**
        FileLogger = logging.FileHandler(filename=LOGS_DIR / "Logs.log")
        FileLogger.setLevel(logging.INFO)
        FileLogger.setFormatter(self.formatter)

        # Instanciando los objetos Handler al Objeto Logger
        # Esto en Caso de que no se halla hecho ya
        if not self.logger.handlers:
            self.logger.addHandler(hdlr=ConsoleLogger)
            self.logger.addHandler(hdlr=FileLogger)

        self.logger.info("Se inicializao el Logger!")

        return self.logger

    def get_Logger(self) -> logging.Logger:
        """
        Devuelve el objeto `(object logging.Logger)`, 
        ya instanciado de la calase `(class logging.Logger)`

        **Parametros:**
            `None`
        
        **Retorna:**
            `(object logging.Logger)`
        """
        return self.logger