![Game UI](https://i.imgur.com/epJ3nGA.png)
# GobangGame-python
Based on the purpose of learning python, I developed this little game.


## TABLE OF CONTENTS
* **Usage**
* **Requirements**
* **Introduction**
  * **Technology**
  * **Game rules, cases & evaluation**
  * **Computer AI**
  
## Usage
 1. If the computer system is Windows, you can use the .exe file in the dist directory.
 2. For other, please run the main.py file directly


## Requirements

**Task 1.** To make a game environment, include as following
  * Game chess board (white and black chess, x-index, y-index)
  * Texi view for showing message of game
  * Button and onclick events such as start game and restart game
  
**Task 2.** To create a file named "game_logic.py" and write game logic on it

**Task 3.** To develop a computer AI as the opponent and use programs to calculate AI actions

## Introduction

### 1. Technology

  |   Tools |  Language  | Module  |
  |:-------:|:----------:|:-------:|
  | PyCharm |  python 3  | NumPy   |
  |         |            | Tkinter |
  
### 2. Game rules, case & evaluation

Computer AI needs to understand the game to a certain extent, so we need to collect some game cases and make the evaluation form. The quality of the evaluation form largely determines the intelligence of computer AI

* **Game rules**

  Game wins when 5 points or more are connected in a line (as following)
  
  ![game five](https://i.imgur.com/CF2IWVp.png)
  
* **Game cases & evaluation**

  First, we need to understand some simple game cases, as shown below
  
  ![game case](https://i.imgur.com/OL8Dkfr.png)
  
    ****If connected to the opponent, it is sleep type***
  
  Then we need to evaluate the above cases
  
  ![game evaluation](https://i.imgur.com/qbEoyMd.png)
  
### 3. Computer AI
