# Python Program: Seeker Game 🔍

## Description
Seeker is a game in which the player seeks to find the hider by guessing its location. The hider gives hints until it is found.

For further information please visit the following [link](https://byui-cse.github.io/cse210-course-competency/encapsulation/materials/seeker-specification.html)

### Python Version:
To run this script `python>3.5` is recommended

## Getting Started 🔥

- Download and extract the repository.
- Open a terminal and move to the with the cd command to the path where the folder was extract: $ cd "/path/to/project/folder"
- From within the repo directory run the command
  $ python main.py (for old versions of python3 run $ python3 main.py)

## Classes

### Class Hider
This class holds the location of the hidden item and the distance between , this location is a private which can not be accessed.
The only function this class has is two comparative functions to determine wether
### Class Player
Following the logic of the real game, every game has a "player" and this player is responsible of take decisions .
### Class Game
The game class manage the game from the moment the player starts playing it and keep control of it during it's development.

## How encapsulation was used?

An example of this is the class Hider, the location value is actually never used by any of the other classes, the functions were implemented in such a way
that the logic of the hidder class didn't required of changes when the class game was implemented in the last updating of the program.
