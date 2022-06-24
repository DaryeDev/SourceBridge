# SourceBridge

Little util to connect to your Source Game Developer Console to Python.

## Setup

Install `psutils` with pip: `pip install psutils`

Check out the example on `main.py`.

### NetCon

Gamewise, some games can be launched with the launch argument `-netconport 2121`.

Adding it to your launch arguments will make connecting to the Game and sending commands much faster.

#### Games known to be working with NetCon

- Portal 2
- Left for Dead 2
- Counter-Strike Global Offensive

#### Games known to not be working with NetCon

- Team Fortress 2
- Portal (1)
- Half-Life 2
- Counter-Strike Source
- Garry's Mod

## Kudos

Kudos to PortalRunner for letting me know about the NetCon Method, and [@maxdup](https://github.com/maxdup) for [ValveEXE](https://github.com/pySourceSDK/ValveEXE), inspiration and base for the Hijack Method. 
