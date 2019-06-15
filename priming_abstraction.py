#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.0),
    on Sat Jun 15 17:35:46 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
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
psychopyVersion = '3.1.0'
expName = 'priming_almost'  # from the Builder filename that created this script
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
    originPath='/Users/po/Documents/lindy_exp/priming_almost3.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

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

# Initialize components for Routine "guide"
guideClock = core.Clock()
expl = visual.TextStim(win=win, name='expl',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "title"
titleClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "priming"
primingClock = core.Clock()
mask = visual.TextStim(win=win, name='mask',
    text='###########',
    font='Arial',
    pos=(0, 0), height=0.13, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
prime = visual.TextStim(win=win, name='prime',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
target = visual.TextStim(win=win, name='target',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "exp"
expClock = core.Clock()
text5 = visual.TextStim(win=win, name='text5',
    text='Эксперимент\nБлок 1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "priming"
primingClock = core.Clock()
mask = visual.TextStim(win=win, name='mask',
    text='###########',
    font='Arial',
    pos=(0, 0), height=0.13, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
prime = visual.TextStim(win=win, name='prime',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
target = visual.TextStim(win=win, name='target',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "exp2"
exp2Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Блок 2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "priming"
primingClock = core.Clock()
mask = visual.TextStim(win=win, name='mask',
    text='###########',
    font='Arial',
    pos=(0, 0), height=0.13, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
prime = visual.TextStim(win=win, name='prime',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
target = visual.TextStim(win=win, name='target',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "exp3"
exp3Clock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Блок 3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "priming"
primingClock = core.Clock()
mask = visual.TextStim(win=win, name='mask',
    text='###########',
    font='Arial',
    pos=(0, 0), height=0.13, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
prime = visual.TextStim(win=win, name='prime',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
target = visual.TextStim(win=win, name='target',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "exp4"
exp4Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Блок 4',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "priming"
primingClock = core.Clock()
mask = visual.TextStim(win=win, name='mask',
    text='###########',
    font='Arial',
    pos=(0, 0), height=0.13, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
prime = visual.TextStim(win=win, name='prime',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
target = visual.TextStim(win=win, name='target',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "fin"
finClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Эксперимент окончен.\nБольшое спасибо!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
guide_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('guide_loop.xlsx'),
    seed=None, name='guide_loop')
thisExp.addLoop(guide_loop)  # add the loop to the experiment
thisGuide_loop = guide_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGuide_loop.rgb)
if thisGuide_loop != None:
    for paramName in thisGuide_loop:
        exec('{} = thisGuide_loop[paramName]'.format(paramName))

for thisGuide_loop in guide_loop:
    currentLoop = guide_loop
    # abbreviate parameter names if possible (e.g. rgb = thisGuide_loop.rgb)
    if thisGuide_loop != None:
        for paramName in thisGuide_loop:
            exec('{} = thisGuide_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "guide"-------
    t = 0
    guideClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    expl.setText(explanation)
    key_resp_6 = keyboard.Keyboard()
    # keep track of which components have finished
    guideComponents = [expl, key_resp_6]
    for thisComponent in guideComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "guide"-------
    while continueRoutine:
        # get current time
        t = guideClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *expl* updates
        if t >= 0.0 and expl.status == NOT_STARTED:
            # keep track of start time/frame for later
            expl.tStart = t  # not accounting for scr refresh
            expl.frameNStart = frameN  # exact frame index
            win.timeOnFlip(expl, 'tStartRefresh')  # time at next scr refresh
            expl.setAutoDraw(True)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t  # not accounting for scr refresh
            key_resp_6.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            key_resp_6.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in guideComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "guide"-------
    for thisComponent in guideComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    guide_loop.addData('expl.started', expl.tStartRefresh)
    guide_loop.addData('expl.stopped', expl.tStopRefresh)
    # the Routine "guide" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'guide_loop'


# ------Prepare to start Routine "title"-------
t = 0
titleClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
text_5.setText('Тренировка')
key_resp_4 = keyboard.Keyboard()
# keep track of which components have finished
titleComponents = [text_5, key_resp_4]
for thisComponent in titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "title"-------
while continueRoutine:
    # get current time
    t = titleClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # not accounting for scr refresh
        text_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # not accounting for scr refresh
        key_resp_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "title"-------
for thisComponent in titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# the Routine "title" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_loop.xlsx'),
    seed=None, name='trial_loop')
thisExp.addLoop(trial_loop)  # add the loop to the experiment
thisTrial_loop = trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
if thisTrial_loop != None:
    for paramName in thisTrial_loop:
        exec('{} = thisTrial_loop[paramName]'.format(paramName))

for thisTrial_loop in trial_loop:
    currentLoop = trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
    if thisTrial_loop != None:
        for paramName in thisTrial_loop:
            exec('{} = thisTrial_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "priming"-------
    t = 0
    primingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    prime.setText(prime_var)
    key_resp_10 = keyboard.Keyboard()
    target.setText(stim_var)
    # keep track of which components have finished
    primingComponents = [mask, prime, key_resp_10, target]
    for thisComponent in primingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "priming"-------
    while continueRoutine:
        # get current time
        t = primingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mask* updates
        if frameN >= 30 and mask.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask.tStart = t  # not accounting for scr refresh
            mask.frameNStart = frameN  # exact frame index
            win.timeOnFlip(mask, 'tStartRefresh')  # time at next scr refresh
            mask.setAutoDraw(True)
        if mask.status == STARTED and frameN >= 60:
            # keep track of stop time/frame for later
            mask.tStop = t  # not accounting for scr refresh
            mask.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mask, 'tStopRefresh')  # time at next scr refresh
            mask.setAutoDraw(False)
        
        # *prime* updates
        if frameN >= 60 and prime.status == NOT_STARTED:
            # keep track of start time/frame for later
            prime.tStart = t  # not accounting for scr refresh
            prime.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prime, 'tStartRefresh')  # time at next scr refresh
            prime.setAutoDraw(True)
        if prime.status == STARTED and frameN >= 63:
            # keep track of stop time/frame for later
            prime.tStop = t  # not accounting for scr refresh
            prime.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prime, 'tStopRefresh')  # time at next scr refresh
            prime.setAutoDraw(False)
        
        # *key_resp_10* updates
        if frameN >= 63 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t  # not accounting for scr refresh
            key_resp_10.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            key_resp_10.clearEvents(eventType='keyboard')
        if key_resp_10.status == STARTED:
            theseKeys = key_resp_10.getKeys(keyList=['f', 'j'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_10.keys = theseKeys.name  # just the last key pressed
                key_resp_10.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp_10.keys == str(correctAns)) or (key_resp_10.keys == correctAns):
                    key_resp_10.corr = 1
                else:
                    key_resp_10.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *target* updates
        if frameN >= 63.0 and target.status == NOT_STARTED:
            # keep track of start time/frame for later
            target.tStart = t  # not accounting for scr refresh
            target.frameNStart = frameN  # exact frame index
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED and frameN >= 93.0:
            # keep track of stop time/frame for later
            target.tStop = t  # not accounting for scr refresh
            target.frameNStop = frameN  # exact frame index
            win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
            target.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in primingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "priming"-------
    for thisComponent in primingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_loop.addData('mask.started', mask.tStartRefresh)
    trial_loop.addData('mask.stopped', mask.tStopRefresh)
    trial_loop.addData('prime.started', prime.tStartRefresh)
    trial_loop.addData('prime.stopped', prime.tStopRefresh)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           key_resp_10.corr = 1;  # correct non-response
        else:
           key_resp_10.corr = 0;  # failed to respond (incorrectly)
    # store data for trial_loop (TrialHandler)
    trial_loop.addData('key_resp_10.keys',key_resp_10.keys)
    trial_loop.addData('key_resp_10.corr', key_resp_10.corr)
    if key_resp_10.keys != None:  # we had a response
        trial_loop.addData('key_resp_10.rt', key_resp_10.rt)
    trial_loop.addData('key_resp_10.started', key_resp_10.tStartRefresh)
    trial_loop.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
    trial_loop.addData('target.started', target.tStartRefresh)
    trial_loop.addData('target.stopped', target.tStopRefresh)
    # the Routine "priming" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trial_loop'


# ------Prepare to start Routine "exp"-------
t = 0
expClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = keyboard.Keyboard()
# keep track of which components have finished
expComponents = [text5, key_resp_5]
for thisComponent in expComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "exp"-------
while continueRoutine:
    # get current time
    t = expClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text5* updates
    if t >= 0.0 and text5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text5.tStart = t  # not accounting for scr refresh
        text5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text5, 'tStartRefresh')  # time at next scr refresh
        text5.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # not accounting for scr refresh
        key_resp_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
    if key_resp_5.status == STARTED:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in expComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exp"-------
for thisComponent in expComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text5.started', text5.tStartRefresh)
thisExp.addData('text5.stopped', text5.tStopRefresh)
# the Routine "exp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
first_session = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loop1.xlsx'),
    seed=None, name='first_session')
thisExp.addLoop(first_session)  # add the loop to the experiment
thisFirst_session = first_session.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFirst_session.rgb)
if thisFirst_session != None:
    for paramName in thisFirst_session:
        exec('{} = thisFirst_session[paramName]'.format(paramName))

for thisFirst_session in first_session:
    currentLoop = first_session
    # abbreviate parameter names if possible (e.g. rgb = thisFirst_session.rgb)
    if thisFirst_session != None:
        for paramName in thisFirst_session:
            exec('{} = thisFirst_session[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "priming"-------
    t = 0
    primingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    prime.setText(prime_var)
    key_resp_10 = keyboard.Keyboard()
    target.setText(stim_var)
    # keep track of which components have finished
    primingComponents = [mask, prime, key_resp_10, target]
    for thisComponent in primingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "priming"-------
    while continueRoutine:
        # get current time
        t = primingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mask* updates
        if frameN >= 30 and mask.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask.tStart = t  # not accounting for scr refresh
            mask.frameNStart = frameN  # exact frame index
            win.timeOnFlip(mask, 'tStartRefresh')  # time at next scr refresh
            mask.setAutoDraw(True)
        if mask.status == STARTED and frameN >= 60:
            # keep track of stop time/frame for later
            mask.tStop = t  # not accounting for scr refresh
            mask.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mask, 'tStopRefresh')  # time at next scr refresh
            mask.setAutoDraw(False)
        
        # *prime* updates
        if frameN >= 60 and prime.status == NOT_STARTED:
            # keep track of start time/frame for later
            prime.tStart = t  # not accounting for scr refresh
            prime.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prime, 'tStartRefresh')  # time at next scr refresh
            prime.setAutoDraw(True)
        if prime.status == STARTED and frameN >= 63:
            # keep track of stop time/frame for later
            prime.tStop = t  # not accounting for scr refresh
            prime.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prime, 'tStopRefresh')  # time at next scr refresh
            prime.setAutoDraw(False)
        
        # *key_resp_10* updates
        if frameN >= 63 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t  # not accounting for scr refresh
            key_resp_10.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            key_resp_10.clearEvents(eventType='keyboard')
        if key_resp_10.status == STARTED:
            theseKeys = key_resp_10.getKeys(keyList=['f', 'j'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_10.keys = theseKeys.name  # just the last key pressed
                key_resp_10.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp_10.keys == str(correctAns)) or (key_resp_10.keys == correctAns):
                    key_resp_10.corr = 1
                else:
                    key_resp_10.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *target* updates
        if frameN >= 63.0 and target.status == NOT_STARTED:
            # keep track of start time/frame for later
            target.tStart = t  # not accounting for scr refresh
            target.frameNStart = frameN  # exact frame index
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED and frameN >= 93.0:
            # keep track of stop time/frame for later
            target.tStop = t  # not accounting for scr refresh
            target.frameNStop = frameN  # exact frame index
            win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
            target.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in primingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "priming"-------
    for thisComponent in primingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    first_session.addData('mask.started', mask.tStartRefresh)
    first_session.addData('mask.stopped', mask.tStopRefresh)
    first_session.addData('prime.started', prime.tStartRefresh)
    first_session.addData('prime.stopped', prime.tStopRefresh)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           key_resp_10.corr = 1;  # correct non-response
        else:
           key_resp_10.corr = 0;  # failed to respond (incorrectly)
    # store data for first_session (TrialHandler)
    first_session.addData('key_resp_10.keys',key_resp_10.keys)
    first_session.addData('key_resp_10.corr', key_resp_10.corr)
    if key_resp_10.keys != None:  # we had a response
        first_session.addData('key_resp_10.rt', key_resp_10.rt)
    first_session.addData('key_resp_10.started', key_resp_10.tStartRefresh)
    first_session.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
    first_session.addData('target.started', target.tStartRefresh)
    first_session.addData('target.stopped', target.tStopRefresh)
    # the Routine "priming" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'first_session'


# ------Prepare to start Routine "exp2"-------
t = 0
exp2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = keyboard.Keyboard()
# keep track of which components have finished
exp2Components = [text_3, key_resp_7]
for thisComponent in exp2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "exp2"-------
while continueRoutine:
    # get current time
    t = exp2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # not accounting for scr refresh
        text_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # not accounting for scr refresh
        key_resp_7.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        key_resp_7.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exp2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exp2"-------
for thisComponent in exp2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "exp2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
sec_session = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loop2.xlsx'),
    seed=None, name='sec_session')
thisExp.addLoop(sec_session)  # add the loop to the experiment
thisSec_session = sec_session.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSec_session.rgb)
if thisSec_session != None:
    for paramName in thisSec_session:
        exec('{} = thisSec_session[paramName]'.format(paramName))

for thisSec_session in sec_session:
    currentLoop = sec_session
    # abbreviate parameter names if possible (e.g. rgb = thisSec_session.rgb)
    if thisSec_session != None:
        for paramName in thisSec_session:
            exec('{} = thisSec_session[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "priming"-------
    t = 0
    primingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    prime.setText(prime_var)
    key_resp_10 = keyboard.Keyboard()
    target.setText(stim_var)
    # keep track of which components have finished
    primingComponents = [mask, prime, key_resp_10, target]
    for thisComponent in primingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "priming"-------
    while continueRoutine:
        # get current time
        t = primingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mask* updates
        if frameN >= 30 and mask.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask.tStart = t  # not accounting for scr refresh
            mask.frameNStart = frameN  # exact frame index
            win.timeOnFlip(mask, 'tStartRefresh')  # time at next scr refresh
            mask.setAutoDraw(True)
        if mask.status == STARTED and frameN >= 60:
            # keep track of stop time/frame for later
            mask.tStop = t  # not accounting for scr refresh
            mask.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mask, 'tStopRefresh')  # time at next scr refresh
            mask.setAutoDraw(False)
        
        # *prime* updates
        if frameN >= 60 and prime.status == NOT_STARTED:
            # keep track of start time/frame for later
            prime.tStart = t  # not accounting for scr refresh
            prime.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prime, 'tStartRefresh')  # time at next scr refresh
            prime.setAutoDraw(True)
        if prime.status == STARTED and frameN >= 63:
            # keep track of stop time/frame for later
            prime.tStop = t  # not accounting for scr refresh
            prime.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prime, 'tStopRefresh')  # time at next scr refresh
            prime.setAutoDraw(False)
        
        # *key_resp_10* updates
        if frameN >= 63 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t  # not accounting for scr refresh
            key_resp_10.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            key_resp_10.clearEvents(eventType='keyboard')
        if key_resp_10.status == STARTED:
            theseKeys = key_resp_10.getKeys(keyList=['f', 'j'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_10.keys = theseKeys.name  # just the last key pressed
                key_resp_10.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp_10.keys == str(correctAns)) or (key_resp_10.keys == correctAns):
                    key_resp_10.corr = 1
                else:
                    key_resp_10.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *target* updates
        if frameN >= 63.0 and target.status == NOT_STARTED:
            # keep track of start time/frame for later
            target.tStart = t  # not accounting for scr refresh
            target.frameNStart = frameN  # exact frame index
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED and frameN >= 93.0:
            # keep track of stop time/frame for later
            target.tStop = t  # not accounting for scr refresh
            target.frameNStop = frameN  # exact frame index
            win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
            target.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in primingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "priming"-------
    for thisComponent in primingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sec_session.addData('mask.started', mask.tStartRefresh)
    sec_session.addData('mask.stopped', mask.tStopRefresh)
    sec_session.addData('prime.started', prime.tStartRefresh)
    sec_session.addData('prime.stopped', prime.tStopRefresh)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           key_resp_10.corr = 1;  # correct non-response
        else:
           key_resp_10.corr = 0;  # failed to respond (incorrectly)
    # store data for sec_session (TrialHandler)
    sec_session.addData('key_resp_10.keys',key_resp_10.keys)
    sec_session.addData('key_resp_10.corr', key_resp_10.corr)
    if key_resp_10.keys != None:  # we had a response
        sec_session.addData('key_resp_10.rt', key_resp_10.rt)
    sec_session.addData('key_resp_10.started', key_resp_10.tStartRefresh)
    sec_session.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
    sec_session.addData('target.started', target.tStartRefresh)
    sec_session.addData('target.stopped', target.tStopRefresh)
    # the Routine "priming" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'sec_session'


# ------Prepare to start Routine "exp3"-------
t = 0
exp3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = keyboard.Keyboard()
# keep track of which components have finished
exp3Components = [text_7, key_resp_8]
for thisComponent in exp3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "exp3"-------
while continueRoutine:
    # get current time
    t = exp3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # not accounting for scr refresh
        text_7.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t  # not accounting for scr refresh
        key_resp_8.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        key_resp_8.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exp3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exp3"-------
for thisComponent in exp3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# the Routine "exp3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
thir_session = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loop3.xlsx'),
    seed=None, name='thir_session')
thisExp.addLoop(thir_session)  # add the loop to the experiment
thisThir_session = thir_session.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisThir_session.rgb)
if thisThir_session != None:
    for paramName in thisThir_session:
        exec('{} = thisThir_session[paramName]'.format(paramName))

for thisThir_session in thir_session:
    currentLoop = thir_session
    # abbreviate parameter names if possible (e.g. rgb = thisThir_session.rgb)
    if thisThir_session != None:
        for paramName in thisThir_session:
            exec('{} = thisThir_session[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "priming"-------
    t = 0
    primingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    prime.setText(prime_var)
    key_resp_10 = keyboard.Keyboard()
    target.setText(stim_var)
    # keep track of which components have finished
    primingComponents = [mask, prime, key_resp_10, target]
    for thisComponent in primingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "priming"-------
    while continueRoutine:
        # get current time
        t = primingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mask* updates
        if frameN >= 30 and mask.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask.tStart = t  # not accounting for scr refresh
            mask.frameNStart = frameN  # exact frame index
            win.timeOnFlip(mask, 'tStartRefresh')  # time at next scr refresh
            mask.setAutoDraw(True)
        if mask.status == STARTED and frameN >= 60:
            # keep track of stop time/frame for later
            mask.tStop = t  # not accounting for scr refresh
            mask.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mask, 'tStopRefresh')  # time at next scr refresh
            mask.setAutoDraw(False)
        
        # *prime* updates
        if frameN >= 60 and prime.status == NOT_STARTED:
            # keep track of start time/frame for later
            prime.tStart = t  # not accounting for scr refresh
            prime.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prime, 'tStartRefresh')  # time at next scr refresh
            prime.setAutoDraw(True)
        if prime.status == STARTED and frameN >= 63:
            # keep track of stop time/frame for later
            prime.tStop = t  # not accounting for scr refresh
            prime.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prime, 'tStopRefresh')  # time at next scr refresh
            prime.setAutoDraw(False)
        
        # *key_resp_10* updates
        if frameN >= 63 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t  # not accounting for scr refresh
            key_resp_10.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            key_resp_10.clearEvents(eventType='keyboard')
        if key_resp_10.status == STARTED:
            theseKeys = key_resp_10.getKeys(keyList=['f', 'j'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_10.keys = theseKeys.name  # just the last key pressed
                key_resp_10.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp_10.keys == str(correctAns)) or (key_resp_10.keys == correctAns):
                    key_resp_10.corr = 1
                else:
                    key_resp_10.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *target* updates
        if frameN >= 63.0 and target.status == NOT_STARTED:
            # keep track of start time/frame for later
            target.tStart = t  # not accounting for scr refresh
            target.frameNStart = frameN  # exact frame index
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED and frameN >= 93.0:
            # keep track of stop time/frame for later
            target.tStop = t  # not accounting for scr refresh
            target.frameNStop = frameN  # exact frame index
            win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
            target.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in primingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "priming"-------
    for thisComponent in primingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thir_session.addData('mask.started', mask.tStartRefresh)
    thir_session.addData('mask.stopped', mask.tStopRefresh)
    thir_session.addData('prime.started', prime.tStartRefresh)
    thir_session.addData('prime.stopped', prime.tStopRefresh)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           key_resp_10.corr = 1;  # correct non-response
        else:
           key_resp_10.corr = 0;  # failed to respond (incorrectly)
    # store data for thir_session (TrialHandler)
    thir_session.addData('key_resp_10.keys',key_resp_10.keys)
    thir_session.addData('key_resp_10.corr', key_resp_10.corr)
    if key_resp_10.keys != None:  # we had a response
        thir_session.addData('key_resp_10.rt', key_resp_10.rt)
    thir_session.addData('key_resp_10.started', key_resp_10.tStartRefresh)
    thir_session.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
    thir_session.addData('target.started', target.tStartRefresh)
    thir_session.addData('target.stopped', target.tStopRefresh)
    # the Routine "priming" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'thir_session'


# ------Prepare to start Routine "exp4"-------
t = 0
exp4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = keyboard.Keyboard()
# keep track of which components have finished
exp4Components = [text_8, key_resp_9]
for thisComponent in exp4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "exp4"-------
while continueRoutine:
    # get current time
    t = exp4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t  # not accounting for scr refresh
        text_8.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t  # not accounting for scr refresh
        key_resp_9.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        key_resp_9.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exp4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exp4"-------
for thisComponent in exp4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# the Routine "exp4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
forth_session = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loop4.xlsx'),
    seed=None, name='forth_session')
thisExp.addLoop(forth_session)  # add the loop to the experiment
thisForth_session = forth_session.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisForth_session.rgb)
if thisForth_session != None:
    for paramName in thisForth_session:
        exec('{} = thisForth_session[paramName]'.format(paramName))

for thisForth_session in forth_session:
    currentLoop = forth_session
    # abbreviate parameter names if possible (e.g. rgb = thisForth_session.rgb)
    if thisForth_session != None:
        for paramName in thisForth_session:
            exec('{} = thisForth_session[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "priming"-------
    t = 0
    primingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    prime.setText(prime_var)
    key_resp_10 = keyboard.Keyboard()
    target.setText(stim_var)
    # keep track of which components have finished
    primingComponents = [mask, prime, key_resp_10, target]
    for thisComponent in primingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "priming"-------
    while continueRoutine:
        # get current time
        t = primingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mask* updates
        if frameN >= 30 and mask.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask.tStart = t  # not accounting for scr refresh
            mask.frameNStart = frameN  # exact frame index
            win.timeOnFlip(mask, 'tStartRefresh')  # time at next scr refresh
            mask.setAutoDraw(True)
        if mask.status == STARTED and frameN >= 60:
            # keep track of stop time/frame for later
            mask.tStop = t  # not accounting for scr refresh
            mask.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mask, 'tStopRefresh')  # time at next scr refresh
            mask.setAutoDraw(False)
        
        # *prime* updates
        if frameN >= 60 and prime.status == NOT_STARTED:
            # keep track of start time/frame for later
            prime.tStart = t  # not accounting for scr refresh
            prime.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prime, 'tStartRefresh')  # time at next scr refresh
            prime.setAutoDraw(True)
        if prime.status == STARTED and frameN >= 63:
            # keep track of stop time/frame for later
            prime.tStop = t  # not accounting for scr refresh
            prime.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prime, 'tStopRefresh')  # time at next scr refresh
            prime.setAutoDraw(False)
        
        # *key_resp_10* updates
        if frameN >= 63 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t  # not accounting for scr refresh
            key_resp_10.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            key_resp_10.clearEvents(eventType='keyboard')
        if key_resp_10.status == STARTED:
            theseKeys = key_resp_10.getKeys(keyList=['f', 'j'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_10.keys = theseKeys.name  # just the last key pressed
                key_resp_10.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp_10.keys == str(correctAns)) or (key_resp_10.keys == correctAns):
                    key_resp_10.corr = 1
                else:
                    key_resp_10.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *target* updates
        if frameN >= 63.0 and target.status == NOT_STARTED:
            # keep track of start time/frame for later
            target.tStart = t  # not accounting for scr refresh
            target.frameNStart = frameN  # exact frame index
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED and frameN >= 93.0:
            # keep track of stop time/frame for later
            target.tStop = t  # not accounting for scr refresh
            target.frameNStop = frameN  # exact frame index
            win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
            target.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in primingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "priming"-------
    for thisComponent in primingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    forth_session.addData('mask.started', mask.tStartRefresh)
    forth_session.addData('mask.stopped', mask.tStopRefresh)
    forth_session.addData('prime.started', prime.tStartRefresh)
    forth_session.addData('prime.stopped', prime.tStopRefresh)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           key_resp_10.corr = 1;  # correct non-response
        else:
           key_resp_10.corr = 0;  # failed to respond (incorrectly)
    # store data for forth_session (TrialHandler)
    forth_session.addData('key_resp_10.keys',key_resp_10.keys)
    forth_session.addData('key_resp_10.corr', key_resp_10.corr)
    if key_resp_10.keys != None:  # we had a response
        forth_session.addData('key_resp_10.rt', key_resp_10.rt)
    forth_session.addData('key_resp_10.started', key_resp_10.tStartRefresh)
    forth_session.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
    forth_session.addData('target.started', target.tStartRefresh)
    forth_session.addData('target.stopped', target.tStopRefresh)
    # the Routine "priming" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'forth_session'


# ------Prepare to start Routine "fin"-------
t = 0
finClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
finComponents = [text_6]
for thisComponent in finComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "fin"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # not accounting for scr refresh
        text_6.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_6.tStop = t  # not accounting for scr refresh
        text_6.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
        text_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fin"-------
for thisComponent in finComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)

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
