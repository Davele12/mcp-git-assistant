import subprocess
import os
from config import get_Logger

logger = get_Logger()

def execute_action(accion, params):
    if accion == "crear_repo":
        nombre = params["nombre"]
        os.makedirs(nombre, exist_ok=True)
        subprocess.run(["git", "init"], cwd=nombre)
        # En caso de no querer este Mensaje en el Archvio de Logs cambiarlo a `.debug()`
        logger.info(f"✅ Repositorio '{nombre}' creado")

        from github_api import crear_repo_remoto
        url_remoto = crear_repo_remoto(nombre)

        if url_remoto:
            subprocess.run(["git", "remote", "add", "origin", url_remoto], cwd=nombre)
            subprocess.run(["git", "branch", "-M", "main"], cwd=nombre)
            subprocess.run(["git", "add", "."], cwd=nombre)
            subprocess.run(["git", "commit", "-m", "primer commit"], cwd=nombre)
            subprocess.run(["git", "push", "-u", "origin", "main"], cwd=nombre)
            logger.info("🚀 Subido al repositorio remoto")

    elif accion == "commit":
        mensaje = params["mensaje"]
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", mensaje], check=True)
        logger.info(f"✅ Commit realizado: {mensaje}")

    elif accion == "push":
        subprocess.run(["git", "push"], check=True)
        logger.info("✅ Cambios enviados al repositorio remoto")

    elif accion == "desconocido":
        logger.info("⚠️ No entendí la acción que me pediste.")
