import telnetlib
import os
import subprocess
import time
import psutil


print("Trying to connect to game...")
try:
    tn = telnetlib.Telnet("127.0.0.1", "2121")
    print("Connected to compatible Source game! (Netconport)")
except:
    tn = False
    compatibleGameRunning = False
    try:
        gameExecs = ["hl2.exe", "csgo.exe", "portal2.exe"]
        modDirs = {"GarrysMod": "garrysmod", "Team Fortress 2": "tf2"}
        for p in psutil.process_iter():
            if p.name() in gameExecs:
                gameExe = p.exe()
                gameDir = os.path.dirname(gameExe)
                gameName = os.path.basename(gameDir)
                modDir = os.path.join(gameDir, modDirs[gameName])
                compatibleGameRunning = True
                print("Connected to "+gameName+"! (Hijack)")
                break
    except:
        pass

def run(command):
    if tn:
        tn.write((str(command) + "\n").encode('utf-8'))
    else:
        launch_params = [gameExe, '-hijack', '+', command]
        process = subprocess.Popen(
            launch_params,
            creationflags=subprocess.DETACHED_PROCESS |
            subprocess.CREATE_NEW_PROCESS_GROUP)
        time.sleep(1)