import subprocess
import os

def execute_action(accion, params):
    if accion == "crear_repo":
        nombre = params["nombre"]
        os.makedirs(nombre, exist_ok=True)
        subprocess.run(["git", "init"], cwd=nombre)
        print(f"✅ Repositorio '{nombre}' creado")

        from github_api import crear_repo_remoto
        url_remoto = crear_repo_remoto(nombre)

        if url_remoto:
            subprocess.run(["git", "remote", "add", "origin", url_remoto], cwd=nombre)
            subprocess.run(["git", "branch", "-M", "main"], cwd=nombre)
            subprocess.run(["git", "add", "."], cwd=nombre)
            subprocess.run(["git", "commit", "-m", "primer commit"], cwd=nombre)
            subprocess.run(["git", "push", "-u", "origin", "main"], cwd=nombre)
            print("🚀 Subido al repositorio remoto")

    elif accion == "commit":
        mensaje = params["mensaje"]
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", mensaje], check=True)
        print(f"✅ Commit realizado: {mensaje}")

    elif accion == "push":
        subprocess.run(["git", "push"], check=True)
        print("✅ Cambios enviados al repositorio remoto")

    elif accion == "desconocido":
        print("⚠️ No entendí la acción que me pediste.")
