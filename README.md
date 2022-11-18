# Low-Level-Design-Python

This repo contains Low level designs in Python 3.
Idea is to have a head start to the low level designing concepts and to write clean,readable code implementation of real world problems.  
Some modules here can be excecuted while some define the basic structures and the overall flow of the problems.

**Note** : This repo is still under development and any contribution is welcomed!

<br/>


## [Tic Tac Toe](TicTacToe.py)

Tic tac toe is a board game where players can choose their own entity to play with and try to win against their opponents with a set of given rules.  

Different new strategies can be implemented and be plugged in to the game for various set of rules for winning using Strategy Pattern.  
Some other requirements implemented:

- Mutiple Players can play
- Players able to win by any winning strategy
- There can be multiple winning strategies
- Entities can have types
- Board can be customised with given size
- Games have specific players and board.  


<br/>


## [Snake And Ladder Game](SnakeAndLadder.py)

Snake and ladder is a classic board game where players goes through a fight with opponent players to reach the last grid square first, starting from the same point.

The board will not only slow players down by attacking them with snakes but also help to reach faster by providing ladders in places. Only key is luck with dice.
Some of the requirements implemented:

- Mutiple Players can play
- Board can be customised with given size
- Customised number of snakes and ladders can be placed on the board
- Games have specific players and board



<br/>

## [Car Rental System](CarRentalService/CarRentalSystem.py)

This contains low level design implementation for a Car Rental Service with basic work flow and function definitions. It also contains the `main.py` module to indicate the work flow of the system.


Some of the requirements implemented:
- Different types of vehicles - cars, trucks, SUVs, vans, and motorcycles.
- Each vehicle have a barcode and SpotId where it is parked
- Two types of users considered: Admin and Members/Customer
- Member can search/reserve/return vehicles

