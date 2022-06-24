# SourceBridge
Little util to connect to your Source Game Developer Console from Python. 

## Setup
Download this repo and import sourceBridge, then call `sourceBridge.run(command)`, being `command` the command to execute on your Source Game Developer Console. 

Easy to use.

### NetCon
Gamewise, some games can be launched with the launch argument `-netconport 2121`. 

Adding it to your launch arguments will make connecting to the Game and sending commands much faster.

#### Games known to be working with NetCon
 - Portal 2
 - Left for Dead 2
 
#### Games known to not be working with NetCon
 - Team Fortress 2
 - Garry's Mod
