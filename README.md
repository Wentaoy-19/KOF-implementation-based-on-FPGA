# KOF-implementation-based-on-FPGA
This project implements the classical video game Streetfighter on an FPGA board and SystemVerilog Language. Our design includes NIOS II SoC for interfacing with a USB Keyboard as the game controller to manage the keyboard input. The main game logic is supported by FSMs. The animation is done through a sequence of sprites controlled by an animation FSM. The background, sprites and music are stored in SRAM as buffers.

## Team member 
Yao Wentao - ZJU-UIUC Institution, Homepage: https://github.com/Wentaoy-19
Kong Zitai - ZJU-UIUC Institution, Homepage: https://github.com/HiracharleFranklin
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

![image](https://github.com/HiracharleFranklin/KOF-implementation-based-on-FPGA/blob/dc7b63d026ce4a2d09de20204a6c434c8b6eb3cf/image/image7.jpg)
![image](https://github.com/HiracharleFranklin/KOF-implementation-based-on-FPGA/blob/dc7b63d026ce4a2d09de20204a6c434c8b6eb3cf/image/image8.jpg)
![image](https://github.com/HiracharleFranklin/KOF-implementation-based-on-FPGA/blob/dc7b63d026ce4a2d09de20204a6c434c8b6eb3cf/image/image9.jpg)

> Module: clk_0 

This is the clock source module that will generate clock signals used in all of other modules
		
> Module: nios2_gen2_0 

This is the NIOS-II processor serving as the central controller with the interface with other IO and modules and process the C codes we write. 

> Module: onchip_memory2_0 

This is the on chip memory module that can be used for storing data. In this lab, we mostly use it to hold the address of our modules. 

> Module: sdram

This module will allow us to access SDRAM on FPGA. 

> Module: sdram_pll

This module will generate the phase shift of the clock, so that it can provide a precise clock signal for the SDRAM to read and write data.

> Module: sysid_qsys_0 

This module is the system ID checker used for ensuring the compatibility between the hardware and software. 

> Module: jtag_qsys_0 

This allows for terminal access for use in software debugging. 

> Module: keycode 0-5

These are the keycodes delivered by the keyboard. 

> Module: otg_hpi_address

This specifies the address for reading and writing value on the USB OTG chip.

> Module: otg_hpi_r

This is the control signal for reading value from OTG chip. 

> Module: otg_hpi_w

This is the control signal for writing value to the USB OTG chip.

> Module: otg_chip_cs

This is the chip select control signal for the OTG chip 

> Module: otg_hpi_reset

This is used to reset the state of the chip

> Module: otg_hpi_data

This is for the data connection between USB chip and FPGA. 

### Written description of Software

In our design, the software serves the same function as our lab8. That is to receive the keycode input from the keyboard. In the design of lab8, we use a 16-bit keycode to receive the input from the keyboard. Since a single keycode needs 8-btis, so it actually can receive 2 different keycodes. But in our design, since this is a game with two players, each has different keycodes to control the game characters. Therefore, we need to let the NIOS-II core to receive different keycode input at the same time. From the protocol our usb, it can only receive 6 keycodes at the same time. Therefore, we use six 8-bit keycodes to receive the input from the keyboard. The code is nearly the same as our lab8 code, as shown below: 
 
 ![image](https://github.com/HiracharleFranklin/KOF-implementation-based-on-FPGA/blob/dc7b63d026ce4a2d09de20204a6c434c8b6eb3cf/image/%E5%9B%BE%E7%89%8710.jpg)
 
The keycodes will be passed through the PIO as the output to our design circuit. And these keycodes input in our top level will be wrap up through a key controller module to generate valid control signals to the character state machine. 

### Design Statistic Table
 
 ![image](https://github.com/HiracharleFranklin/KOF-implementation-based-on-FPGA/blob/dc7b63d026ce4a2d09de20204a6c434c8b6eb3cf/image/image11.jpg)

## Conclusion 

### Functionality Discussion

In our design, we generally achieve the function of the baseline in our proposal. That is, to achieve a basic fighting game framework. We have two players in the game, they have the basic actions like move, attack, defend and hurt. In each action, we achieve the animation to make it looks lively. Besides, some general game logic is also well designed, like the defense can used to against the attack from the other players, and the attack can interrupt the moving and stand state, etc. And we have HP bar to record the health point of each player, so we get the general functionality of a round of the game. Additionally, a background music is also added to our design to make our game lively. With some refine to the game state and some parameters, we achieve the baseline of our design. 

The feature of our design is that. We achieve the basic framework of a fighting game, which looks very closer to the original game. Besides, we have very sophisticated background images and fluent animation in each action of our game characters, and the control to these animations is also quite fluent. We have well designed animation control state machine to make the transition of each action very fluent. Additionally, the UI with the HP bar is also very beautiful and like the original king of fighter game. And the background music added to the game also makes it much better. 

However, due to the time limitation, there still exists some functions that we should achieve with more time. Firstly, the game of our baseline is not that fun, since each player only have attack and defense. This game logic is not complete. We can add more actions with animation to our game to make it better, like some more attack actions to break the defense from the other character. Or the skill with sophisticated animation that can cause huge damage to the other players. Additionally, the actions like jump and rolling can also be added to this game to make it more fun. Secondly, from now on we only achieve the background music. And with more time, we can add more sound effect accompanied with the action of the game to make it closer to the original KOF game. 

### Problems and challenges we encountered

In our design process, we encountered many bugs. Among all these problems, there are some problems and challenges that are quite representative.

To begin with, the character state machine is a big challenge and also the core of our game. All our animations and character actions are based on the state machine. We firstly combine the state machine and the character drawing module together. However, we find that through this process, we module will be quite huge and not that easily to be understood. So, we redesign this part and divide the character drawing module and the character state machine. The state machine has some output signals that serves as the input signal to control our character drawing module. In that case, our design process becomes more fluent. 

Secondly, after we load all the character animations and background images into the on-chip memory, we find that the image data are so large that is out of the capacity of the on-chip memory. Therefore, we compress all our images by resizing the images. And we change the codes of drawing so that it can double the size of images. So that we can draw all our images with less memory. 

Lastly, the game logic design is also another challenge that we meet. Since the fighting game need to judge when the attack is valid, or in which situation the defense is successfully done. So, we write a independent module between the key input and the character state machine to better organize these input signals. With the logic designs, this module will send the final hurt/attack/defense signals to the state machine. So that it makes our design clearer and achieve the function. 

### Final conclusions 
In our final project, with the teamwork with the two of us, we achieve the street fighter game. In our design, we achieve basic fighting game framework of some basic actions like moving, attack, defense. In each of the action, we have animation with several frames to make it lively. We also have background music added to this game. In our design process, with encounter with several problems like the state machine design and the huge amount of image data. With hard work, we eventually figure out these problems and achieve our design. However, if we have more time, we can still add more game functionalities to our design. This FPGA based game design provide both of us the knowledge of the hardware design through FPGA and the knowledge of logic design, software-hardware interactions. We think it is a wonderful experiences in our study in ECE field.
