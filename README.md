# Gamemaker-RPC
A RPC for GameMaker in English / French (doesn't work in other languages)
----------------------

## Description

Gamemaker-RPC is a Python script that updates your **Discord Rich Presence** with the current project you're working on in **GameMaker**. It checks if **GameMaker** is running, then retrieves the name of the project you're working on and displays it in your Discord status.

---

## Requirements :

- **Python** (obviously)
- **PyPresence** => The RPC Client (to interact with Discord)
- **PSUtil** => To verify if **gamemaker.exe** is running
- **PyGetWindow** => To retrieve the title of the active window (to check what project is open)

---

## Installation
You need to install the required libraries by running the following command:

```bash
pip install psutil pypresence pygetwindow
```

Then you can modify the 'config.json' file and finally use 'launcher.pyw' as the launcher.