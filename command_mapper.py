import re

def limpiar_nombre(texto):
    nombre = texto.split("llamado")[-1] if "llamado" in texto else texto
    nombre = nombre.strip().strip('"').strip('.')
    nombre = re.sub(r'[^\w\-]', '_', nombre)  # solo permite letras, números, guiones y guiones bajos
    return nombre

def map_to_action(respuesta_llama):
    respuesta = respuesta_llama.lower()

    if "nuevo repositorio" in respuesta or "crear repositorio" in respuesta:
        nombre = limpiar_nombre(respuesta)
        return "crear_repo", {"nombre": nombre}
    
    elif "commit" in respuesta:
        mensaje = respuesta.split("mensaje")[-1].strip() if "mensaje" in respuesta else "Actualización"
        return "commit", {"mensaje": mensaje}

    elif "push" in respuesta:
        return "push", {}

    else:
        return "desconocido", {}

