# Capstone Project : Unraveling the Team Composition Influence in TFT 


### Table of Contents:
- [Problem Statement](#Problem-Statement)
- [Game Description](#Game-Description)
    
- [Data Dictionary](#Data-Dictionary)

## Problem Statement

With the massive growth of e-sports and competitive online games, developers strive to come up with a revolutionary new genre that may shape the future of e-sports.  In 2019, a new type of online game, aka “auto-chess” has been on the rise and Riot Games has created a version of their own by the name of Team Fight Tactics with expectations of mobile releases in 2020.

Certain final team compositions and item builds may affect the outcome of a random match in a TFT.  Depending on what strategy an individual takes, a player can gain an advantage over other players slightly.  Using supervised models we will explore if there is a significant evidence that certain team composition and item choices yield better placements.

## Game Description

Teamfight Tactics is an alternative turn-based mode in a Multiplayer Online Battle Arena (MOBA) game, League of Legends by Riot Games.  Teamfight Tactics was created with the game foundation inspired by Dota Auto Chess (another alternative mode from a MOBA game) infused with champions from League of Legends.  A player is given a chance during his planning phase to purchase and/or place champions on a board with 8 rows and 7 columns of hexagons split horizontally for 2 players. 

Teamfight Tactics has 4 general phases that cycle.
1. **Carousel Phase:** At the start of a match, begins a carousel phase where 8 players (if later in the game, players remaining) simultaneously compete to choose the first champion from a rotating carousel of champions in the center of the board.  After the first carousel phase, all other carousel phases will have two players simultaneously choose champions at a time starting with the two weakest players. Then begins the planning phase.  


![Image description](./images/carousel_phase.png)


	
2. **Planning Phase:** Planning phase occurs between every other phase and players are rewarded gold coins which can be spent on purchasing level experience or champion units.  During this phase, every player is simultaneously given an access to the shop which shows a random pool of 5 champions to purchase from a global pool of champions shared by all players.  Note that tier level of the champion (higher tier means stronger base stats) available in the shop are based on player levels. (experience needed for the player to level up increases per level increased) After a player purchases a unit, it is stored in the player's inventory so the player can choose to place the unit on the board.  When the player does not enough units on the board equivalent to the player's level, player's units are automatically placed on the board starting with the first unit in the player's inventory.

3. **Player vs. Environment (PVE) Phase:** where the player's units automatically fight the neutral units on the board without the player having control of the units placed on their side of the board.  When the player kills the neutral unit, there is a random chance for the player to obtain a random number of items or gold coins based on the number of neutral units on the board killed.

4. Once again, planning phase will occur and players can make changes to their board during this phase to prepare for the PVP phase.  Player vs. player (PVP) phase is a clash between two random players.  All players start out the match with 100 health points where every neutral or enemy player's unit that survives fighting the player's team does damage until the player reaches 0 points.  A player's health point is a universal scoring system that will carry over throughout all phases and a ranking of the players is determined based on the health point remaining throughout the match.  After some combination of PVP and PVE phases, the carousel phase returns and the cycle repeats until only a single player is alive.  


### Champions & Set Effects

In Teamfight Tactics, all champions start as tier 1 but are automatically fused into tier 2 and 3 when the player obtains 3 copies of the identical units of the same tier.  Higher tier of units equate to higher base stats of the unit.  All units have 1 or 2 traits that are assigned to the units (static) which can give the entire team or the units with the same traits additional bonus effects that can benefit the team.  The bonus effect of the traits only activate when the specific units are placed on the board which is the reason for team compositions being so influential over a player's outcome of the match.  

### Items 

Each champion is allowed up to 3 items to equip.  There are 9 items that can combine with another item to create a total variation of 45 different combined items.  Items automatically combine once they are equipped to a single unit.    

## Executive Summary

In order to perform any modeling or analysis, first thing we need to do is to obtain the appropriate data, then clean the data so that information can be interpreted through modeling techniques offered by the python library.  


### Limitations 

-"un-robustness of API"
- Game is not simple enough
- Due to the depth of the game data available at the moment, further analysis based on player's data in between phases (turns) or analysis based on gold coin (income) trend are limited
- RIOT API only gives data based on final holdings of champions
- TFT is relatively new & RIOT API is still under development (they don't want ML to master 'botting')

### Initial Discovery (EDA)

- even though "shared pool" of champions but somehow majority of all players have similar team compositions 
- There is a trend "meta" most players try to mimic or follow (increasing collinearity between features from original data)


### Modeling 

We used multiclass classification with ensemble models to predict our outcome.
The models we used are Decision Trees, Random Forest, XGBoost, AdaBoost.

#### Model Optimization

GridSearchCV to look for optimal parameters which we were able to utilize to increase our accuracy score slightly.


## Conclusion

After we have optimized our model by tuning the hyper parameters of our models, we found that our XGBoost Model can predict the placement of a player at approximately 26% accuracy.  This at first seemed like a low value; however, when compared to our baseline score of 0.146, our XGBoost accuracy score of 0.261 is actually performing far better at predicting placement of a player when using champion units data.

Originally, we had believed that we would be able to determine whether we can predict the best team composition based on our model prediction then taking the important feature depicted by the model to determine whether it is a good indicator.  After actually executing the models, although we did better than the baseline, it still does not seem like there is a great predictor that specifically assists in becoming a winner.

## Recommendation

## Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|gold_left|object|game_df|Total number of gold coins a player had remaining when eliminated from the game| 
|last_round|float|game_df|Round number a player was on when eliminated from the game| 
|level|float|game_df|The player's level when eliminated from the game| 
|placement|float|game_df|Player's final placement (1st - 8th)|
|players_eliminated|float|game_df|Total number of match opponents a player eliminated throughout the course of the game before finally being eliminated from the game|
|time_eliminated|float|game_df|Total number of time elapsed (in seconds)|
|total_damage_to_players|float|game_df|Total number of damage inflicted to match opponents.|
|summonerName|object|game_df|Player's game ID|
|division_tier|object|game_df|Player's division name and tier.|


 ## Sources