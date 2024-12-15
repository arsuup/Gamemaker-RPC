from pypresence import Presence
import pygetwindow as gw
import configparser
import subprocess
import psutil
import time
import sys
import os


script_directory = os.path.dirname(os.path.abspath(__file__))
repertorytxt = script_directory + '\\repertory.txt'
file_path = repertorytxt

with open(file_path, 'r', encoding='utf-8') as file:
    repertory1 = file.read()

repertory = repertory1.replace("\\", "\\\\")
client_id = '1317817618601738340'
game_maker_process_name = 'gamemaker.exe'
large_image2 = 'gamemaker_logo_1_0'
large_text2 = 'Gamemaker Studio'
project = 'launching...'

rpc = Presence(client_id)
rpc.connect()

def is_game_maker_running():
    for proc in psutil.process_iter(['pid', 'name']):
        if game_maker_process_name.lower() in proc.info['name'].lower():
            return True
    return False

if not is_game_maker_running():
    subprocess.Popen(repertory)

rpc.update(
    details=f"{project}",
    start=time.time(),
    large_image=large_image2,
    large_text=large_text2
)
print("Rich Presence active !")

last_project = project

while True:
    if not is_game_maker_running():
        print("GameMaker closed.")
        rpc.close()
        sys.exit(0)
    
    time.sleep(5)

    if is_game_maker_running():
        windows = gw.getWindowsWithTitle('')

        for window in windows:
            if " - GameMaker" in window.title:
                if "démarrage" in window.title or "Start" in window.title:
                    if " - GameMaker*" in window.title:
                        project = window.title.removesuffix(" - GameMaker*")
                    else:
                        project = window.title.removesuffix(" - GameMaker")
                else:
                    if " - GameMaker*" in window.title:
                        project = "Projet : " + window.title.removesuffix(" - GameMaker*")
                    else:
                        project = "Projet : " + window.title.removesuffix(" - GameMaker")
        
        # Mettre à jour le Rich Presence si le projet a changé
        if project != last_project:
            print(f"Projet en cours : {project}")
            rpc.update(
                details=f"{project}",
                start=time.time(),
                large_image=large_image2,
                large_text=large_text2
            )
            print("Rich Presence Updaté !")
            last_project = project

    time.sleep(5)  # Vérifie toutes les 5 secondes