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
