:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Planner App
## CS 110 Final Project
### Fall 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

<< [repl](#) >>

<< [link to demo presentation slides](#) >>

### Team:  Boogers 
####  Team Members: John Dambra, Erin Zhao, Rachel Todd

***

## Project Description *(Software Lead)*

<< Give an overview of your project >>
It is a calendar that ranges from May 2022 to April 2023 and has a somewhat working notes function to go along with it

***    

## User Interface Design *(Front End Specialist)*

The picture of the GUI is in the assets folder. "assets/GUI.png"
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>
* 

***        

## Program Design *(Backend Specialist)*

* Non-Standard libraries
    * pygame
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
        * ![class diagram](assets/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * << You should have a list of each of your classes with a description. >>

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:

* main.py
* src
    * <all of your python files should go here>
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*

   * You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - John Dambra

I made all of the assets into transparent pngs to be used fluidly on a background as buttons to scroll through the months on the calendar. Created a buttons sprite class that created the sprites in pygame, re-sized each button accordingly and positioned them in the proper spot on the window.

Created a calendar class that managed the creation of the calendar grid, clearing and re-creating the calendar when changing months to avoid overlapping of text

Attempted to create a notes class to create a dynamic text box next to the calendar for note taking purposes. Unfortunately, could not figure out how to get text wrapping within the text box to make it function properly. I was also unable to create dictionaries to load and saves the notes to each month respectively.

### Front End Specialist - Erin Zhao

We designed a GUI layout for our app. We also designed sprite icons for things like buttons. We also created a calendar layout for the monthly and weekly calendars, as well as the general layout of the todo section and the calendars.

### Back End Specialist - Rachel Todd

We have created files for the different components of our project. These components include a calendar, notes, and button, layout. 

## Testing *(Software Lead)*

* << Describe your testing strategy for your project. >>
    * << Example >>

## ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run program  | GUI window appears using pygame and displays current month, text box, and left and right arrow buttons |          |
|  2  | click left button  | calendar goes back 1 months (rolls over to other end if at an end) |                 |
| 3 | click right button | calendar goes forward 1 month (rolls over to other end if at an end)| |
| 4 | click text box | activates text box| |
| 5 | push any key on keyboard except backspace| letter/symbol in text box| |
 6 | push backspace on keyboard | text box string deletes last written character | doesn't backspace |