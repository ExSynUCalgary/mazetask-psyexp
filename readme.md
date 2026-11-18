# Maze PsychoPy Readme

This PsyExp file is fully functional in PsychoPy Studio 2026.2.5. The initial version was built in version 2024.1.5.

The code components have intentional redundancies and failsafe mechanisms. This is due to the way that the AutoJS writer operates. The UCalgary Experimental Syntax Lab is a Python first lab and many of these could be removed it were only meant to be run locally through the PsychoPy builder. In order to ensure straightforward Pavlovia compatibility, additional code has been added into the builder. In other words, this experiment is constructed in such a way that it will not require manual changes to the JS file that it generates to run on Pavlovia, simplifying the process when changes are made in PsychoPy and then uploaded to Pavlovia. 

## Intro Screen

This is where all of the variables that will be used in later routines are established. Their initial values are set in the code block named "Initialization_Code".

Region_Num - This variable is a number that begins at 0 and increments by 1 after each Maze routine. The other variables make use of this to point to their appropriate values within the Maze Region_Loop.

LeftVar - Variable associated with text on the left side of the screen during Maze Region_Loop.

RightVar - Variable associated with text on the right side of the screen during Maze Region_Loop.

Correct - Evaluated as the correct key response (either 'a' or 'l' in the demo). This is used to determine the correct word (left or right) in the maze task at the beginning of each Maze routine. This variable allows for a different routine ending key to be assigned as determined by the stimuli input spreadsheet (which is randomized in the demo).

Incorrect - This will always be evaluated as the opposite of Correct (i.e. if Correct is evaluated as the 'a' key, this variable will be evaluated as 'l' and vice versa). A participant pressing the incorrect key during the Maze routine will cause text to display on the screen reminding them to select the correct option for continuing the sentence. The full mechanics of this are discussed in the Error_Display_Code component in the Maze routine.

Initilization_Code - This code block sets all initial values for variables that are used within the Maze routine. Because the stimuli spreadsheet begins at r0, all variables are manually set to point to those respective columns ("r0l" = region 0 left text, "r0r" = region 0 right text, etc.) before setting the Region_Num variable value. This is done manually because of the AutoJS writing in PsychoPy which converts the local builder code into JS code automatically for running online experiments on Pavlovia. Calling the Region_Num variable as it increments and converting it into a string within the Maze loop is fine, but it will not work in the JS file in this initial block. The error_text_visibility variable is set to zero here to both initialize the variable and ensure that the reminder text is not displayed at the start of the maze. When the participant selects the wrong option in the Maze loop, this will flip to 1. The full mechanics of this are discussed in the Error_Display_Code component in the Maze routine.

## Instructions

Optional additional instruction text routine that is used to explain how the maze task works in the demos we have run. Can be freely deleted/modified.

## Items_Loop 

The Stimuli file needs to be selected in this outermost loop. The parameters from the Stimuli file will be passed down into the embedded loop. The number of repeats here should be set to 1 unless otherwise required by your design.

## Region_Loop

This is the loop that increments through each region. It is important that Num. repeats is set to the number of regions in each stimuli sentence and that the Loop type is sequential. The number of regions for all stimuli items must be identical.

Maze Routine - This routine should not need to be modified as it is. The allowed keys setting in the Response_key component is the only thing that would likely need changing. The other values are determined elsewhere and modifications to values in this routine will likely break the experiment. All functions will be explained as succinctly as possible, but modify at your own risk.

Error_Display_Code - This code will reset the error_text_visibilty value to zero at the beginning of each iteration (redundant for region 0, but necessary for all other regions if participants do press the incorrect key).

The keys string here stores all of the keys pressed by participants in the current iteration of the routine. Because it is a separate string from the get.keys event that is used in the Routine_End component, it needs to be reset to clear out the input from previous loops. This avoids skipping regions where the "correct" choice is on the same side of the screen as the previous region. Without this reset, if there are two regions in a row where the correct choice is on the left side of the screen, the second region will be skipped as the keypress for the "correct" choice will be checked and force the end of the routine on the first possible frame.

The userChoice variable is set to an arbitrary value at the start of the routine so that later code in this routine is not attempting to index an empty list.

key1 corresponds to the correct choice to advance the Maze task ('a' for the left side of the screen, 'l' for the right side).

key2 corresponds to the incorrect choice (essentially, the opposite value of key1)

The values for key1 and key2 are compared to the Userchoice every frame in the Routine_End code component.


LeftText - Mostly self explanatory -- displays text on the left side of the screen corresponding to the 'a' key based on the LeftVar variable which is initialized at the start of the experiment and updated at the end of step of the inner loop.

RightText - Mostly self explanatory -- displays text on the left side of the screen corresponding to the 'l' key based on the RightVar variable which is initialized at the start of the experiment and updated at the end of step of the inner loop.

Incorrect_Text - A static reminder text that will display when participants select the incorrect option in the maze. The Opacity is controlled via the error_text_visibility variable set to 0 initially and flipping to 1 when participants press the incorrect key.


Response_key - This component is required to generate by region reaction times in the data file. It will measure the reaction time from the start of the routine until participants press the correct key to advance the Maze task. Removing this component will not impact the functionality of the experiment, but it will create more work in the data processing stage as reaction times will need to be calculated.

### Routine_End

This code component has code that is checked each frame as well as at the end of the routine.

### Each Frame

The keys string is set to be equal to the getKeys() event. Because we don't want to attempt to index an empty string, the userChoice variable will only be assigned a new value when there is at least one value in the keys string (i.e. when the participant has pressed at least one key).

As an additional failsafe, this is why the userChoice variable was assigned an arbitrary value ('x') at the beginning of the routine so that it would not accidentally store the correct value from a previous loop and would not skip the routine/display the reminder text at the bottom before a participant has time to respond.

The inner if loops are independent to ensure that they only trigger when their unique conditions are met. If the last key that the participant presses corresponds to key2 (incorrect), the opacity of the reminder text is set to 1 making it visible at the bottom of the screen. This value is set back to 0 at the beginning of the routine meaning that participants will only see the reminder text when they press the incorrect key on a given loop. If the last key that the participant presses corresponds to key1 (correct), the routine ends and the maze advances to the next loop. Once the participant reaches the end of the sentence in the Maze, the experiment flow will force them out of the loop in the Comp_Screen routine where they are asked a comprehension question.

### End Routine

This tab handles the region increment and reassignment of variables for the next iteration of the routine. This is fairly self explanatory -- increment Region_Num by 1 and then reassign all other variables using the new region number so that they point to the correct columns in the Stimuli spreadsheet. The values of these variables will be reset in the Comp_Screen routine so there is no issue with the Region_Num variable incrementing beyond the number of regions available in the Stimuli file.

## Comp_Screen 

Displays the comprehension question for the sentence (Comprehension_Question component) as well as reminder text on the bottom for which keys are available to use as answers ('a' or 'l' by default -- Comprehension_Answer component). The Comp_Key component is restricted to only accept 'a' or 'l' as possible choices and has the correct answer field corresponding to the CompAns column in the Stimuli file.

The Reset_Code component is similar to the initialization component in the first routine. All variables are set to their initial values. The updating variable (LeftVar, RightVar, Correct, Incorrect) are set to default values manually ("r0l", "r0rr", etc.) to avoid issues with the AutoJS writer mixing the order of operations when generating the JS file. The previous keypresses from the comprehension question are also cleared as a failsafe to avoid unintentionally skipping the first region of the next Maze item if the correct key corresponds to the key the participant used to respond to the comprehension question.

After the Comp_Screen routine, the experiment will advance to the beginning and begin the Region_Loop again on the next item. Once all items have been seen by participants, the experiment will exit the Items_Loop and move to the Exit_Screen routine. 

If your experiment design requires a practice block or multiple blocks with breaks, simply insert additional iterations of the Maze and Comp_Screen routines with new loops built to fit your criteria. This will avoid needing to rebuild all code components as shown in this demo.


