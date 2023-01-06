# Rules

**WORK IN PROGRESS**

The rules of the game are enumerated below:

1. Overview
2. Algorithms
3. Gameplay
   1. Turn
   2. Combat
4. Winning
5. Advanced Topics
   1. Multi-Faction Games
   2. Throwing away **The Rules**

## Terms

FC - Faction controller -> the player or algo controlling the faction
cell - one unit of area in the map, owned by a faction and can contain a unit

## 1. Overview

This game consists of several factions, rendered as separate colors in the terminal, fighting to be the last ones standing. After game start, the game progresses through turn after turn until only one faction remains. During each turn, the current map is given to each FC, who/which returns a map of the desired moves to be made. The outcomes of each turn occur all at once, rather than one after another, requiring FCs to consider both their own moves as well as the moves of other FCs. In addition to other competing factions (marked in color on the map), there also exist two other cell owners: the Factionless, and Impassable Terrain.

The Factionless are groups of villages that do not belong to a larger Faction. They are not counted for victory conditions, as they possess no capital. No points are awarded for beating the villages of the Factionless, but FCs that defeat a village are rewarded in-game with a village that they may place anywhere within their Faction. This can be used to create challenges for FCs in early game or help set up larger and more powerful Factions.

Impassable Terrain is exactly as the name implies. Factions are incapable of claiming these cells, and any units sent to them will be destroyed with no effect on the cell. As they can only be rendered as white cells, it is up to viewers exactly what the terrain is. High peaks? Dense Forests? Small Oceans? Up to you. Whatever makes you happy.

## 2. Algorithms

The game is played by Faction Controllers (FC)s. These are humans or algorithms controlling the factions. At the moment, effort is mostly being put into making the game usable, and so algorithms are being given preference, as it's easier. If you feel like making an interface for a human controller though, feel free to beat us to it and make a commit.

## 3. Gameplay

### 3.1 Turn

### 3.2 Combat

## 4. Winning

## 5. Advanced Topics

### 5.1 Multi-Faction Games

### 5.2 Throwing away The Rules

Everything laid out here? Just the vanilla rule-set. Want to change how the Factionless take their turns? Replace their algorithm with one of your choice. Want to simulate a forest fire in the Impassable Terrain? Wait, that'd be rad. I just made it for you, check it out. But if I hadn't, add a file in the on_update folder and specify it in game setup. Beyond that: think a unit is OP? It's all Python... Change its stats in the Units file!

Any Suggestions? Feel free to make an Issue on the GitHub Page.
