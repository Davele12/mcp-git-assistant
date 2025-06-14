from interpreter import prompt_llama
from command_mapper import map_to_action
from git_engine import execute_action
from config import get_Logger

def main():
    logger = get_Logger()
    texto_usuario = input("🧠 Dime qué quieres hacer con tu repo: ")
    respuesta_llama = prompt_llama(texto_usuario)
    logger.info(f"\n🤖 LLaMA respondió: {respuesta_llama}\n")
    
    accion, parametros = map_to_action(respuesta_llama)
    execute_action(accion, parametros)

if __name__ == "__main__":
    main()
