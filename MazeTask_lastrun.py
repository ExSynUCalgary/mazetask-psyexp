#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.5),
    on November 04, 2026, at 10:53
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.5'
expName = 'MazeTask'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 960]
_loggingLevel = logging.getLevel('error')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\jesse\\My Drive\\Work\\GithubProjects\\Maze_Task_Psychopy\\MazeTask_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('Intro_Screen_Key') is None:
        # initialise Intro_Screen_Key
        Intro_Screen_Key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Intro_Screen_Key',
        )
    if deviceManager.getDevice('Instruction_Key') is None:
        # initialise Instruction_Key
        Instruction_Key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Instruction_Key',
        )
    if deviceManager.getDevice('Response_key') is None:
        # initialise Response_key
        Response_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Response_key',
        )
    if deviceManager.getDevice('Comp_Key') is None:
        # initialise Comp_Key
        Comp_Key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Comp_Key',
        )
    if deviceManager.getDevice('Exit_Key') is None:
        # initialise Exit_Key
        Exit_Key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Exit_Key',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # enter 'rush' mode (raise CPU priority)
    if not PILOTING:
        core.rush(enable=True)
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Intro_Screen" ---
    Intro_Screen_Text = visual.TextStim(win=win, name='Intro_Screen_Text',
        text='Welcome to the Maze Task Demo.\n\nIn this study, you will "build" sentences one word at a time by selecting between two choices. Only one of these choices will be the correct continuation of the sentence. \n\nUse the \'a\' key to select the word on the left side of the screen, and the \'l\' key to select the word on the right side of the screen.\n\nPress \'1\' to continue.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Intro_Screen_Key = keyboard.Keyboard(deviceName='Intro_Screen_Key')
    # Set experiment start values for variable component Region_Num
    Region_Num = 0
    Region_NumContainer = []
    # Set experiment start values for variable component LeftVar
    LeftVar = ''
    LeftVarContainer = []
    # Set experiment start values for variable component RightVar
    RightVar = ''
    RightVarContainer = []
    # Set experiment start values for variable component Correct
    Correct = ''
    CorrectContainer = []
    # Set experiment start values for variable component Incorrect
    Incorrect = ''
    IncorrectContainer = []
    
    # --- Initialize components for Routine "Instructions" ---
    Instruction_Text = visual.TextStim(win=win, name='Instruction_Text',
        text="After each sentence, there will be a comprehension question based on that sentence. \n\nPlease respond to this question by pressing left for yes, and right for no.\n\nThe task will begin on the next screen. Press the '1' key when you are ready.",
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Instruction_Key = keyboard.Keyboard(deviceName='Instruction_Key')
    
    # --- Initialize components for Routine "Maze" ---
    LeftText = visual.TextStim(win=win, name='LeftText',
        text='',
        font='Open Sans',
        pos=(-.250, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    RightText = visual.TextStim(win=win, name='RightText',
        text='',
        font='Open Sans',
        pos=(.25, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    Incorrect_Text = visual.TextStim(win=win, name='Incorrect_Text',
        text='Please select the correct option.',
        font='Arial',
        pos=(0, -0.250), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-3.0);
    Response_key = keyboard.Keyboard(deviceName='Response_key')
    
    # --- Initialize components for Routine "Comp_Screen" ---
    Comp_Key = keyboard.Keyboard(deviceName='Comp_Key')
    Comprehension_Question = visual.TextStim(win=win, name='Comprehension_Question',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Comprehension_Answer_Choices = visual.TextStim(win=win, name='Comprehension_Answer_Choices',
        text='a <-- YES    |    NO --> l',
        font='Open Sans',
        pos=(0, -.25), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Exit_Screen" ---
    Exit_Text = visual.TextStim(win=win, name='Exit_Text',
        text="Thank you for participating!\n\nThe results will be updated on the screen soon.\n\nPress '1' to exit this screen.",
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Exit_Key = keyboard.Keyboard(deviceName='Exit_Key')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Intro_Screen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Intro_Screen.started', globalClock.getTime(format='float'))
    # create starting attributes for Intro_Screen_Key
    Intro_Screen_Key.keys = []
    Intro_Screen_Key.rt = []
    _Intro_Screen_Key_allKeys = []
    # Run 'Begin Routine' code from Initialization_Code
    LeftVar ="r" + str(Region_Num) + "l"
    RightVar ="r" + str(Region_Num) + "r"
    Correct ="r" + str(Region_Num) + "corr"
    Incorrect ="r" + str(Region_Num) + "incorr"
    
    # keep track of which components have finished
    Intro_ScreenComponents = [Intro_Screen_Text, Intro_Screen_Key]
    for thisComponent in Intro_ScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Intro_Screen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Intro_Screen_Text* updates
        
        # if Intro_Screen_Text is starting this frame...
        if Intro_Screen_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Intro_Screen_Text.frameNStart = frameN  # exact frame index
            Intro_Screen_Text.tStart = t  # local t and not account for scr refresh
            Intro_Screen_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Intro_Screen_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Intro_Screen_Text.started')
            # update status
            Intro_Screen_Text.status = STARTED
            Intro_Screen_Text.setAutoDraw(True)
        
        # if Intro_Screen_Text is active this frame...
        if Intro_Screen_Text.status == STARTED:
            # update params
            pass
        
        # *Intro_Screen_Key* updates
        waitOnFlip = False
        
        # if Intro_Screen_Key is starting this frame...
        if Intro_Screen_Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Intro_Screen_Key.frameNStart = frameN  # exact frame index
            Intro_Screen_Key.tStart = t  # local t and not account for scr refresh
            Intro_Screen_Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Intro_Screen_Key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Intro_Screen_Key.started')
            # update status
            Intro_Screen_Key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Intro_Screen_Key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Intro_Screen_Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Intro_Screen_Key.status == STARTED and not waitOnFlip:
            theseKeys = Intro_Screen_Key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Intro_Screen_Key_allKeys.extend(theseKeys)
            if len(_Intro_Screen_Key_allKeys):
                Intro_Screen_Key.keys = _Intro_Screen_Key_allKeys[-1].name  # just the last key pressed
                Intro_Screen_Key.rt = _Intro_Screen_Key_allKeys[-1].rt
                Intro_Screen_Key.duration = _Intro_Screen_Key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Intro_ScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Intro_Screen" ---
    for thisComponent in Intro_ScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Intro_Screen.stopped', globalClock.getTime(format='float'))
    # check responses
    if Intro_Screen_Key.keys in ['', [], None]:  # No response was made
        Intro_Screen_Key.keys = None
    thisExp.addData('Intro_Screen_Key.keys',Intro_Screen_Key.keys)
    if Intro_Screen_Key.keys != None:  # we had a response
        thisExp.addData('Intro_Screen_Key.rt', Intro_Screen_Key.rt)
        thisExp.addData('Intro_Screen_Key.duration', Intro_Screen_Key.duration)
    
    
    
    
    
    thisExp.nextEntry()
    # the Routine "Intro_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions.started', globalClock.getTime(format='float'))
    # create starting attributes for Instruction_Key
    Instruction_Key.keys = []
    Instruction_Key.rt = []
    _Instruction_Key_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [Instruction_Text, Instruction_Key]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instruction_Text* updates
        
        # if Instruction_Text is starting this frame...
        if Instruction_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_Text.frameNStart = frameN  # exact frame index
            Instruction_Text.tStart = t  # local t and not account for scr refresh
            Instruction_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction_Text.started')
            # update status
            Instruction_Text.status = STARTED
            Instruction_Text.setAutoDraw(True)
        
        # if Instruction_Text is active this frame...
        if Instruction_Text.status == STARTED:
            # update params
            pass
        
        # *Instruction_Key* updates
        waitOnFlip = False
        
        # if Instruction_Key is starting this frame...
        if Instruction_Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_Key.frameNStart = frameN  # exact frame index
            Instruction_Key.tStart = t  # local t and not account for scr refresh
            Instruction_Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_Key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction_Key.started')
            # update status
            Instruction_Key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instruction_Key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instruction_Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instruction_Key.status == STARTED and not waitOnFlip:
            theseKeys = Instruction_Key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Instruction_Key_allKeys.extend(theseKeys)
            if len(_Instruction_Key_allKeys):
                Instruction_Key.keys = _Instruction_Key_allKeys[-1].name  # just the last key pressed
                Instruction_Key.rt = _Instruction_Key_allKeys[-1].rt
                Instruction_Key.duration = _Instruction_Key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions.stopped', globalClock.getTime(format='float'))
    # check responses
    if Instruction_Key.keys in ['', [], None]:  # No response was made
        Instruction_Key.keys = None
    thisExp.addData('Instruction_Key.keys',Instruction_Key.keys)
    if Instruction_Key.keys != None:  # we had a response
        thisExp.addData('Instruction_Key.rt', Instruction_Key.rt)
        thisExp.addData('Instruction_Key.duration', Instruction_Key.duration)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Items_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Stimuli.xlsx'),
        seed=None, name='Items_Loop')
    thisExp.addLoop(Items_Loop)  # add the loop to the experiment
    thisItems_Loop = Items_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisItems_Loop.rgb)
    if thisItems_Loop != None:
        for paramName in thisItems_Loop:
            globals()[paramName] = thisItems_Loop[paramName]
    
    for thisItems_Loop in Items_Loop:
        currentLoop = Items_Loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisItems_Loop.rgb)
        if thisItems_Loop != None:
            for paramName in thisItems_Loop:
                globals()[paramName] = thisItems_Loop[paramName]
        
        # set up handler to look after randomisation of conditions etc
        Region_Loop = data.TrialHandler(nReps=16.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='Region_Loop')
        thisExp.addLoop(Region_Loop)  # add the loop to the experiment
        thisRegion_Loop = Region_Loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRegion_Loop.rgb)
        if thisRegion_Loop != None:
            for paramName in thisRegion_Loop:
                globals()[paramName] = thisRegion_Loop[paramName]
        
        for thisRegion_Loop in Region_Loop:
            currentLoop = Region_Loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisRegion_Loop.rgb)
            if thisRegion_Loop != None:
                for paramName in thisRegion_Loop:
                    globals()[paramName] = thisRegion_Loop[paramName]
            
            # --- Prepare to start Routine "Maze" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Maze.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from Error_Display_Code
            error_text_visibility = 0
            keys = []
            userChoice = "x"
            key1 = str(eval(Correct))
            key2 = str(eval(Incorrect))
            LeftText.setText(eval(LeftVar))
            RightText.setText(eval(RightVar))
            # create starting attributes for Response_key
            Response_key.keys = []
            Response_key.rt = []
            _Response_key_allKeys = []
            # keep track of which components have finished
            MazeComponents = [LeftText, RightText, Incorrect_Text, Response_key]
            for thisComponent in MazeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Maze" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *LeftText* updates
                
                # if LeftText is starting this frame...
                if LeftText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    LeftText.frameNStart = frameN  # exact frame index
                    LeftText.tStart = t  # local t and not account for scr refresh
                    LeftText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LeftText, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'LeftText.started')
                    # update status
                    LeftText.status = STARTED
                    LeftText.setAutoDraw(True)
                
                # if LeftText is active this frame...
                if LeftText.status == STARTED:
                    # update params
                    pass
                
                # *RightText* updates
                
                # if RightText is starting this frame...
                if RightText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RightText.frameNStart = frameN  # exact frame index
                    RightText.tStart = t  # local t and not account for scr refresh
                    RightText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RightText, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RightText.started')
                    # update status
                    RightText.status = STARTED
                    RightText.setAutoDraw(True)
                
                # if RightText is active this frame...
                if RightText.status == STARTED:
                    # update params
                    pass
                
                # *Incorrect_Text* updates
                
                # if Incorrect_Text is starting this frame...
                if Incorrect_Text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    Incorrect_Text.frameNStart = frameN  # exact frame index
                    Incorrect_Text.tStart = t  # local t and not account for scr refresh
                    Incorrect_Text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Incorrect_Text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Incorrect_Text.started')
                    # update status
                    Incorrect_Text.status = STARTED
                    Incorrect_Text.setAutoDraw(True)
                
                # if Incorrect_Text is active this frame...
                if Incorrect_Text.status == STARTED:
                    # update params
                    Incorrect_Text.setOpacity(error_text_visibility, log=False)
                
                # *Response_key* updates
                waitOnFlip = False
                
                # if Response_key is starting this frame...
                if Response_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Response_key.frameNStart = frameN  # exact frame index
                    Response_key.tStart = t  # local t and not account for scr refresh
                    Response_key.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Response_key, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Response_key.started')
                    # update status
                    Response_key.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Response_key.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Response_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Response_key.status == STARTED and not waitOnFlip:
                    theseKeys = Response_key.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                    _Response_key_allKeys.extend(theseKeys)
                    if len(_Response_key_allKeys):
                        Response_key.keys = _Response_key_allKeys[-1].name  # just the last key pressed
                        Response_key.rt = _Response_key_allKeys[-1].rt
                        Response_key.duration = _Response_key_allKeys[-1].duration
                        # was this correct?
                        if (Response_key.keys == str(eval(Correct))) or (Response_key.keys == eval(Correct)):
                            Response_key.corr = 1
                        else:
                            Response_key.corr = 0
                # Run 'Each Frame' code from Routine_End
                keys = event.getKeys()
                if len(keys) > 0:
                    userChoice = keys[-1]
                    if userChoice == key2:
                        error_text_visibility = 1
                    if userChoice == key1:
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in MazeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Maze" ---
            for thisComponent in MazeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Maze.stopped', globalClock.getTime(format='float'))
            # check responses
            if Response_key.keys in ['', [], None]:  # No response was made
                Response_key.keys = None
                # was no response the correct answer?!
                if str(eval(Correct)).lower() == 'none':
                   Response_key.corr = 1;  # correct non-response
                else:
                   Response_key.corr = 0;  # failed to respond (incorrectly)
            # store data for Region_Loop (TrialHandler)
            Region_Loop.addData('Response_key.keys',Response_key.keys)
            Region_Loop.addData('Response_key.corr', Response_key.corr)
            if Response_key.keys != None:  # we had a response
                Region_Loop.addData('Response_key.rt', Response_key.rt)
                Region_Loop.addData('Response_key.duration', Response_key.duration)
            # Run 'End Routine' code from Routine_End
            Region_Num += 1
            LeftVar ="r" + str(Region_Num) + "l"
            RightVar ="r" + str(Region_Num) + "r"
            Correct ="r" + str(Region_Num) + "corr"
            Incorrect = "r" + str(Region_Num) + "incorr"
            # the Routine "Maze" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 16.0 repeats of 'Region_Loop'
        
        
        # --- Prepare to start Routine "Comp_Screen" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Comp_Screen.started', globalClock.getTime(format='float'))
        # create starting attributes for Comp_Key
        Comp_Key.keys = []
        Comp_Key.rt = []
        _Comp_Key_allKeys = []
        Comprehension_Question.setText(Comp)
        # keep track of which components have finished
        Comp_ScreenComponents = [Comp_Key, Comprehension_Question, Comprehension_Answer_Choices]
        for thisComponent in Comp_ScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Comp_Screen" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Comp_Key* updates
            waitOnFlip = False
            
            # if Comp_Key is starting this frame...
            if Comp_Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Comp_Key.frameNStart = frameN  # exact frame index
                Comp_Key.tStart = t  # local t and not account for scr refresh
                Comp_Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Comp_Key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Comp_Key.started')
                # update status
                Comp_Key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Comp_Key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Comp_Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Comp_Key.status == STARTED and not waitOnFlip:
                theseKeys = Comp_Key.getKeys(keyList=['a', 'l'], ignoreKeys=["escape"], waitRelease=False)
                _Comp_Key_allKeys.extend(theseKeys)
                if len(_Comp_Key_allKeys):
                    Comp_Key.keys = _Comp_Key_allKeys[-1].name  # just the last key pressed
                    Comp_Key.rt = _Comp_Key_allKeys[-1].rt
                    Comp_Key.duration = _Comp_Key_allKeys[-1].duration
                    # was this correct?
                    if (Comp_Key.keys == str(CompAns)) or (Comp_Key.keys == CompAns):
                        Comp_Key.corr = 1
                    else:
                        Comp_Key.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *Comprehension_Question* updates
            
            # if Comprehension_Question is starting this frame...
            if Comprehension_Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Comprehension_Question.frameNStart = frameN  # exact frame index
                Comprehension_Question.tStart = t  # local t and not account for scr refresh
                Comprehension_Question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Comprehension_Question, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Comprehension_Question.started')
                # update status
                Comprehension_Question.status = STARTED
                Comprehension_Question.setAutoDraw(True)
            
            # if Comprehension_Question is active this frame...
            if Comprehension_Question.status == STARTED:
                # update params
                pass
            
            # *Comprehension_Answer_Choices* updates
            
            # if Comprehension_Answer_Choices is starting this frame...
            if Comprehension_Answer_Choices.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Comprehension_Answer_Choices.frameNStart = frameN  # exact frame index
                Comprehension_Answer_Choices.tStart = t  # local t and not account for scr refresh
                Comprehension_Answer_Choices.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Comprehension_Answer_Choices, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Comprehension_Answer_Choices.started')
                # update status
                Comprehension_Answer_Choices.status = STARTED
                Comprehension_Answer_Choices.setAutoDraw(True)
            
            # if Comprehension_Answer_Choices is active this frame...
            if Comprehension_Answer_Choices.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Comp_ScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Comp_Screen" ---
        for thisComponent in Comp_ScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Comp_Screen.stopped', globalClock.getTime(format='float'))
        # check responses
        if Comp_Key.keys in ['', [], None]:  # No response was made
            Comp_Key.keys = None
            # was no response the correct answer?!
            if str(CompAns).lower() == 'none':
               Comp_Key.corr = 1;  # correct non-response
            else:
               Comp_Key.corr = 0;  # failed to respond (incorrectly)
        # store data for Items_Loop (TrialHandler)
        Items_Loop.addData('Comp_Key.keys',Comp_Key.keys)
        Items_Loop.addData('Comp_Key.corr', Comp_Key.corr)
        if Comp_Key.keys != None:  # we had a response
            Items_Loop.addData('Comp_Key.rt', Comp_Key.rt)
            Items_Loop.addData('Comp_Key.duration', Comp_Key.duration)
        # Run 'End Routine' code from Reset_Code
        Region_Num = 0
        LeftVar ="r" + str(Region_Num) + "l"
        RightVar ="r" + str(Region_Num) + "r"
        Correct ="r" + str(Region_Num) + "corr"
        Incorrect = "r" + str(Region_Num) + "incorr"
        event.clearEvents(eventType='keyboard') 
        # the Routine "Comp_Screen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'Items_Loop'
    
    
    # --- Prepare to start Routine "Exit_Screen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Exit_Screen.started', globalClock.getTime(format='float'))
    # create starting attributes for Exit_Key
    Exit_Key.keys = []
    Exit_Key.rt = []
    _Exit_Key_allKeys = []
    # keep track of which components have finished
    Exit_ScreenComponents = [Exit_Text, Exit_Key]
    for thisComponent in Exit_ScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Exit_Screen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Exit_Text* updates
        
        # if Exit_Text is starting this frame...
        if Exit_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Exit_Text.frameNStart = frameN  # exact frame index
            Exit_Text.tStart = t  # local t and not account for scr refresh
            Exit_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Exit_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Exit_Text.started')
            # update status
            Exit_Text.status = STARTED
            Exit_Text.setAutoDraw(True)
        
        # if Exit_Text is active this frame...
        if Exit_Text.status == STARTED:
            # update params
            pass
        
        # *Exit_Key* updates
        waitOnFlip = False
        
        # if Exit_Key is starting this frame...
        if Exit_Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Exit_Key.frameNStart = frameN  # exact frame index
            Exit_Key.tStart = t  # local t and not account for scr refresh
            Exit_Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Exit_Key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Exit_Key.started')
            # update status
            Exit_Key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Exit_Key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Exit_Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Exit_Key.status == STARTED and not waitOnFlip:
            theseKeys = Exit_Key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Exit_Key_allKeys.extend(theseKeys)
            if len(_Exit_Key_allKeys):
                Exit_Key.keys = _Exit_Key_allKeys[-1].name  # just the last key pressed
                Exit_Key.rt = _Exit_Key_allKeys[-1].rt
                Exit_Key.duration = _Exit_Key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Exit_ScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Exit_Screen" ---
    for thisComponent in Exit_ScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Exit_Screen.stopped', globalClock.getTime(format='float'))
    # check responses
    if Exit_Key.keys in ['', [], None]:  # No response was made
        Exit_Key.keys = None
    thisExp.addData('Exit_Key.keys',Exit_Key.keys)
    if Exit_Key.keys != None:  # we had a response
        thisExp.addData('Exit_Key.rt', Exit_Key.rt)
        thisExp.addData('Exit_Key.duration', Exit_Key.duration)
    thisExp.nextEntry()
    # the Routine "Exit_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    
    
    
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)
    # end 'rush' mode
    core.rush(enable=False)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
