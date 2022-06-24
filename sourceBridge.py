import telnetlib
import os
import subprocess
import time
import psutil

class SourceBridge():

    tn = gameExe = gameDir = gameName = modDir = None
    isConnected = False

    def connect(self):
        if self.tn == None:
            print("Trying to connect to game...")
            try:
                self.tn = telnetlib.Telnet("127.0.0.1", "2121")
                self.isConnected = True
                print("Connected to compatible Source game! (NetCon)")
                return True
            except:
                self.tn = False
                try:
                    gameExecs = ["hl2.exe", "csgo.exe", "portal2.exe"]
                    modDirs = {"GarrysMod": "garrysmod", "Team Fortress 2": "tf2", "Portal 2": "portal2", "Portal": "portal", "Counter-Strike Source": "cstrike", "Counter-Strike Global Offensive": "csgo", "Half-Life 2": "hl2"}
                    for p in psutil.process_iter():
                        if p.name() in gameExecs:
                            self.gameExe = p.exe()
                            self.gameDir = os.path.dirname(self.gameExe)
                            self.gameName = os.path.basename(self.gameDir)
                            self.modDir = os.path.join(self.gameDir, modDirs[self.gameName])
                            self.isConnected = True
                            print("Connected to "+self.gameName+"! (Hijack)")
                            return True
                except:
                    pass
                if not self.isConnected:
                    print("Could not connect to compatible Source Game :(")
                    return False
        else:
            return self.isConnected

    def run(self, command):
        if self.tn == None:
            self.connect()
        if self.isConnected:
            if self.tn:
                self.tn.write((str(command) + "\n").encode('utf-8'))
            else:
                launch_params = [self.gameExe, '-hijack', '+', command]
                process = subprocess.Popen(
                    launch_params,
                    creationflags=subprocess.DETACHED_PROCESS |
                    subprocess.CREATE_NEW_PROCESS_GROUP)
                time.sleep(1)
            
            return True
        else:
            raise Exception("Compatible Source Game not Connected.")
        
    def __init__(self) -> None:
        self.connect()