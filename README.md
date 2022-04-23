# KOF-implementation-based-on-FPGA
This project implements the classical video game Streetfighter on an FPGA board and SystemVerilog Language. Our design includes NIOS II SoC for interfacing with a USB Keyboard as the game controller to manage the keyboard input. The main game logic is supported by FSMs. The animation is done through a sequence of sprites controlled by an animation FSM. The background, sprites and music are stored in SRAM as buffers.

## Partner
Yao Wentao - ZJU-UIUC Institution
The same work at https://github.com/yaowentao001/ece385code.git

## Introduction 
  This is the final project based on a protocol to interface a keyboard and a monitor with the DE2 board using the on-board USE and VGA port. We implemented the classical video game Street fighter on the monitor. We use the input of a USB keyboard to control the behavior of the characters. By pressing A, S, D, W, the first character can move left, defend, move right and attack; the same functionality is to press left, down, right, up for the second character. The characters can push each other and there are hps to record the score of each player-. Additionally, we add the background music.
## Written Description of Final Project
### Written description of Final Project 
In our project, we implement a Street fighter game simplified from the classical video game Street Fighter from CAPCOM. The game of our design will have two players, each can choose and control a character. The two players will fight with each other by using their attacking skills or defend the attack from the other. The attack will cause damage to the other player but can be defended. Each player will have the same HP (health points) at the beginning, the winner is the player who first “kill” the other player by decreasing the HP to 0.

The features of our projects are the following things. For each character, we design seven animations for the stand, move left, move right, attack, defend, hurt response and die. The animations are done through a sequence of sprites controlled by an animation FSM. The sprites will be stored in OCM as image buffer. In addition, we also have background music stored in OCM and played by the self-written audio driver. 

The hardware bases include NIOS II SoC for interfacing with USB Keyboard as the game controller to manage the keyboard input. we connect both USB keyboard and VGA monitor to our DE-2 board. We write several modules and functions to handle the IO interface between USB driver and the FPGA. We use the HPI connect the FPGA to EZ-OTG chip. A tri-state buffer is set here for both receiving data and writing data in the USB. For the VGA connection, we use a VGA controller to connect with the top-level. Additionally, a 25MHz VGA clock is also set up to control the VGA module.

For the demo of our project, we will illustrate how the two players fight with each other, how to attack, defend. Basically, we will show one round of the game. Plus, some additional features will also be shown in the demo.

### Description of Game Procedure
This is a multi-player game with two players, each control a different game character to fight with each other. Generally, we have three game scenes. The start screen, Game scene and “KO” scene. 

a)	Start screen

In this game scene, we have a background image with the title on the game. When the users press “space” on the keyboard, the game will start and transit to the game scene. And whenever the user press the “reset” button on the DE2 board, the game will reset all state to the default state and back to this screen. 

![image](https://github.com/HiracharleFranklin/KOF-implementation-based-on-FPGA/blob/082c9cd97252ab0201cdd705a5f206c85d2b4e79/image/image1.jpg) 

b)	Game scene

This is the main scene of our game. Two players can control their characters on the right and left side to fight with each other.

The UI of our game is the HP bar on the top of our game screen. Here, we have the image of both the game characters with their HP separately shown here. With the attack from the other player and get hurt, the HP bar will get decreased just like the read street fighter game. 

The main scene of the game has two components. The game players and the background images. Each players have four different actions: moving forward, moving backward, defense and attack. With pressing on the buttons on the keyboard, the characters can move and attack or defend. It also has two additional states, hurt and stand. If the two characters reaches specific distances, one characters’ attack can cause hurt of the other character without defense. Besides, there is another state “stand” when there is no other button pressed. The two players can “push” each other with moving forward and touch the other. And in each of the states or actions, we have several frames that can make up to sophisticated animations. 

![image](https://github.com/HiracharleFranklin/KOF-implementation-based-on-FPGA/blob/c76718068822c6a756d4b49428b7048393bcceb5/image/image2.jpg)
 
c)	The end scene 

The end scene of our game will come when one of the players beat the other player, that is, reduce the HP of the other player to 0. In that case, the “KO” image will be shown on the screen, with the dead animation of the beaten player. In this case, a round of the game comes to an end. And if the user press the “space” button on the keyboard, the game will reset all the states and restart the game to the game scene.

![image](https://github.com/HiracharleFranklin/KOF-implementation-based-on-FPGA/blob/c76718068822c6a756d4b49428b7048393bcceb5/image/image3.jpg)

### Block Diagram 

a.	High Level Diagram

![image](https://github.com/HiracharleFranklin/KOF-implementation-based-on-FPGA/blob/c76718068822c6a756d4b49428b7048393bcceb5/image/image4.jpg)
 
b.	State machine diagram of game characters 

![image](https://github.com/HiracharleFranklin/KOF-implementation-based-on-FPGA/blob/c76718068822c6a756d4b49428b7048393bcceb5/image/image5.jpg)

c.	RTL diagram

![image](https://github.com/HiracharleFranklin/KOF-implementation-based-on-FPGA/blob/c76718068822c6a756d4b49428b7048393bcceb5/image/image6.jpg)
 
## Written description of hardware

### Hardware components 

> Sprites and background image files
 
In this lab, we use frame buffer to store all the images used for our lab. To be specific, we store all the actions of the characters, that is, a series of frame images into one RAM file as the buffer. In that way, we can fetch the image of each frame through the address of the ram data. Since our original image is too large and sophisticated, and there does not exist enough on-chip memory for our design. Therefore, we compress our images by resizing the images of height and width as well as reduces the number of colors used in one image. And when drawing the image, we can double its height and width twice to recover its original size. 

> Character drawing component 

This part is used for drawing the animation of our characters as well as changing its positions when receiving the corresponding signal from the character state machine. Here, it will receive the control signal from the character state machine, like the state of character, the current frame number of character, the attack/move/defend signals, etc. It will use these signals to change the position of the character and drawing the frame images by output the image data to the color mapper. 

> Character state machine 

This is the state machine that used to control our character. Generally, we have moving forward, moving backward, stand, attack, hurt, die these states. The transition of the state will be based on the animation/game logic as well as the input signal from the user through keyboard. The control logic is based on our state machine diagram. On each state, it will output some control signals to the character drawing component to specify the position of the character as well as the animation that should be drawn on the screen currently. 

> Attack-defend judger

This is an auxiliary module to judge if the current attack instruction is available. That is, to judge if the distance of two characters is within a specific value and the other character is not successfully defend. It will send the corresponding hurt and attack signal to the character state machine to control the current state 

> Game logic controller 

This is the state machine that warp up all our game, to be specific, it is used to control the game state, like game start, during the game, and game over of our game. It will send the control signals to both the character drawing module and the character state machine to control them. 

> Game Sound component

In our game, we have a background music in it. The music data is compressed by some sound processing software to reduce its size. And we store the sound data into 16-bit file into the onchip-memory, quite the similar way as the image sprites. Besides, we use a audio interface to transform our data into the sound data, and a audio control module is also used to control the implementation of the pace of our sound. 
		

### Module description

