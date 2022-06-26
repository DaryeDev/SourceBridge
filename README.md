# SourceBridge

Little util to connect to your Source Game Developer Console to Python.

## Setup

Install `psutils` with pip: `pip install psutils`

Check out the example on `main.py`.

## How does it connect?

SourceBridge uses 2 methods to connect to your game: Hijack and NetCon

### Hijack

The Hijack method works with all tested games, but it is slower connecting to the game and sending the commands (Although not that noticeable).

#### Compatible Games

 - All (All tested, that is.)

#### Incompatible Games

 - None (None that were tested.)

### NetCon

The NetCon method is faster connecting to SourceBridge, and faster sending the commands; but it's only compatible with a few games, and the game must be launched with the launch argument `-netconport 2121`.

#### Compatible Games

- Portal 2
- Left for Dead 2
- Counter-Strike Global Offensive

#### Incompatible Games

- Team Fortress 2
- Portal (1)
- Half-Life 2
- Counter-Strike Source
- Garry's Mod


## Kudos

Kudos to PortalRunner for letting me know about the NetCon Method, and [@maxdup](https://github.com/maxdup) for [ValveEXE](https://github.com/pySourceSDK/ValveEXE), inspiration and base for the Hijack Method. 
