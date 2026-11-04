/***************** 
 * Mazetask *
 *****************/


// store info about the experiment session:
let expName = 'MazeTask';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Intro_ScreenRoutineBegin());
flowScheduler.add(Intro_ScreenRoutineEachFrame());
flowScheduler.add(Intro_ScreenRoutineEnd());
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const Items_LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Items_LoopLoopBegin(Items_LoopLoopScheduler));
flowScheduler.add(Items_LoopLoopScheduler);
flowScheduler.add(Items_LoopLoopEnd);





flowScheduler.add(Exit_ScreenRoutineBegin());
flowScheduler.add(Exit_ScreenRoutineEachFrame());
flowScheduler.add(Exit_ScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'Stimuli.xlsx', 'path': 'Stimuli.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.ERROR);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.1.5';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var Intro_ScreenClock;
var Intro_Screen_Text;
var Intro_Screen_Key;
var InstructionsClock;
var Instruction_Text;
var Instruction_Key;
var MazeClock;
var LeftText;
var RightText;
var Incorrect_Text;
var Response_key;
var Comp_ScreenClock;
var Comp_Key;
var Comprehension_Question;
var Comprehension_Answer_Choices;
var Exit_ScreenClock;
var Exit_Text;
var Exit_Key;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Intro_Screen"
  Intro_ScreenClock = new util.Clock();
  Intro_Screen_Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Intro_Screen_Text',
    text: 'Welcome to the Maze Task Demo.\n\nIn this study, you will "build" sentences one word at a time by selecting between two choices. Only one of these choices will be the correct continuation of the sentence. \n\nUse the \'a\' key to select the word on the left side of the screen, and the \'l\' key to select the word on the right side of the screen.\n\nPress \'1\' to continue.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Intro_Screen_Key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  Instruction_Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instruction_Text',
    text: "After each sentence, there will be a comprehension question based on that sentence. \n\nPlease respond to this question by pressing left for yes, and right for no.\n\nThe task will begin on the next screen. Press the '1' key when you are ready.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Instruction_Key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Maze"
  MazeClock = new util.Clock();
  LeftText = new visual.TextStim({
    win: psychoJS.window,
    name: 'LeftText',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.25), 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  RightText = new visual.TextStim({
    win: psychoJS.window,
    name: 'RightText',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.25, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  Incorrect_Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Incorrect_Text',
    text: 'Please select the correct option.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: -3.0 
  });
  
  Response_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Comp_Screen"
  Comp_ScreenClock = new util.Clock();
  Comp_Key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Comprehension_Question = new visual.TextStim({
    win: psychoJS.window,
    name: 'Comprehension_Question',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  Comprehension_Answer_Choices = new visual.TextStim({
    win: psychoJS.window,
    name: 'Comprehension_Answer_Choices',
    text: 'a <-- YES    |    NO --> l',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Exit_Screen"
  Exit_ScreenClock = new util.Clock();
  Exit_Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Exit_Text',
    text: "Thank you for participating!\n\nThe results will be updated on the screen soon.\n\nPress '1' to exit this screen.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Exit_Key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _Intro_Screen_Key_allKeys;
var LeftVar;
var RightVar;
var Correct;
var Incorrect;
var Intro_ScreenComponents;
function Intro_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Intro_Screen' ---
    t = 0;
    Intro_ScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Intro_Screen.started', globalClock.getTime());
    Intro_Screen_Key.keys = undefined;
    Intro_Screen_Key.rt = undefined;
    _Intro_Screen_Key_allKeys = [];
    // Run 'Begin Routine' code from Initialization_Code
    LeftVar = (("r" + Region_Num.toString()) + "l");
    RightVar = (("r" + Region_Num.toString()) + "r");
    Correct = (("r" + Region_Num.toString()) + "corr");
    Incorrect = (("r" + Region_Num.toString()) + "incorr");
    
    // keep track of which components have finished
    Intro_ScreenComponents = [];
    Intro_ScreenComponents.push(Intro_Screen_Text);
    Intro_ScreenComponents.push(Intro_Screen_Key);
    
    Intro_ScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Intro_ScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Intro_Screen' ---
    // get current time
    t = Intro_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Intro_Screen_Text* updates
    if (t >= 0.0 && Intro_Screen_Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Intro_Screen_Text.tStart = t;  // (not accounting for frame time here)
      Intro_Screen_Text.frameNStart = frameN;  // exact frame index
      
      Intro_Screen_Text.setAutoDraw(true);
    }
    
    
    // *Intro_Screen_Key* updates
    if (t >= 0.0 && Intro_Screen_Key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Intro_Screen_Key.tStart = t;  // (not accounting for frame time here)
      Intro_Screen_Key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Intro_Screen_Key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Intro_Screen_Key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Intro_Screen_Key.clearEvents(); });
    }
    
    if (Intro_Screen_Key.status === PsychoJS.Status.STARTED) {
      let theseKeys = Intro_Screen_Key.getKeys({keyList: ['space'], waitRelease: false});
      _Intro_Screen_Key_allKeys = _Intro_Screen_Key_allKeys.concat(theseKeys);
      if (_Intro_Screen_Key_allKeys.length > 0) {
        Intro_Screen_Key.keys = _Intro_Screen_Key_allKeys[_Intro_Screen_Key_allKeys.length - 1].name;  // just the last key pressed
        Intro_Screen_Key.rt = _Intro_Screen_Key_allKeys[_Intro_Screen_Key_allKeys.length - 1].rt;
        Intro_Screen_Key.duration = _Intro_Screen_Key_allKeys[_Intro_Screen_Key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Intro_ScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Intro_ScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Intro_Screen' ---
    Intro_ScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Intro_Screen.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Intro_Screen_Key.corr, level);
    }
    psychoJS.experiment.addData('Intro_Screen_Key.keys', Intro_Screen_Key.keys);
    if (typeof Intro_Screen_Key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Intro_Screen_Key.rt', Intro_Screen_Key.rt);
        psychoJS.experiment.addData('Intro_Screen_Key.duration', Intro_Screen_Key.duration);
        routineTimer.reset();
        }
    
    Intro_Screen_Key.stop();
    // the Routine "Intro_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _Instruction_Key_allKeys;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions' ---
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instructions.started', globalClock.getTime());
    Instruction_Key.keys = undefined;
    Instruction_Key.rt = undefined;
    _Instruction_Key_allKeys = [];
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(Instruction_Text);
    InstructionsComponents.push(Instruction_Key);
    
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions' ---
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instruction_Text* updates
    if (t >= 0.0 && Instruction_Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instruction_Text.tStart = t;  // (not accounting for frame time here)
      Instruction_Text.frameNStart = frameN;  // exact frame index
      
      Instruction_Text.setAutoDraw(true);
    }
    
    
    // *Instruction_Key* updates
    if (t >= 0.0 && Instruction_Key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instruction_Key.tStart = t;  // (not accounting for frame time here)
      Instruction_Key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Instruction_Key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Instruction_Key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Instruction_Key.clearEvents(); });
    }
    
    if (Instruction_Key.status === PsychoJS.Status.STARTED) {
      let theseKeys = Instruction_Key.getKeys({keyList: ['space'], waitRelease: false});
      _Instruction_Key_allKeys = _Instruction_Key_allKeys.concat(theseKeys);
      if (_Instruction_Key_allKeys.length > 0) {
        Instruction_Key.keys = _Instruction_Key_allKeys[_Instruction_Key_allKeys.length - 1].name;  // just the last key pressed
        Instruction_Key.rt = _Instruction_Key_allKeys[_Instruction_Key_allKeys.length - 1].rt;
        Instruction_Key.duration = _Instruction_Key_allKeys[_Instruction_Key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions' ---
    InstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Instruction_Key.corr, level);
    }
    psychoJS.experiment.addData('Instruction_Key.keys', Instruction_Key.keys);
    if (typeof Instruction_Key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Instruction_Key.rt', Instruction_Key.rt);
        psychoJS.experiment.addData('Instruction_Key.duration', Instruction_Key.duration);
        routineTimer.reset();
        }
    
    Instruction_Key.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Items_Loop;
function Items_LoopLoopBegin(Items_LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Items_Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Stimuli.xlsx',
      seed: undefined, name: 'Items_Loop'
    });
    psychoJS.experiment.addLoop(Items_Loop); // add the loop to the experiment
    currentLoop = Items_Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Items_Loop.forEach(function() {
      snapshot = Items_Loop.getSnapshot();
    
      Items_LoopLoopScheduler.add(importConditions(snapshot));
      const Region_LoopLoopScheduler = new Scheduler(psychoJS);
      Items_LoopLoopScheduler.add(Region_LoopLoopBegin(Region_LoopLoopScheduler, snapshot));
      Items_LoopLoopScheduler.add(Region_LoopLoopScheduler);
      Items_LoopLoopScheduler.add(Region_LoopLoopEnd);
      Items_LoopLoopScheduler.add(Comp_ScreenRoutineBegin(snapshot));
      Items_LoopLoopScheduler.add(Comp_ScreenRoutineEachFrame());
      Items_LoopLoopScheduler.add(Comp_ScreenRoutineEnd(snapshot));
      Items_LoopLoopScheduler.add(Items_LoopLoopEndIteration(Items_LoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var Region_Loop;
function Region_LoopLoopBegin(Region_LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Region_Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 16, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'Region_Loop'
    });
    psychoJS.experiment.addLoop(Region_Loop); // add the loop to the experiment
    currentLoop = Region_Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Region_Loop.forEach(function() {
      snapshot = Region_Loop.getSnapshot();
    
      Region_LoopLoopScheduler.add(importConditions(snapshot));
      Region_LoopLoopScheduler.add(MazeRoutineBegin(snapshot));
      Region_LoopLoopScheduler.add(MazeRoutineEachFrame());
      Region_LoopLoopScheduler.add(MazeRoutineEnd(snapshot));
      Region_LoopLoopScheduler.add(Region_LoopLoopEndIteration(Region_LoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Region_LoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Region_Loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function Region_LoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function Items_LoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Items_Loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function Items_LoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var error_text_visibility;
var keys;
var userChoice;
var key1;
var key2;
var _Response_key_allKeys;
var MazeComponents;
function MazeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Maze' ---
    t = 0;
    MazeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Maze.started', globalClock.getTime());
    // Run 'Begin Routine' code from Error_Display_Code
    error_text_visibility = 0;
    keys = [];
    userChoice = "x";
    key1 = eval(Correct).toString();
    key2 = eval(Incorrect).toString();
    
    LeftText.setText(eval(LeftVar));
    RightText.setText(eval(RightVar));
    Response_key.keys = undefined;
    Response_key.rt = undefined;
    _Response_key_allKeys = [];
    // keep track of which components have finished
    MazeComponents = [];
    MazeComponents.push(LeftText);
    MazeComponents.push(RightText);
    MazeComponents.push(Incorrect_Text);
    MazeComponents.push(Response_key);
    
    MazeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function MazeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Maze' ---
    // get current time
    t = MazeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *LeftText* updates
    if (t >= 0.0 && LeftText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LeftText.tStart = t;  // (not accounting for frame time here)
      LeftText.frameNStart = frameN;  // exact frame index
      
      LeftText.setAutoDraw(true);
    }
    
    
    // *RightText* updates
    if (t >= 0.0 && RightText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RightText.tStart = t;  // (not accounting for frame time here)
      RightText.frameNStart = frameN;  // exact frame index
      
      RightText.setAutoDraw(true);
    }
    
    
    if (Incorrect_Text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      Incorrect_Text.setOpacity(error_text_visibility, false);
    }
    
    // *Incorrect_Text* updates
    if (t >= 0 && Incorrect_Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Incorrect_Text.tStart = t;  // (not accounting for frame time here)
      Incorrect_Text.frameNStart = frameN;  // exact frame index
      
      Incorrect_Text.setAutoDraw(true);
    }
    
    
    // *Response_key* updates
    if (t >= 0.0 && Response_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Response_key.tStart = t;  // (not accounting for frame time here)
      Response_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Response_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Response_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Response_key.clearEvents(); });
    }
    
    if (Response_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = Response_key.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _Response_key_allKeys = _Response_key_allKeys.concat(theseKeys);
      if (_Response_key_allKeys.length > 0) {
        Response_key.keys = _Response_key_allKeys[_Response_key_allKeys.length - 1].name;  // just the last key pressed
        Response_key.rt = _Response_key_allKeys[_Response_key_allKeys.length - 1].rt;
        Response_key.duration = _Response_key_allKeys[_Response_key_allKeys.length - 1].duration;
        // was this correct?
        if (Response_key.keys == eval(Correct)) {
            Response_key.corr = 1;
        } else {
            Response_key.corr = 0;
        }
      }
    }
    
    // Run 'Each Frame' code from Routine_End
    keys = psychoJS.eventManager.getKeys();
    if ((keys.length > 0)) {
        userChoice = keys.slice((- 1))[0];
        if ((userChoice === key2)) {
            error_text_visibility = 1;
        }
        if ((userChoice === key1)) {
            continueRoutine = false;
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    MazeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MazeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Maze' ---
    MazeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Maze.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (Response_key.keys === undefined) {
      if (['None','none',undefined].includes(eval(Correct))) {
         Response_key.corr = 1;  // correct non-response
      } else {
         Response_key.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Response_key.corr, level);
    }
    psychoJS.experiment.addData('Response_key.keys', Response_key.keys);
    psychoJS.experiment.addData('Response_key.corr', Response_key.corr);
    if (typeof Response_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Response_key.rt', Response_key.rt);
        psychoJS.experiment.addData('Response_key.duration', Response_key.duration);
        }
    
    Response_key.stop();
    // Run 'End Routine' code from Routine_End
    Region_Num += 1;
    LeftVar = (("r" + Region_Num.toString()) + "l");
    RightVar = (("r" + Region_Num.toString()) + "r");
    Correct = (("r" + Region_Num.toString()) + "corr");
    Incorrect = (("r" + Region_Num.toString()) + "incorr");
    
    // the Routine "Maze" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _Comp_Key_allKeys;
var Comp_ScreenComponents;
function Comp_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Comp_Screen' ---
    t = 0;
    Comp_ScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Comp_Screen.started', globalClock.getTime());
    Comp_Key.keys = undefined;
    Comp_Key.rt = undefined;
    _Comp_Key_allKeys = [];
    Comprehension_Question.setText(Comp);
    // keep track of which components have finished
    Comp_ScreenComponents = [];
    Comp_ScreenComponents.push(Comp_Key);
    Comp_ScreenComponents.push(Comprehension_Question);
    Comp_ScreenComponents.push(Comprehension_Answer_Choices);
    
    Comp_ScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Comp_ScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Comp_Screen' ---
    // get current time
    t = Comp_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Comp_Key* updates
    if (t >= 0.0 && Comp_Key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Comp_Key.tStart = t;  // (not accounting for frame time here)
      Comp_Key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Comp_Key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Comp_Key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Comp_Key.clearEvents(); });
    }
    
    if (Comp_Key.status === PsychoJS.Status.STARTED) {
      let theseKeys = Comp_Key.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _Comp_Key_allKeys = _Comp_Key_allKeys.concat(theseKeys);
      if (_Comp_Key_allKeys.length > 0) {
        Comp_Key.keys = _Comp_Key_allKeys[_Comp_Key_allKeys.length - 1].name;  // just the last key pressed
        Comp_Key.rt = _Comp_Key_allKeys[_Comp_Key_allKeys.length - 1].rt;
        Comp_Key.duration = _Comp_Key_allKeys[_Comp_Key_allKeys.length - 1].duration;
        // was this correct?
        if (Comp_Key.keys == CompAns) {
            Comp_Key.corr = 1;
        } else {
            Comp_Key.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Comprehension_Question* updates
    if (t >= 0.0 && Comprehension_Question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Comprehension_Question.tStart = t;  // (not accounting for frame time here)
      Comprehension_Question.frameNStart = frameN;  // exact frame index
      
      Comprehension_Question.setAutoDraw(true);
    }
    
    
    // *Comprehension_Answer_Choices* updates
    if (t >= 0.0 && Comprehension_Answer_Choices.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Comprehension_Answer_Choices.tStart = t;  // (not accounting for frame time here)
      Comprehension_Answer_Choices.frameNStart = frameN;  // exact frame index
      
      Comprehension_Answer_Choices.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Comp_ScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var Region_Num;
function Comp_ScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Comp_Screen' ---
    Comp_ScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Comp_Screen.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (Comp_Key.keys === undefined) {
      if (['None','none',undefined].includes(CompAns)) {
         Comp_Key.corr = 1;  // correct non-response
      } else {
         Comp_Key.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Comp_Key.corr, level);
    }
    psychoJS.experiment.addData('Comp_Key.keys', Comp_Key.keys);
    psychoJS.experiment.addData('Comp_Key.corr', Comp_Key.corr);
    if (typeof Comp_Key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Comp_Key.rt', Comp_Key.rt);
        psychoJS.experiment.addData('Comp_Key.duration', Comp_Key.duration);
        routineTimer.reset();
        }
    
    Comp_Key.stop();
    // Run 'End Routine' code from Reset_Code
    Region_Num = 0;
    LeftVar = (("r" + Region_Num.toString()) + "l");
    RightVar = (("r" + Region_Num.toString()) + "r");
    Correct = (("r" + Region_Num.toString()) + "corr");
    Incorrect = (("r" + Region_Num.toString()) + "incorr");
    psychoJS.eventManager.clearEvents({"eventType": "keyboard"});
    
    // the Routine "Comp_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _Exit_Key_allKeys;
var Exit_ScreenComponents;
function Exit_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Exit_Screen' ---
    t = 0;
    Exit_ScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Exit_Screen.started', globalClock.getTime());
    Exit_Key.keys = undefined;
    Exit_Key.rt = undefined;
    _Exit_Key_allKeys = [];
    // keep track of which components have finished
    Exit_ScreenComponents = [];
    Exit_ScreenComponents.push(Exit_Text);
    Exit_ScreenComponents.push(Exit_Key);
    
    Exit_ScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Exit_ScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Exit_Screen' ---
    // get current time
    t = Exit_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Exit_Text* updates
    if (t >= 0.0 && Exit_Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Exit_Text.tStart = t;  // (not accounting for frame time here)
      Exit_Text.frameNStart = frameN;  // exact frame index
      
      Exit_Text.setAutoDraw(true);
    }
    
    
    // *Exit_Key* updates
    if (t >= 0.0 && Exit_Key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Exit_Key.tStart = t;  // (not accounting for frame time here)
      Exit_Key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Exit_Key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Exit_Key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Exit_Key.clearEvents(); });
    }
    
    if (Exit_Key.status === PsychoJS.Status.STARTED) {
      let theseKeys = Exit_Key.getKeys({keyList: ['space'], waitRelease: false});
      _Exit_Key_allKeys = _Exit_Key_allKeys.concat(theseKeys);
      if (_Exit_Key_allKeys.length > 0) {
        Exit_Key.keys = _Exit_Key_allKeys[_Exit_Key_allKeys.length - 1].name;  // just the last key pressed
        Exit_Key.rt = _Exit_Key_allKeys[_Exit_Key_allKeys.length - 1].rt;
        Exit_Key.duration = _Exit_Key_allKeys[_Exit_Key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Exit_ScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Exit_ScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Exit_Screen' ---
    Exit_ScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Exit_Screen.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Exit_Key.corr, level);
    }
    psychoJS.experiment.addData('Exit_Key.keys', Exit_Key.keys);
    if (typeof Exit_Key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Exit_Key.rt', Exit_Key.rt);
        psychoJS.experiment.addData('Exit_Key.duration', Exit_Key.duration);
        routineTimer.reset();
        }
    
    Exit_Key.stop();
    // the Routine "Exit_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
