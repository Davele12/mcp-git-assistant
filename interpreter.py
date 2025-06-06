import requests

def prompt_llama(prompt):
    instrucciones = (
        "Eres un asistente local de desarrollo que puede ejecutar comandos Git. "
        "Tus capacidades actuales incluyen: "
        "1) Crear repositorios locales, "
        "2) Inicializarlos con Git, "
        "3) Crear repositorios remotos en GitHub, "
        "4) Conectarlos y hacer push, "
        "5) Hacer commits. "
        "No debes responder con instrucciones para usar curl o Postman, "
        "solo responde con la intención clara del usuario, en lenguaje natural simplificado, "
        "para que otro sistema pueda ejecutar esa acción."
        "\n\n"
        f"Usuario: {prompt}\nAsistente:"
    )

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": instrucciones,
        "stream": False
    })
    return response.json()["response"].strip()
