#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Wed Mar 11 14:39:59 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Passive Viewing'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/omarhernandez/Desktop/424_Experiment_Materials/passive_viewing_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "launch_scan"
launch_scanClock = core.Clock()
from psychopy.hardware.emulator import launchScan
scanner_settings = {
    'TR': 2.0,  # in seconds
    'volumes': 30,  # for emulator
    'sync': 't',
    'skip': 0,  # number of scans to omit before proceeding
    }
globalClock = core.Clock()



# Initialize components for Routine "Passive_Viewing"
Passive_ViewingClock = core.Clock()
Introduction = visual.TextStim(win=win, name='Introduction',
    text='\nWelcome!\n\nRelax and focus on the images\n \n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blockON"
blockONClock = core.Clock()

# Initialize components for Routine "SCRtool"
SCRtoolClock = core.Clock()
SCRtools = visual.ImageStim(
    win=win,
    name='SCRtools', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blockOFF"
blockOFFClock = core.Clock()

# Initialize components for Routine "pause"
pauseClock = core.Clock()
rest = visual.TextStim(win=win, name='rest',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blockON"
blockONClock = core.Clock()

# Initialize components for Routine "tool"
toolClock = core.Clock()
tools = visual.ImageStim(
    win=win,
    name='tools', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blockOFF"
blockOFFClock = core.Clock()

# Initialize components for Routine "pause"
pauseClock = core.Clock()
rest = visual.TextStim(win=win, name='rest',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blockON"
blockONClock = core.Clock()

# Initialize components for Routine "SCRshape"
SCRshapeClock = core.Clock()
SCRshapes = visual.ImageStim(
    win=win,
    name='SCRshapes', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blockOFF"
blockOFFClock = core.Clock()

# Initialize components for Routine "pause"
pauseClock = core.Clock()
rest = visual.TextStim(win=win, name='rest',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blockON"
blockONClock = core.Clock()

# Initialize components for Routine "shape"
shapeClock = core.Clock()
shapes = visual.ImageStim(
    win=win,
    name='shapes', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blockOFF"
blockOFFClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "launch_scan"-------
# update component parameters for each repeat
# keep track of which components have finished
launch_scanComponents = []
for thisComponent in launch_scanComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
launch_scanClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "launch_scan"-------
while continueRoutine:
    # get current time
    t = launch_scanClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=launch_scanClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in launch_scanComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "launch_scan"-------
for thisComponent in launch_scanComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
vol = launchScan(win, scanner_settings, globalClock=globalClock, mode='Scan')
 
pulsetime = globalClock.getTime()
thisExp.addData('pulsetime',pulsetime)
thisExp.nextEntry()
# the Routine "launch_scan" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Passive_Viewing"-------
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Passive_ViewingComponents = [Introduction]
for thisComponent in Passive_ViewingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Passive_ViewingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Passive_Viewing"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Passive_ViewingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Passive_ViewingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Introduction* updates
    if Introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Introduction.frameNStart = frameN  # exact frame index
        Introduction.tStart = t  # local t and not account for scr refresh
        Introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Introduction, 'tStartRefresh')  # time at next scr refresh
        Introduction.setAutoDraw(True)
    if Introduction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Introduction.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            Introduction.tStop = t  # not accounting for scr refresh
            Introduction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Introduction, 'tStopRefresh')  # time at next scr refresh
            Introduction.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Passive_ViewingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Passive_Viewing"-------
for thisComponent in Passive_ViewingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Introduction.started', Introduction.tStartRefresh)
thisExp.addData('Introduction.stopped', Introduction.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "blockON"-------
    # update component parameters for each repeat
    stimON = globalClock.getTime()
    thisExp.addData('stimON',stimON)
    # keep track of which components have finished
    blockONComponents = []
    for thisComponent in blockONComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockONClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "blockON"-------
    while continueRoutine:
        # get current time
        t = blockONClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockONClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockONComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockON"-------
    for thisComponent in blockONComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blockON" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('CSV stimuli/SCRtool.csv.xlsx', selection=random(8)*9),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "SCRtool"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        SCRtools.setImage(imagefile)
        # keep track of which components have finished
        SCRtoolComponents = [SCRtools]
        for thisComponent in SCRtoolComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        SCRtoolClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "SCRtool"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = SCRtoolClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=SCRtoolClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *SCRtools* updates
            if SCRtools.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SCRtools.frameNStart = frameN  # exact frame index
                SCRtools.tStart = t  # local t and not account for scr refresh
                SCRtools.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SCRtools, 'tStartRefresh')  # time at next scr refresh
                SCRtools.setAutoDraw(True)
            if SCRtools.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SCRtools.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    SCRtools.tStop = t  # not accounting for scr refresh
                    SCRtools.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SCRtools, 'tStopRefresh')  # time at next scr refresh
                    SCRtools.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SCRtoolComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "SCRtool"-------
        for thisComponent in SCRtoolComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('SCRtools.started', SCRtools.tStartRefresh)
        trials.addData('SCRtools.stopped', SCRtools.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "blockOFF"-------
    # update component parameters for each repeat
    stimOFF = globalClock.getTime()
    thisExp.addData('dur',stimOFF-stimON)
    # keep track of which components have finished
    blockOFFComponents = []
    for thisComponent in blockOFFComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockOFFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "blockOFF"-------
    while continueRoutine:
        # get current time
        t = blockOFFClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockOFFClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockOFFComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockOFF"-------
    for thisComponent in blockOFFComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blockOFF" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pause"-------
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pauseComponents = [rest]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest* updates
        if rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest.frameNStart = frameN  # exact frame index
            rest.tStart = t  # local t and not account for scr refresh
            rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest, 'tStartRefresh')  # time at next scr refresh
            rest.setAutoDraw(True)
        if rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                rest.tStop = t  # not accounting for scr refresh
                rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest, 'tStopRefresh')  # time at next scr refresh
                rest.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('rest.started', rest.tStartRefresh)
    trials_5.addData('rest.stopped', rest.tStopRefresh)
    
    # ------Prepare to start Routine "blockON"-------
    # update component parameters for each repeat
    stimON = globalClock.getTime()
    thisExp.addData('stimON',stimON)
    # keep track of which components have finished
    blockONComponents = []
    for thisComponent in blockONComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockONClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "blockON"-------
    while continueRoutine:
        # get current time
        t = blockONClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockONClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockONComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockON"-------
    for thisComponent in blockONComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blockON" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('CSV stimuli/tools.csv.xlsx', selection=random(8)*9),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "tool"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        tools.setImage(imagefile)
        # keep track of which components have finished
        toolComponents = [tools]
        for thisComponent in toolComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        toolClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "tool"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = toolClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=toolClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tools* updates
            if tools.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tools.frameNStart = frameN  # exact frame index
                tools.tStart = t  # local t and not account for scr refresh
                tools.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tools, 'tStartRefresh')  # time at next scr refresh
                tools.setAutoDraw(True)
            if tools.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tools.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    tools.tStop = t  # not accounting for scr refresh
                    tools.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tools, 'tStopRefresh')  # time at next scr refresh
                    tools.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in toolComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "tool"-------
        for thisComponent in toolComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('tools.started', tools.tStartRefresh)
        trials_2.addData('tools.stopped', tools.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    
    # ------Prepare to start Routine "blockOFF"-------
    # update component parameters for each repeat
    stimOFF = globalClock.getTime()
    thisExp.addData('dur',stimOFF-stimON)
    # keep track of which components have finished
    blockOFFComponents = []
    for thisComponent in blockOFFComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockOFFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "blockOFF"-------
    while continueRoutine:
        # get current time
        t = blockOFFClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockOFFClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockOFFComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockOFF"-------
    for thisComponent in blockOFFComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blockOFF" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pause"-------
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pauseComponents = [rest]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest* updates
        if rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest.frameNStart = frameN  # exact frame index
            rest.tStart = t  # local t and not account for scr refresh
            rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest, 'tStartRefresh')  # time at next scr refresh
            rest.setAutoDraw(True)
        if rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                rest.tStop = t  # not accounting for scr refresh
                rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest, 'tStopRefresh')  # time at next scr refresh
                rest.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('rest.started', rest.tStartRefresh)
    trials_5.addData('rest.stopped', rest.tStopRefresh)
    
    # ------Prepare to start Routine "blockON"-------
    # update component parameters for each repeat
    stimON = globalClock.getTime()
    thisExp.addData('stimON',stimON)
    # keep track of which components have finished
    blockONComponents = []
    for thisComponent in blockONComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockONClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "blockON"-------
    while continueRoutine:
        # get current time
        t = blockONClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockONClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockONComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockON"-------
    for thisComponent in blockONComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blockON" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('CSV stimuli/SCRshapes.csv.xlsx', selection=random(8)*9),
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "SCRshape"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        SCRshapes.setImage(imagefile)
        # keep track of which components have finished
        SCRshapeComponents = [SCRshapes]
        for thisComponent in SCRshapeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        SCRshapeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "SCRshape"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = SCRshapeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=SCRshapeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *SCRshapes* updates
            if SCRshapes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SCRshapes.frameNStart = frameN  # exact frame index
                SCRshapes.tStart = t  # local t and not account for scr refresh
                SCRshapes.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SCRshapes, 'tStartRefresh')  # time at next scr refresh
                SCRshapes.setAutoDraw(True)
            if SCRshapes.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SCRshapes.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    SCRshapes.tStop = t  # not accounting for scr refresh
                    SCRshapes.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SCRshapes, 'tStopRefresh')  # time at next scr refresh
                    SCRshapes.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SCRshapeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "SCRshape"-------
        for thisComponent in SCRshapeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_3.addData('SCRshapes.started', SCRshapes.tStartRefresh)
        trials_3.addData('SCRshapes.stopped', SCRshapes.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_3'
    
    
    # ------Prepare to start Routine "blockOFF"-------
    # update component parameters for each repeat
    stimOFF = globalClock.getTime()
    thisExp.addData('dur',stimOFF-stimON)
    # keep track of which components have finished
    blockOFFComponents = []
    for thisComponent in blockOFFComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockOFFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "blockOFF"-------
    while continueRoutine:
        # get current time
        t = blockOFFClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockOFFClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockOFFComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockOFF"-------
    for thisComponent in blockOFFComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blockOFF" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pause"-------
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pauseComponents = [rest]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest* updates
        if rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest.frameNStart = frameN  # exact frame index
            rest.tStart = t  # local t and not account for scr refresh
            rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest, 'tStartRefresh')  # time at next scr refresh
            rest.setAutoDraw(True)
        if rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                rest.tStop = t  # not accounting for scr refresh
                rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest, 'tStopRefresh')  # time at next scr refresh
                rest.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('rest.started', rest.tStartRefresh)
    trials_5.addData('rest.stopped', rest.tStopRefresh)
    
    # ------Prepare to start Routine "blockON"-------
    # update component parameters for each repeat
    stimON = globalClock.getTime()
    thisExp.addData('stimON',stimON)
    # keep track of which components have finished
    blockONComponents = []
    for thisComponent in blockONComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockONClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "blockON"-------
    while continueRoutine:
        # get current time
        t = blockONClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockONClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockONComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockON"-------
    for thisComponent in blockONComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blockON" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('CSV stimuli/shape.csv.xlsx', selection=random(8)*9),
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "shape"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        shapes.setImage(imagefile)
        # keep track of which components have finished
        shapeComponents = [shapes]
        for thisComponent in shapeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        shapeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "shape"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = shapeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=shapeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *shapes* updates
            if shapes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                shapes.frameNStart = frameN  # exact frame index
                shapes.tStart = t  # local t and not account for scr refresh
                shapes.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(shapes, 'tStartRefresh')  # time at next scr refresh
                shapes.setAutoDraw(True)
            if shapes.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > shapes.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    shapes.tStop = t  # not accounting for scr refresh
                    shapes.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(shapes, 'tStopRefresh')  # time at next scr refresh
                    shapes.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in shapeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "shape"-------
        for thisComponent in shapeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_4.addData('shapes.started', shapes.tStartRefresh)
        trials_4.addData('shapes.stopped', shapes.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_4'
    
# completed 5 repeats of 'trials_5'


# ------Prepare to start Routine "blockOFF"-------
# update component parameters for each repeat
stimOFF = globalClock.getTime()
thisExp.addData('dur',stimOFF-stimON)
# keep track of which components have finished
blockOFFComponents = []
for thisComponent in blockOFFComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blockOFFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "blockOFF"-------
while continueRoutine:
    # get current time
    t = blockOFFClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blockOFFClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockOFFComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blockOFF"-------
for thisComponent in blockOFFComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "blockOFF" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
