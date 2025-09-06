import random

from oracle_data import (spirit_animals, superpowers, hidden_destinations,
                         colors_aura, secret_messages, power_stones, pre_reveal_phrases, emojis)
import time
import sys

again = False
while not again:
    welcome = r"""
    ╔══════════════════════════╗
    ║  🔮 ORÁCULO CON EL PYTHONCITO 🐍  ║
    ╚══════════════════════════╝
    """

    print(welcome)
    print("🔮 Bienvenido al Oráculo en Python 🐍.\nTu destino está a punto de ser revelado...")
    # ---------------------------------------------------------------------------------------------------Name
    name = input("\nDime tu nombre: ").upper()
    print("\nConsultando a los astros ", end="")

    for i in range(5):
        print("🔮", end="")
        sys.stdout.flush()
        time.sleep(0.5)

    random_phrase = random.choice(pre_reveal_phrases)
    index_phrase = pre_reveal_phrases.index(random_phrase)

    print(f"\n{random_phrase}", end="")
    for i in range(5):
        print(f"{emojis[index_phrase]}", end="")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")
    # --------------------------------------------------------------------------------------------------- Index
    index_spirit_animal = random.randint(0, 26)
    index_superpower = random.randint(0, 26)
    index_hidden_dest = random.randint(0, 26)
    index_color_aura = random.randint(0,26)
    index_power_stone = random.randint(0,26)
    index_secret_message = random.randint(0,26)

    #-------------------------------------------------------------------------------------------------------Final
    final_message = f"✨✨✨ Los astros han revelado tu destino {name} ✨✨✨"
    print(final_message + "\n")
    time.sleep(1)

    print(f"✨ Animal espiritual: {spirit_animals[index_spirit_animal]}")
    print(f"⚡ Poder oculto: {superpowers[index_superpower]}")
    print(f"🔮 Destino: {hidden_destinations[index_hidden_dest - 1]}")
    print(f"🌈 Color de aura: {colors_aura[index_color_aura]}")
    print(f"💎 Piedra de poder: {power_stones[index_power_stone]}")
    print(f"📝 Mensaje secreto: {secret_messages[index_secret_message]}")

    # ----------------------------------------------------------------------------------------------------
    replay = input("\n🎲 ¿Te gustaría jugar de nuevo? (s/n): ").lower()

    if replay == "s":
        print("\n"*300)
    else:
        print("\n✨ Gracias por consultar al Oráculo con el Pythoncito 🔮🐍. ¡Hasta la próxima! ✨")
        again = True
