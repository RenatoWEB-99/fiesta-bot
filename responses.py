import math
import random

def handle_response(message) -> str
    p_message = message.lower()

    if p_message == "oi"
        return "opa"

    if p_message == ":roll"
        return str(random.radiant(1, 6))

    if p_message == ":help"
        return "`Você acabou de usar o comando :help. Parece que você precisa de ajuda!\nMeu prefixo padrão é ':'.\n:roll - Rola um número aleatório entre 1 e 6.\n`"
