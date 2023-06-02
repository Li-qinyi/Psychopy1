#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on 六月 01, 2023, at 23:23
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'MID&SID day1-encode'  # from the Builder filename that created this script
expInfo = {
    'name': '',
    'ID': '',
    'gender': '',
    'age': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['name'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\MID\\MID_SID_ day1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0.506,0.506,0.506], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "prep" ---
prep_image = visual.ImageStim(
    win=win,
    name='prep_image', units='pix', 
    image='instruction/prepare.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
define = keyboard.Keyboard()

# --- Initialize components for Routine "MID_pra" ---
instr = visual.ImageStim(
    win=win,
    name='instr', units='pix', 
    image='instruction/instruction1.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
enter = keyboard.Keyboard()
# Run 'Begin Experiment' code from MID
mon_condition = 'images'+'/'+'cue'+'/'+'reward-condition'+'/'+'cue1_1.jpg'
mon_no_condition = 'images'+'/'+'cue'+'/'+'no-reward'+'/'+'cue1_2.jpg'
mon_feedback = 'images'+'/'+'feedback'+'/'+'reward_fe'+'/'+'feedback1_1.jpg'
mon_no_feedback = 'images'+'/'+'feedback'+'/'+'no_reward_fe'+'/'+'feedback1_2.jpg'
warning = 'instruction' + '/' + 'warning.bmp'
notpress=0

# --- Initialize components for Routine "pra_encode" ---
fixation1_1 = visual.ShapeStim(
    win=win, name='fixation1_1', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
cue = visual.ImageStim(
    win=win,
    name='cue', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
fixation1_2 = visual.ShapeStim(
    win=win, name='fixation1_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=-3.0, interpolate=True)
pra_target = visual.ImageStim(
    win=win,
    name='pra_target', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
response = keyboard.Keyboard()

# --- Initialize components for Routine "pra_feedback" ---
fix1 = visual.ShapeStim(
    win=win, name='fix1', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "pra_ITI" ---
pra_fix_ITI = visual.TextStim(win=win, name='pra_fix_ITI',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "interval" ---
image_2 = visual.ImageStim(
    win=win,
    name='image_2', units='pix', 
    image='instruction/practice.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "MID1_instru" ---
MID1_inst = visual.ImageStim(
    win=win,
    name='MID1_inst', units='pix', 
    image='instruction/MID_instru.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
enter1 = keyboard.Keyboard()

# --- Initialize components for Routine "shou_encd" ---
fixation2_12 = visual.ShapeStim(
    win=win, name='fixation2_12', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
cue_6 = visual.ImageStim(
    win=win,
    name='cue_6', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
fixation2_13 = visual.ShapeStim(
    win=win, name='fixation2_13', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=-3.0, interpolate=True)
formal_target_5 = visual.ImageStim(
    win=win,
    name='formal_target_5', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
response2_5 = keyboard.Keyboard()
# Run 'Begin Experiment' code from shou
pressIndex = 1
slow_shou = visual.ImageStim(
    win=win,
    name='slow_shou', units='pix', 
    image='instruction'+'/'+'toSlow.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
warn_slow = visual.ImageStim(
    win=win,
    name='warn_slow', units='pix', 
    image='instruction'+'/'+'alarm.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# --- Initialize components for Routine "shou_feed" ---
shou_polygon = visual.ShapeStim(
    win=win, name='shou_polygon', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=-1.0, interpolate=True)
formal_fe_2 = visual.ImageStim(
    win=win,
    name='formal_fe_2', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "shouITI" ---
fix_ITI_6 = visual.TextStim(win=win, name='fix_ITI_6',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "MID1_encode" ---
fixation2_1 = visual.ShapeStim(
    win=win, name='fixation2_1', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
cue_2 = visual.ImageStim(
    win=win,
    name='cue_2', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
fixation2_2 = visual.ShapeStim(
    win=win, name='fixation2_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=-3.0, interpolate=True)
formal_target = visual.ImageStim(
    win=win,
    name='formal_target', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
response2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from MID1
pressIndex = 1
slow = visual.ImageStim(
    win=win,
    name='slow', units='pix', 
    image='instruction'+'/'+'toSlow.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
warn = visual.ImageStim(
    win=win,
    name='warn', units='pix', 
    image='instruction'+'/'+'alarm.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# --- Initialize components for Routine "MID1_feedback" ---
fixation2_3 = visual.ShapeStim(
    win=win, name='fixation2_3', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
formal_fe = visual.ImageStim(
    win=win,
    name='formal_fe', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "MID1_ITI" ---
fix_ITI = visual.TextStim(win=win, name='fix_ITI',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "MID1_rest" ---
rest = visual.ImageStim(
    win=win,
    name='rest', units='pix', 
    image='instruction/rest.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960,720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "SID_pra" ---
instr_2 = visual.ImageStim(
    win=win,
    name='instr_2', units='pix', 
    image='instruction/instruction1.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
enter_2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from SID
#定义reward-condition/no-reward的路径
sub_id = expInfo['ID']

soci_condition = 'images'+'/'+'cue'+'/'+'reward-condition'+'/'+'cue2_1.jpg'
soci_no_condition = 'images'+'/'+'cue'+'/'+'no-reward'+'/'+'cue2_2.jpg'
soci_no_feedback = 'images'+'/'+'feedback'+'/'+'no_reward_fe'+'/'+'feedback2_2.bmp'
soci_feedback = 'images'+'/'+'feedback'+'/'+'reward_fe'+'/'+'pra.jpg'

warning = 'instruction' + '/' + 'warning.bmp'
notpress=0

# --- Initialize components for Routine "Spra_encode" ---
fixation1 = visual.ShapeStim(
    win=win, name='fixation1', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
cue_8 = visual.ImageStim(
    win=win,
    name='cue_8', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
fixation1_3 = visual.ShapeStim(
    win=win, name='fixation1_3', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=-3.0, interpolate=True)
pra_target_2 = visual.ImageStim(
    win=win,
    name='pra_target_2', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
response_2 = keyboard.Keyboard()

# --- Initialize components for Routine "Spra_feedback" ---
fix1_2 = visual.ShapeStim(
    win=win, name='fix1_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "Spra_ITI" ---
pra_fix_ITI_2 = visual.TextStim(win=win, name='pra_fix_ITI_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "S_interval" ---
image_4 = visual.ImageStim(
    win=win,
    name='image_4', units='pix', 
    image='instruction/practice.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "SID1_instru" ---
SID1_instr = visual.ImageStim(
    win=win,
    name='SID1_instr', units='pix', 
    image='instruction/SID_instru.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
enter2 = keyboard.Keyboard()

# --- Initialize components for Routine "SID1_encode" ---
fixation2 = visual.ShapeStim(
    win=win, name='fixation2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
cue_3 = visual.ImageStim(
    win=win,
    name='cue_3', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
fixation2_4 = visual.ShapeStim(
    win=win, name='fixation2_4', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=-3.0, interpolate=True)
formal_target_2 = visual.ImageStim(
    win=win,
    name='formal_target_2', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
response2_2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from SID1
pressIndex = 1
SID_slow = visual.ImageStim(
    win=win,
    name='SID_slow', units='pix', 
    image='instruction'+'/'+'toSlow.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
SID_warn = visual.ImageStim(
    win=win,
    name='SID_warn', units='pix', 
    image='instruction'+'/'+'alarm.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# --- Initialize components for Routine "SID1_feedback" ---
fix_SID1 = visual.ShapeStim(
    win=win, name='fix_SID1', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
SID_feed1 = visual.ImageStim(
    win=win,
    name='SID_feed1', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "SID1_ITI" ---
fix_ITI_2 = visual.TextStim(win=win, name='fix_ITI_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "SID_rest" ---
rest_2 = visual.ImageStim(
    win=win,
    name='rest_2', units='pix', 
    image='instruction/rest.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960,720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "MID2_instr" ---
MID1_inst_2 = visual.ImageStim(
    win=win,
    name='MID1_inst_2', units='pix', 
    image='instruction/MID_instru.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
enter1_2 = keyboard.Keyboard()

# --- Initialize components for Routine "MID2_encode" ---
fixation2_6 = visual.ShapeStim(
    win=win, name='fixation2_6', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
cue_4 = visual.ImageStim(
    win=win,
    name='cue_4', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
fixation2_7 = visual.ShapeStim(
    win=win, name='fixation2_7', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=-3.0, interpolate=True)
formal_target_3 = visual.ImageStim(
    win=win,
    name='formal_target_3', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
response2_3 = keyboard.Keyboard()
# Run 'Begin Experiment' code from MID2
pressIndex = 1
MID2_slow = visual.ImageStim(
    win=win,
    name='MID2_slow', units='pix', 
    image='instruction'+'/'+'toSlow.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
MID2_warn = visual.ImageStim(
    win=win,
    name='MID2_warn', units='pix', 
    image='instruction'+'/'+'alarm.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# --- Initialize components for Routine "MID2_feed" ---
MID2_polygon = visual.ShapeStim(
    win=win, name='MID2_polygon', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
formal_fe_3 = visual.ImageStim(
    win=win,
    name='formal_fe_3', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "MID2_ITI_2" ---
fix_ITI_4 = visual.TextStim(win=win, name='fix_ITI_4',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "REST3" ---
rest_3 = visual.ImageStim(
    win=win,
    name='rest_3', units='pix', 
    image='instruction/rest.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960,720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "SID2_instr" ---
SID1_instr_2 = visual.ImageStim(
    win=win,
    name='SID1_instr_2', units='pix', 
    image='instruction/SID_instru.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
enter2_2 = keyboard.Keyboard()

# --- Initialize components for Routine "SID2_enc" ---
fixation2_5 = visual.ShapeStim(
    win=win, name='fixation2_5', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
cue_5 = visual.ImageStim(
    win=win,
    name='cue_5', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
fixation2_8 = visual.ShapeStim(
    win=win, name='fixation2_8', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=-3.0, interpolate=True)
formal_target_4 = visual.ImageStim(
    win=win,
    name='formal_target_4', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
response2_4 = keyboard.Keyboard()
# Run 'Begin Experiment' code from SID2
pressIndex = 1
SID2_slow = visual.ImageStim(
    win=win,
    name='SID2_slow', units='pix', 
    image='instruction'+'/'+'toSlow.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
SID2_warn = visual.ImageStim(
    win=win,
    name='SID2_warn', units='pix', 
    image='instruction'+'/'+'alarm.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# --- Initialize components for Routine "SID2_fee" ---
fix_SID1_2 = visual.ShapeStim(
    win=win, name='fix_SID1_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
SID_feed1_2 = visual.ImageStim(
    win=win,
    name='SID_feed1_2', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "SID2_ITI" ---
fix_ITI_5 = visual.TextStim(win=win, name='fix_ITI_5',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "jin_encd" ---
fixation2_15 = visual.ShapeStim(
    win=win, name='fixation2_15', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
cue_7 = visual.ImageStim(
    win=win,
    name='cue_7', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
fixation2_16 = visual.ShapeStim(
    win=win, name='fixation2_16', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=-3.0, interpolate=True)
formal_target_6 = visual.ImageStim(
    win=win,
    name='formal_target_6', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
response2_6 = keyboard.Keyboard()
# Run 'Begin Experiment' code from jin
pressIndex = 1
jin_slow = visual.ImageStim(
    win=win,
    name='jin_slow', units='pix', 
    image='instruction'+'/'+'toSlow.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
jin_warn = visual.ImageStim(
    win=win,
    name='jin_warn', units='pix', 
    image='instruction'+'/'+'alarm.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# --- Initialize components for Routine "jin_feed" ---
JIN_polygon = visual.ShapeStim(
    win=win, name='JIN_polygon', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
    opacity=1.0, depth=0.0, interpolate=True)
formal_fe_5 = visual.ImageStim(
    win=win,
    name='formal_fe_5', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(920, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "jinITI" ---
fix_ITI_7 = visual.TextStim(win=win, name='fix_ITI_7',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "thanks" ---
end = visual.ImageStim(
    win=win,
    name='end', units='pix', 
    image='instruction/rate_end.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(960, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
the_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "prep" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
define.keys = []
define.rt = []
_define_allKeys = []
# keep track of which components have finished
prepComponents = [prep_image, define]
for thisComponent in prepComponents:
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

# --- Run Routine "prep" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prep_image* updates
    if prep_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prep_image.frameNStart = frameN  # exact frame index
        prep_image.tStart = t  # local t and not account for scr refresh
        prep_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prep_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prep_image.started')
        prep_image.setAutoDraw(True)
    
    # *define* updates
    waitOnFlip = False
    if define.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        define.frameNStart = frameN  # exact frame index
        define.tStart = t  # local t and not account for scr refresh
        define.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(define, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'define.started')
        define.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(define.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(define.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if define.status == STARTED and not waitOnFlip:
        theseKeys = define.getKeys(keyList=['space'], waitRelease=False)
        _define_allKeys.extend(theseKeys)
        if len(_define_allKeys):
            define.keys = _define_allKeys[-1].name  # just the last key pressed
            define.rt = _define_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prepComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prep" ---
for thisComponent in prepComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if define.keys in ['', [], None]:  # No response was made
    define.keys = None
thisExp.addData('define.keys',define.keys)
if define.keys != None:  # we had a response
    thisExp.addData('define.rt', define.rt)
thisExp.nextEntry()
# the Routine "prep" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MID_pra" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
enter.keys = []
enter.rt = []
_enter_allKeys = []
# keep track of which components have finished
MID_praComponents = [instr, enter]
for thisComponent in MID_praComponents:
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

# --- Run Routine "MID_pra" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr.frameNStart = frameN  # exact frame index
        instr.tStart = t  # local t and not account for scr refresh
        instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr.started')
        instr.setAutoDraw(True)
    
    # *enter* updates
    waitOnFlip = False
    if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter.frameNStart = frameN  # exact frame index
        enter.tStart = t  # local t and not account for scr refresh
        enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'enter.started')
        enter.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['space'], waitRelease=False)
        _enter_allKeys.extend(theseKeys)
        if len(_enter_allKeys):
            enter.keys = _enter_allKeys[-1].name  # just the last key pressed
            enter.rt = _enter_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MID_praComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MID_pra" ---
for thisComponent in MID_praComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if enter.keys in ['', [], None]:  # No response was made
    enter.keys = None
thisExp.addData('enter.keys',enter.keys)
if enter.keys != None:  # we had a response
    thisExp.addData('enter.rt', enter.rt)
thisExp.nextEntry()
# the Routine "MID_pra" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
MIDprac_loop = data.TrialHandler(nReps=0.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice/pra_MID.xlsx'),
    seed=None, name='MIDprac_loop')
thisExp.addLoop(MIDprac_loop)  # add the loop to the experiment
thisMIDprac_loop = MIDprac_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMIDprac_loop.rgb)
if thisMIDprac_loop != None:
    for paramName in thisMIDprac_loop:
        exec('{} = thisMIDprac_loop[paramName]'.format(paramName))

for thisMIDprac_loop in MIDprac_loop:
    currentLoop = MIDprac_loop
    # abbreviate parameter names if possible (e.g. rgb = thisMIDprac_loop.rgb)
    if thisMIDprac_loop != None:
        for paramName in thisMIDprac_loop:
            exec('{} = thisMIDprac_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "pra_encode" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pra_code
    if trial_type==1 or trial_type==2: #社会奖赏条件
        cue_path = mon_condition
    if trial_type==3 or trial_type==4: #无社会奖赏条件
        cue_path = mon_no_condition
    cue.setImage(cue_path)
    pra_target.setImage(pra_images2)
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # keep track of which components have finished
    pra_encodeComponents = [fixation1_1, cue, fixation1_2, pra_target, response]
    for thisComponent in pra_encodeComponents:
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
    
    # --- Run Routine "pra_encode" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation1_1* updates
        if fixation1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation1_1.frameNStart = frameN  # exact frame index
            fixation1_1.tStart = t  # local t and not account for scr refresh
            fixation1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation1_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation1_1.started')
            fixation1_1.setAutoDraw(True)
        if fixation1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation1_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation1_1.tStop = t  # not accounting for scr refresh
                fixation1_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation1_1.stopped')
                fixation1_1.setAutoDraw(False)
        
        # *cue* updates
        if cue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            cue.frameNStart = frameN  # exact frame index
            cue.tStart = t  # local t and not account for scr refresh
            cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue.started')
            cue.setAutoDraw(True)
        if cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cue.tStop = t  # not accounting for scr refresh
                cue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue.stopped')
                cue.setAutoDraw(False)
        
        # *fixation1_2* updates
        if fixation1_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            fixation1_2.frameNStart = frameN  # exact frame index
            fixation1_2.tStart = t  # local t and not account for scr refresh
            fixation1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation1_2.started')
            fixation1_2.setAutoDraw(True)
        if fixation1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation1_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation1_2.tStop = t  # not accounting for scr refresh
                fixation1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation1_2.stopped')
                fixation1_2.setAutoDraw(False)
        
        # *pra_target* updates
        if pra_target.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            pra_target.frameNStart = frameN  # exact frame index
            pra_target.tStart = t  # local t and not account for scr refresh
            pra_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pra_target.started')
            pra_target.setAutoDraw(True)
        if pra_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pra_target.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                pra_target.tStop = t  # not accounting for scr refresh
                pra_target.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pra_target.stopped')
                pra_target.setAutoDraw(False)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response.started')
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                response.tStop = t  # not accounting for scr refresh
                response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response.stopped')
                response.status = FINISHED
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=["f","j"], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[-1].name  # just the last key pressed
                response.rt = _response_allKeys[-1].rt
                # was this correct?
                if (response.keys == str(corrAns)) or (response.keys == corrAns):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra_encodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pra_encode" ---
    for thisComponent in pra_encodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for MIDprac_loop (TrialHandler)
    MIDprac_loop.addData('response.keys',response.keys)
    MIDprac_loop.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        MIDprac_loop.addData('response.rt', response.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "pra_feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from setMsg
    if trial_type==1 or trial_type==2:
        prafeedback_path = mon_feedback
    if trial_type==3 or trial_type==4:
        prafeedback_path = mon_no_feedback
    image.setImage(prafeedback_path)
    # keep track of which components have finished
    pra_feedbackComponents = [fix1, image]
    for thisComponent in pra_feedbackComponents:
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
    
    # --- Run Routine "pra_feedback" ---
    while continueRoutine and routineTimer.getTime() < 2.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix1* updates
        if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix1.frameNStart = frameN  # exact frame index
            fix1.tStart = t  # local t and not account for scr refresh
            fix1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix1.started')
            fix1.setAutoDraw(True)
        if fix1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix1.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fix1.tStop = t  # not accounting for scr refresh
                fix1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix1.stopped')
                fix1.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pra_feedback" ---
    for thisComponent in pra_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.300000)
    
    # --- Prepare to start Routine "pra_ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    pra_ITIComponents = [pra_fix_ITI]
    for thisComponent in pra_ITIComponents:
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
    
    # --- Run Routine "pra_ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pra_fix_ITI* updates
        if pra_fix_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pra_fix_ITI.frameNStart = frameN  # exact frame index
            pra_fix_ITI.tStart = t  # local t and not account for scr refresh
            pra_fix_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_fix_ITI, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pra_fix_ITI.started')
            pra_fix_ITI.setAutoDraw(True)
        if pra_fix_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pra_fix_ITI.tStartRefresh + random () +1.5-frameTolerance:
                # keep track of stop time/frame for later
                pra_fix_ITI.tStop = t  # not accounting for scr refresh
                pra_fix_ITI.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pra_fix_ITI.stopped')
                pra_fix_ITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pra_ITI" ---
    for thisComponent in pra_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "pra_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "interval" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_5
    if notpress >= 4:
        inter_image = 'instruction/failpractice.bmp'
    else:
        inter_image = 'instruction/practice.jpg'
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    intervalComponents = [image_2, key_resp]
    for thisComponent in intervalComponents:
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
    
    # --- Run Routine "interval" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_5
        if trialNum == 6:
            continueRoutine = True
        else:
            continueRoutine = False
        if notpress >= 4:
            inter_image = 'instruction/failpractice.bmp'
        else:
            inter_image = 'instruction/practice.jpg'
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2.started')
            image_2.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intervalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "interval" ---
    for thisComponent in intervalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_5
    if trialNum == 6 and notpress <= 4:
        MIDprac_loop.finished = True
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    MIDprac_loop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        MIDprac_loop.addData('key_resp.rt', key_resp.rt)
    # the Routine "interval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'MIDprac_loop'

# get names of stimulus parameters
if MIDprac_loop.trialList in ([], [None], None):
    params = []
else:
    params = MIDprac_loop.trialList[0].keys()
# save data for this loop
MIDprac_loop.saveAsExcel(filename + '.xlsx', sheetName='MIDprac_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "MID1_instru" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
enter1.keys = []
enter1.rt = []
_enter1_allKeys = []
# keep track of which components have finished
MID1_instruComponents = [MID1_inst, enter1]
for thisComponent in MID1_instruComponents:
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

# --- Run Routine "MID1_instru" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *MID1_inst* updates
    if MID1_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MID1_inst.frameNStart = frameN  # exact frame index
        MID1_inst.tStart = t  # local t and not account for scr refresh
        MID1_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MID1_inst, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'MID1_inst.started')
        MID1_inst.setAutoDraw(True)
    
    # *enter1* updates
    waitOnFlip = False
    if enter1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter1.frameNStart = frameN  # exact frame index
        enter1.tStart = t  # local t and not account for scr refresh
        enter1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'enter1.started')
        enter1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter1.status == STARTED and not waitOnFlip:
        theseKeys = enter1.getKeys(keyList=['space'], waitRelease=False)
        _enter1_allKeys.extend(theseKeys)
        if len(_enter1_allKeys):
            enter1.keys = _enter1_allKeys[-1].name  # just the last key pressed
            enter1.rt = _enter1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MID1_instruComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MID1_instru" ---
for thisComponent in MID1_instruComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if enter1.keys in ['', [], None]:  # No response was made
    enter1.keys = None
thisExp.addData('enter1.keys',enter1.keys)
if enter1.keys != None:  # we had a response
    thisExp.addData('enter1.rt', enter1.rt)
thisExp.nextEntry()
# the Routine "MID1_instru" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=0.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('shouyin.xlsx'),
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
    
    # --- Prepare to start Routine "shou_encd" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pra_code_6
    if trial_type==1 or trial_type==2: #金钱奖赏条件
          cue_path=mon_condition
    if trial_type==3 or trial_type==4: #无金钱奖赏条件
          cue_path=mon_no_condition
    if trial_type==5 or trial_type==6: #社会奖赏条件
          cue_path=soci_condition
    if trial_type==7 or trial_type==8: #无社会奖赏条件
          cue_path=soci_no_condition
    cue_6.setImage(cue_path)
    formal_target_5.setImage(images)
    response2_5.keys = []
    response2_5.rt = []
    _response2_5_allKeys = []
    # Run 'Begin Routine' code from shou
    alarm = False
    # keep track of which components have finished
    shou_encdComponents = [fixation2_12, cue_6, fixation2_13, formal_target_5, response2_5, slow_shou, warn_slow]
    for thisComponent in shou_encdComponents:
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
    
    # --- Run Routine "shou_encd" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2_12* updates
        if fixation2_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2_12.frameNStart = frameN  # exact frame index
            fixation2_12.tStart = t  # local t and not account for scr refresh
            fixation2_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_12.started')
            fixation2_12.setAutoDraw(True)
        if fixation2_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_12.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_12.tStop = t  # not accounting for scr refresh
                fixation2_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_12.stopped')
                fixation2_12.setAutoDraw(False)
        
        # *cue_6* updates
        if cue_6.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            cue_6.frameNStart = frameN  # exact frame index
            cue_6.tStart = t  # local t and not account for scr refresh
            cue_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue_6.started')
            cue_6.setAutoDraw(True)
        if cue_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_6.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_6.tStop = t  # not accounting for scr refresh
                cue_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue_6.stopped')
                cue_6.setAutoDraw(False)
        
        # *fixation2_13* updates
        if fixation2_13.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            fixation2_13.frameNStart = frameN  # exact frame index
            fixation2_13.tStart = t  # local t and not account for scr refresh
            fixation2_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_13.started')
            fixation2_13.setAutoDraw(True)
        if fixation2_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_13.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_13.tStop = t  # not accounting for scr refresh
                fixation2_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_13.stopped')
                fixation2_13.setAutoDraw(False)
        
        # *formal_target_5* updates
        if formal_target_5.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            formal_target_5.frameNStart = frameN  # exact frame index
            formal_target_5.tStart = t  # local t and not account for scr refresh
            formal_target_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_target_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_target_5.started')
            formal_target_5.setAutoDraw(True)
        if formal_target_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal_target_5.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                formal_target_5.tStop = t  # not accounting for scr refresh
                formal_target_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'formal_target_5.stopped')
                formal_target_5.setAutoDraw(False)
        
        # *response2_5* updates
        waitOnFlip = False
        if response2_5.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            response2_5.frameNStart = frameN  # exact frame index
            response2_5.tStart = t  # local t and not account for scr refresh
            response2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response2_5.started')
            response2_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response2_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response2_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response2_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response2_5.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                response2_5.tStop = t  # not accounting for scr refresh
                response2_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response2_5.stopped')
                response2_5.status = FINISHED
        if response2_5.status == STARTED and not waitOnFlip:
            theseKeys = response2_5.getKeys(keyList=["f","j"], waitRelease=False)
            _response2_5_allKeys.extend(theseKeys)
            if len(_response2_5_allKeys):
                response2_5.keys = _response2_5_allKeys[-1].name  # just the last key pressed
                response2_5.rt = _response2_5_allKeys[-1].rt
                # was this correct?
                if (response2_5.keys == str(corrAns)) or (response2_5.keys == corrAns):
                    response2_5.corr = 1
                else:
                    response2_5.corr = 0
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from shou
        if pressIndex == 1:
            warn_slow.status = FINISHED
        else:
            alarm = True
        
        # *slow_shou* updates
        if slow_shou.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            slow_shou.frameNStart = frameN  # exact frame index
            slow_shou.tStart = t  # local t and not account for scr refresh
            slow_shou.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slow_shou, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slow_shou.started')
            slow_shou.setAutoDraw(True)
        if slow_shou.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slow_shou.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                slow_shou.tStop = t  # not accounting for scr refresh
                slow_shou.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slow_shou.stopped')
                slow_shou.setAutoDraw(False)
        
        # *warn_slow* updates
        if warn_slow.status == NOT_STARTED and alarm:
            # keep track of start time/frame for later
            warn_slow.frameNStart = frameN  # exact frame index
            warn_slow.tStart = t  # local t and not account for scr refresh
            warn_slow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(warn_slow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'warn_slow.started')
            warn_slow.setAutoDraw(True)
        if warn_slow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > warn_slow.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                warn_slow.tStop = t  # not accounting for scr refresh
                warn_slow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'warn_slow.stopped')
                warn_slow.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in shou_encdComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "shou_encd" ---
    for thisComponent in shou_encdComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response2_5.keys in ['', [], None]:  # No response was made
        response2_5.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response2_5.corr = 1;  # correct non-response
        else:
           response2_5.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('response2_5.keys',response2_5.keys)
    trials.addData('response2_5.corr', response2_5.corr)
    if response2_5.keys != None:  # we had a response
        trials.addData('response2_5.rt', response2_5.rt)
    # Run 'End Routine' code from shou
    pressIndex = 1
    # the Routine "shou_encd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "shou_feed" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    if corrAns == 'f':
        if trial_type==1:
            if response2_6.corr==1:
                feedback = mon_feedback
        elif trial_type==3:
            if response2_6.corr==1:
                feedback = mon_no_feedback
    if response2_6.corr==0:
        feedback = mon_no_feedback
    
    if corrAns == 'j':
        if trial_type==2:
            if response2_6.corr==1:
                feedback = mon_feedback
        elif trial_type==4:
            if response2_6.corr==1:
                feedback = mon_no_feedback
    if response2_6.corr==0:
        feedback = mon_no_feedback
    
    formal_fe_2.setImage(feedback)
    # keep track of which components have finished
    shou_feedComponents = [shou_polygon, formal_fe_2]
    for thisComponent in shou_feedComponents:
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
    
    # --- Run Routine "shou_feed" ---
    while continueRoutine and routineTimer.getTime() < 2.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code
        if response2_5.keys:
            continueRoutine = True
        else:
            continueRoutine = False
        
        # *shou_polygon* updates
        if shou_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            shou_polygon.frameNStart = frameN  # exact frame index
            shou_polygon.tStart = t  # local t and not account for scr refresh
            shou_polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shou_polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'shou_polygon.started')
            shou_polygon.setAutoDraw(True)
        if shou_polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > shou_polygon.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                shou_polygon.tStop = t  # not accounting for scr refresh
                shou_polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'shou_polygon.stopped')
                shou_polygon.setAutoDraw(False)
        
        # *formal_fe_2* updates
        if formal_fe_2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            formal_fe_2.frameNStart = frameN  # exact frame index
            formal_fe_2.tStart = t  # local t and not account for scr refresh
            formal_fe_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_fe_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_fe_2.started')
            formal_fe_2.setAutoDraw(True)
        if formal_fe_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal_fe_2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                formal_fe_2.tStop = t  # not accounting for scr refresh
                formal_fe_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'formal_fe_2.stopped')
                formal_fe_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in shou_feedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "shou_feed" ---
    for thisComponent in shou_feedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.300000)
    
    # --- Prepare to start Routine "shouITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    shouITIComponents = [fix_ITI_6]
    for thisComponent in shouITIComponents:
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
    
    # --- Run Routine "shouITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_ITI_6* updates
        if fix_ITI_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_ITI_6.frameNStart = frameN  # exact frame index
            fix_ITI_6.tStart = t  # local t and not account for scr refresh
            fix_ITI_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_ITI_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_ITI_6.started')
            fix_ITI_6.setAutoDraw(True)
        if fix_ITI_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_ITI_6.tStartRefresh + random () +1.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_ITI_6.tStop = t  # not accounting for scr refresh
                fix_ITI_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_ITI_6.stopped')
                fix_ITI_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in shouITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "shouITI" ---
    for thisComponent in shouITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "shouITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
MID1_trials = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('MID1.xlsx'),
    seed=None, name='MID1_trials')
thisExp.addLoop(MID1_trials)  # add the loop to the experiment
thisMID1_trial = MID1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMID1_trial.rgb)
if thisMID1_trial != None:
    for paramName in thisMID1_trial:
        exec('{} = thisMID1_trial[paramName]'.format(paramName))

for thisMID1_trial in MID1_trials:
    currentLoop = MID1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisMID1_trial.rgb)
    if thisMID1_trial != None:
        for paramName in thisMID1_trial:
            exec('{} = thisMID1_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "MID1_encode" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pra_code_2
    if trial_type==1 or trial_type==2: #金钱奖赏条件
          cue_path=mon_condition
    if trial_type==3 or trial_type==4: #无金钱奖赏条件
          cue_path=mon_no_condition
    if trial_type==5 or trial_type==6: #社会奖赏条件
          cue_path=soci_condition
    if trial_type==7 or trial_type==8: #无社会奖赏条件
          cue_path=soci_no_condition
    cue_2.setImage(cue_path)
    formal_target.setImage(images)
    response2.keys = []
    response2.rt = []
    _response2_allKeys = []
    # Run 'Begin Routine' code from MID1
    alarm = False
    # keep track of which components have finished
    MID1_encodeComponents = [fixation2_1, cue_2, fixation2_2, formal_target, response2, slow, warn]
    for thisComponent in MID1_encodeComponents:
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
    
    # --- Run Routine "MID1_encode" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2_1* updates
        if fixation2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2_1.frameNStart = frameN  # exact frame index
            fixation2_1.tStart = t  # local t and not account for scr refresh
            fixation2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_1.started')
            fixation2_1.setAutoDraw(True)
        if fixation2_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_1.tStop = t  # not accounting for scr refresh
                fixation2_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_1.stopped')
                fixation2_1.setAutoDraw(False)
        
        # *cue_2* updates
        if cue_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            cue_2.frameNStart = frameN  # exact frame index
            cue_2.tStart = t  # local t and not account for scr refresh
            cue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue_2.started')
            cue_2.setAutoDraw(True)
        if cue_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_2.tStop = t  # not accounting for scr refresh
                cue_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue_2.stopped')
                cue_2.setAutoDraw(False)
        
        # *fixation2_2* updates
        if fixation2_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            fixation2_2.frameNStart = frameN  # exact frame index
            fixation2_2.tStart = t  # local t and not account for scr refresh
            fixation2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_2.started')
            fixation2_2.setAutoDraw(True)
        if fixation2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_2.tStop = t  # not accounting for scr refresh
                fixation2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_2.stopped')
                fixation2_2.setAutoDraw(False)
        
        # *formal_target* updates
        if formal_target.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            formal_target.frameNStart = frameN  # exact frame index
            formal_target.tStart = t  # local t and not account for scr refresh
            formal_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_target.started')
            formal_target.setAutoDraw(True)
        if formal_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal_target.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                formal_target.tStop = t  # not accounting for scr refresh
                formal_target.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'formal_target.stopped')
                formal_target.setAutoDraw(False)
        
        # *response2* updates
        waitOnFlip = False
        if response2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            response2.frameNStart = frameN  # exact frame index
            response2.tStart = t  # local t and not account for scr refresh
            response2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response2.started')
            response2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                response2.tStop = t  # not accounting for scr refresh
                response2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response2.stopped')
                response2.status = FINISHED
        if response2.status == STARTED and not waitOnFlip:
            theseKeys = response2.getKeys(keyList=["f","j"], waitRelease=False)
            _response2_allKeys.extend(theseKeys)
            if len(_response2_allKeys):
                response2.keys = _response2_allKeys[-1].name  # just the last key pressed
                response2.rt = _response2_allKeys[-1].rt
                # was this correct?
                if (response2.keys == str(corrAns)) or (response2.keys == corrAns):
                    response2.corr = 1
                else:
                    response2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from MID1
        if pressIndex == 1:
            warn.status = FINISHED
        else:
            alarm = True
        
        # *slow* updates
        if slow.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            slow.frameNStart = frameN  # exact frame index
            slow.tStart = t  # local t and not account for scr refresh
            slow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slow.started')
            slow.setAutoDraw(True)
        if slow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slow.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                slow.tStop = t  # not accounting for scr refresh
                slow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slow.stopped')
                slow.setAutoDraw(False)
        
        # *warn* updates
        if warn.status == NOT_STARTED and alarm:
            # keep track of start time/frame for later
            warn.frameNStart = frameN  # exact frame index
            warn.tStart = t  # local t and not account for scr refresh
            warn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(warn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'warn.started')
            warn.setAutoDraw(True)
        if warn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > warn.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                warn.tStop = t  # not accounting for scr refresh
                warn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'warn.stopped')
                warn.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MID1_encodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "MID1_encode" ---
    for thisComponent in MID1_encodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response2.keys in ['', [], None]:  # No response was made
        response2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response2.corr = 1;  # correct non-response
        else:
           response2.corr = 0;  # failed to respond (incorrectly)
    # store data for MID1_trials (TrialHandler)
    MID1_trials.addData('response2.keys',response2.keys)
    MID1_trials.addData('response2.corr', response2.corr)
    if response2.keys != None:  # we had a response
        MID1_trials.addData('response2.rt', response2.rt)
    # Run 'End Routine' code from MID1
    pressIndex = 1
    # the Routine "MID1_encode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "MID1_feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from setMsg_2
    if corrAns == 'f':
        if trial_type==1:
            if response2.corr==1:
                feedback_path = mon_feedback
        elif trial_type==3:
            if response2.corr==1:
                feedback_path = mon_no_feedback
    if response2.corr==0:
        feedback_path = mon_no_feedback
    
    if corrAns == 'j':
        if trial_type==2:
            if response2.corr==1:
                feedback_path = mon_feedback
        elif trial_type==4:
            if response2.corr==1:
                feedback_path = mon_no_feedback
    if response2.corr==0:
        feedback_path = mon_no_feedback
    
    formal_fe.setImage(feedback_path)
    # keep track of which components have finished
    MID1_feedbackComponents = [fixation2_3, formal_fe]
    for thisComponent in MID1_feedbackComponents:
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
    
    # --- Run Routine "MID1_feedback" ---
    while continueRoutine and routineTimer.getTime() < 2.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2_3* updates
        if fixation2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2_3.frameNStart = frameN  # exact frame index
            fixation2_3.tStart = t  # local t and not account for scr refresh
            fixation2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_3.started')
            fixation2_3.setAutoDraw(True)
        if fixation2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_3.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_3.tStop = t  # not accounting for scr refresh
                fixation2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_3.stopped')
                fixation2_3.setAutoDraw(False)
        # Run 'Each Frame' code from setMsg_2
        if response2.keys:
            continueRoutine = True
        else:
            continueRoutine = False
        
        # *formal_fe* updates
        if formal_fe.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            formal_fe.frameNStart = frameN  # exact frame index
            formal_fe.tStart = t  # local t and not account for scr refresh
            formal_fe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_fe, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_fe.started')
            formal_fe.setAutoDraw(True)
        if formal_fe.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal_fe.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                formal_fe.tStop = t  # not accounting for scr refresh
                formal_fe.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'formal_fe.stopped')
                formal_fe.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MID1_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "MID1_feedback" ---
    for thisComponent in MID1_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.300000)
    
    # --- Prepare to start Routine "MID1_ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    MID1_ITIComponents = [fix_ITI]
    for thisComponent in MID1_ITIComponents:
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
    
    # --- Run Routine "MID1_ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_ITI* updates
        if fix_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_ITI.frameNStart = frameN  # exact frame index
            fix_ITI.tStart = t  # local t and not account for scr refresh
            fix_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_ITI, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_ITI.started')
            fix_ITI.setAutoDraw(True)
        if fix_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_ITI.tStartRefresh + random () +1.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_ITI.tStop = t  # not accounting for scr refresh
                fix_ITI.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_ITI.stopped')
                fix_ITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MID1_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "MID1_ITI" ---
    for thisComponent in MID1_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "MID1_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'MID1_trials'

# get names of stimulus parameters
if MID1_trials.trialList in ([], [None], None):
    params = []
else:
    params = MID1_trials.trialList[0].keys()
# save data for this loop
MID1_trials.saveAsExcel(filename + '.xlsx', sheetName='MID1_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "MID1_rest" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
MID1_restComponents = [rest]
for thisComponent in MID1_restComponents:
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

# --- Run Routine "MID1_rest" ---
while continueRoutine and routineTimer.getTime() < 60.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest* updates
    if rest.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        rest.frameNStart = frameN  # exact frame index
        rest.tStart = t  # local t and not account for scr refresh
        rest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest.started')
        rest.setAutoDraw(True)
    if rest.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            rest.tStop = t  # not accounting for scr refresh
            rest.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest.stopped')
            rest.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MID1_restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MID1_rest" ---
for thisComponent in MID1_restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-60.000000)

# --- Prepare to start Routine "SID_pra" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
enter_2.keys = []
enter_2.rt = []
_enter_2_allKeys = []
# keep track of which components have finished
SID_praComponents = [instr_2, enter_2]
for thisComponent in SID_praComponents:
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

# --- Run Routine "SID_pra" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_2* updates
    if instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_2.frameNStart = frameN  # exact frame index
        instr_2.tStart = t  # local t and not account for scr refresh
        instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_2.started')
        instr_2.setAutoDraw(True)
    
    # *enter_2* updates
    waitOnFlip = False
    if enter_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter_2.frameNStart = frameN  # exact frame index
        enter_2.tStart = t  # local t and not account for scr refresh
        enter_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'enter_2.started')
        enter_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter_2.status == STARTED and not waitOnFlip:
        theseKeys = enter_2.getKeys(keyList=['space'], waitRelease=False)
        _enter_2_allKeys.extend(theseKeys)
        if len(_enter_2_allKeys):
            enter_2.keys = _enter_2_allKeys[-1].name  # just the last key pressed
            enter_2.rt = _enter_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SID_praComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SID_pra" ---
for thisComponent in SID_praComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if enter_2.keys in ['', [], None]:  # No response was made
    enter_2.keys = None
thisExp.addData('enter_2.keys',enter_2.keys)
if enter_2.keys != None:  # we had a response
    thisExp.addData('enter_2.rt', enter_2.rt)
thisExp.nextEntry()
# the Routine "SID_pra" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SIDprac_loop = data.TrialHandler(nReps=0.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice/pra_SID.xlsx'),
    seed=None, name='SIDprac_loop')
thisExp.addLoop(SIDprac_loop)  # add the loop to the experiment
thisSIDprac_loop = SIDprac_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSIDprac_loop.rgb)
if thisSIDprac_loop != None:
    for paramName in thisSIDprac_loop:
        exec('{} = thisSIDprac_loop[paramName]'.format(paramName))

for thisSIDprac_loop in SIDprac_loop:
    currentLoop = SIDprac_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSIDprac_loop.rgb)
    if thisSIDprac_loop != None:
        for paramName in thisSIDprac_loop:
            exec('{} = thisSIDprac_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Spra_encode" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pra_code_8
    if trial_type==5 or trial_type==6: #社会奖赏条件
        cue_path = soci_condition
    if trial_type==7 or trial_type==8: #无社会奖赏条件
        cue_path = soci_no_condition
    cue_8.setImage(cue_path)
    pra_target_2.setImage(pra_images1)
    response_2.keys = []
    response_2.rt = []
    _response_2_allKeys = []
    # keep track of which components have finished
    Spra_encodeComponents = [fixation1, cue_8, fixation1_3, pra_target_2, response_2]
    for thisComponent in Spra_encodeComponents:
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
    
    # --- Run Routine "Spra_encode" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation1* updates
        if fixation1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation1.frameNStart = frameN  # exact frame index
            fixation1.tStart = t  # local t and not account for scr refresh
            fixation1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation1.started')
            fixation1.setAutoDraw(True)
        if fixation1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation1.tStop = t  # not accounting for scr refresh
                fixation1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation1.stopped')
                fixation1.setAutoDraw(False)
        
        # *cue_8* updates
        if cue_8.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            cue_8.frameNStart = frameN  # exact frame index
            cue_8.tStart = t  # local t and not account for scr refresh
            cue_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue_8.started')
            cue_8.setAutoDraw(True)
        if cue_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_8.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_8.tStop = t  # not accounting for scr refresh
                cue_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue_8.stopped')
                cue_8.setAutoDraw(False)
        
        # *fixation1_3* updates
        if fixation1_3.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            fixation1_3.frameNStart = frameN  # exact frame index
            fixation1_3.tStart = t  # local t and not account for scr refresh
            fixation1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation1_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation1_3.started')
            fixation1_3.setAutoDraw(True)
        if fixation1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation1_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation1_3.tStop = t  # not accounting for scr refresh
                fixation1_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation1_3.stopped')
                fixation1_3.setAutoDraw(False)
        
        # *pra_target_2* updates
        if pra_target_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            pra_target_2.frameNStart = frameN  # exact frame index
            pra_target_2.tStart = t  # local t and not account for scr refresh
            pra_target_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_target_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pra_target_2.started')
            pra_target_2.setAutoDraw(True)
        if pra_target_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pra_target_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                pra_target_2.tStop = t  # not accounting for scr refresh
                pra_target_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pra_target_2.stopped')
                pra_target_2.setAutoDraw(False)
        
        # *response_2* updates
        waitOnFlip = False
        if response_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            response_2.frameNStart = frameN  # exact frame index
            response_2.tStart = t  # local t and not account for scr refresh
            response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_2.started')
            response_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                response_2.tStop = t  # not accounting for scr refresh
                response_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_2.stopped')
                response_2.status = FINISHED
        if response_2.status == STARTED and not waitOnFlip:
            theseKeys = response_2.getKeys(keyList=["f","j"], waitRelease=False)
            _response_2_allKeys.extend(theseKeys)
            if len(_response_2_allKeys):
                response_2.keys = _response_2_allKeys[-1].name  # just the last key pressed
                response_2.rt = _response_2_allKeys[-1].rt
                # was this correct?
                if (response_2.keys == str(corrAns)) or (response_2.keys == corrAns):
                    response_2.corr = 1
                else:
                    response_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Spra_encodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Spra_encode" ---
    for thisComponent in Spra_encodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_2.keys in ['', [], None]:  # No response was made
        response_2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_2.corr = 1;  # correct non-response
        else:
           response_2.corr = 0;  # failed to respond (incorrectly)
    # store data for SIDprac_loop (TrialHandler)
    SIDprac_loop.addData('response_2.keys',response_2.keys)
    SIDprac_loop.addData('response_2.corr', response_2.corr)
    if response_2.keys != None:  # we had a response
        SIDprac_loop.addData('response_2.rt', response_2.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Spra_feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from setMsg_3
    if trial_type==5 or trial_type==6:
        praSIDfeed_path = soci_feedback
    if trial_type==7 or trial_type==8:
        praSIDfeed_path = soci_no_feedback
    image_3.setImage(praSIDfeed_path)
    # keep track of which components have finished
    Spra_feedbackComponents = [fix1_2, image_3]
    for thisComponent in Spra_feedbackComponents:
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
    
    # --- Run Routine "Spra_feedback" ---
    while continueRoutine and routineTimer.getTime() < 2.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix1_2* updates
        if fix1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix1_2.frameNStart = frameN  # exact frame index
            fix1_2.tStart = t  # local t and not account for scr refresh
            fix1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix1_2.started')
            fix1_2.setAutoDraw(True)
        if fix1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix1_2.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fix1_2.tStop = t  # not accounting for scr refresh
                fix1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix1_2.stopped')
                fix1_2.setAutoDraw(False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3.started')
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3.stopped')
                image_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Spra_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Spra_feedback" ---
    for thisComponent in Spra_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.300000)
    
    # --- Prepare to start Routine "Spra_ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    Spra_ITIComponents = [pra_fix_ITI_2]
    for thisComponent in Spra_ITIComponents:
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
    
    # --- Run Routine "Spra_ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pra_fix_ITI_2* updates
        if pra_fix_ITI_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pra_fix_ITI_2.frameNStart = frameN  # exact frame index
            pra_fix_ITI_2.tStart = t  # local t and not account for scr refresh
            pra_fix_ITI_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_fix_ITI_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pra_fix_ITI_2.started')
            pra_fix_ITI_2.setAutoDraw(True)
        if pra_fix_ITI_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pra_fix_ITI_2.tStartRefresh + random () +1.5-frameTolerance:
                # keep track of stop time/frame for later
                pra_fix_ITI_2.tStop = t  # not accounting for scr refresh
                pra_fix_ITI_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pra_fix_ITI_2.stopped')
                pra_fix_ITI_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Spra_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Spra_ITI" ---
    for thisComponent in Spra_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Spra_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "S_interval" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_3
    if notpress >= 4:
        inter_image = 'instruction/failpractice.bmp'
    else:
        inter_image = 'instruction/practice.jpg'
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    S_intervalComponents = [image_4, key_resp_2]
    for thisComponent in S_intervalComponents:
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
    
    # --- Run Routine "S_interval" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_3
        if trialNum == 6:
            continueRoutine = True
        else:
            continueRoutine = False
        if notpress >= 4:
            inter_image = 'instruction/failpractice.bmp'
        else:
            inter_image = 'instruction/practice.jpg'
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_4.started')
            image_4.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in S_intervalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "S_interval" ---
    for thisComponent in S_intervalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_3
    if trialNum == 6 and notpress <= 4:
        SIDprac_loop.finished = True
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    SIDprac_loop.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        SIDprac_loop.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "S_interval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'SIDprac_loop'

# get names of stimulus parameters
if SIDprac_loop.trialList in ([], [None], None):
    params = []
else:
    params = SIDprac_loop.trialList[0].keys()
# save data for this loop
SIDprac_loop.saveAsExcel(filename + '.xlsx', sheetName='SIDprac_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "SID1_instru" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
enter2.keys = []
enter2.rt = []
_enter2_allKeys = []
# keep track of which components have finished
SID1_instruComponents = [SID1_instr, enter2]
for thisComponent in SID1_instruComponents:
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

# --- Run Routine "SID1_instru" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SID1_instr* updates
    if SID1_instr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        SID1_instr.frameNStart = frameN  # exact frame index
        SID1_instr.tStart = t  # local t and not account for scr refresh
        SID1_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SID1_instr, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'SID1_instr.started')
        SID1_instr.setAutoDraw(True)
    
    # *enter2* updates
    waitOnFlip = False
    if enter2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        enter2.frameNStart = frameN  # exact frame index
        enter2.tStart = t  # local t and not account for scr refresh
        enter2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'enter2.started')
        enter2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter2.status == STARTED and not waitOnFlip:
        theseKeys = enter2.getKeys(keyList=['space'], waitRelease=False)
        _enter2_allKeys.extend(theseKeys)
        if len(_enter2_allKeys):
            enter2.keys = _enter2_allKeys[-1].name  # just the last key pressed
            enter2.rt = _enter2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SID1_instruComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SID1_instru" ---
for thisComponent in SID1_instruComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if enter2.keys in ['', [], None]:  # No response was made
    enter2.keys = None
thisExp.addData('enter2.keys',enter2.keys)
if enter2.keys != None:  # we had a response
    thisExp.addData('enter2.rt', enter2.rt)
thisExp.nextEntry()
# the Routine "SID1_instru" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SID1_trials = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SID.xlsx'),
    seed=None, name='SID1_trials')
thisExp.addLoop(SID1_trials)  # add the loop to the experiment
thisSID1_trial = SID1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSID1_trial.rgb)
if thisSID1_trial != None:
    for paramName in thisSID1_trial:
        exec('{} = thisSID1_trial[paramName]'.format(paramName))

for thisSID1_trial in SID1_trials:
    currentLoop = SID1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisSID1_trial.rgb)
    if thisSID1_trial != None:
        for paramName in thisSID1_trial:
            exec('{} = thisSID1_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SID1_encode" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pra_code_3
    if trial_type==5 or trial_type==6: #社会奖赏条件
          cue_path=soci_condition
    if trial_type==7 or trial_type==8: #无社会奖赏条件
          cue_path=soci_no_condition
    cue_3.setImage(cue_path)
    formal_target_2.setImage(images)
    response2_2.keys = []
    response2_2.rt = []
    _response2_2_allKeys = []
    # Run 'Begin Routine' code from SID1
    alarm = False
    # keep track of which components have finished
    SID1_encodeComponents = [fixation2, cue_3, fixation2_4, formal_target_2, response2_2, SID_slow, SID_warn]
    for thisComponent in SID1_encodeComponents:
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
    
    # --- Run Routine "SID1_encode" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2* updates
        if fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.tStart = t  # local t and not account for scr refresh
            fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2.started')
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2.stopped')
                fixation2.setAutoDraw(False)
        
        # *cue_3* updates
        if cue_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            cue_3.frameNStart = frameN  # exact frame index
            cue_3.tStart = t  # local t and not account for scr refresh
            cue_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue_3.started')
            cue_3.setAutoDraw(True)
        if cue_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_3.tStop = t  # not accounting for scr refresh
                cue_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue_3.stopped')
                cue_3.setAutoDraw(False)
        
        # *fixation2_4* updates
        if fixation2_4.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            fixation2_4.frameNStart = frameN  # exact frame index
            fixation2_4.tStart = t  # local t and not account for scr refresh
            fixation2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_4.started')
            fixation2_4.setAutoDraw(True)
        if fixation2_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_4.tStop = t  # not accounting for scr refresh
                fixation2_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_4.stopped')
                fixation2_4.setAutoDraw(False)
        
        # *formal_target_2* updates
        if formal_target_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            formal_target_2.frameNStart = frameN  # exact frame index
            formal_target_2.tStart = t  # local t and not account for scr refresh
            formal_target_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_target_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_target_2.started')
            formal_target_2.setAutoDraw(True)
        if formal_target_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal_target_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                formal_target_2.tStop = t  # not accounting for scr refresh
                formal_target_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'formal_target_2.stopped')
                formal_target_2.setAutoDraw(False)
        
        # *response2_2* updates
        waitOnFlip = False
        if response2_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            response2_2.frameNStart = frameN  # exact frame index
            response2_2.tStart = t  # local t and not account for scr refresh
            response2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response2_2.started')
            response2_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response2_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response2_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                response2_2.tStop = t  # not accounting for scr refresh
                response2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response2_2.stopped')
                response2_2.status = FINISHED
        if response2_2.status == STARTED and not waitOnFlip:
            theseKeys = response2_2.getKeys(keyList=["f","j"], waitRelease=False)
            _response2_2_allKeys.extend(theseKeys)
            if len(_response2_2_allKeys):
                response2_2.keys = _response2_2_allKeys[-1].name  # just the last key pressed
                response2_2.rt = _response2_2_allKeys[-1].rt
                # was this correct?
                if (response2_2.keys == str(corrAns)) or (response2_2.keys == corrAns):
                    response2_2.corr = 1
                else:
                    response2_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from SID1
        if pressIndex == 1:
            SID_warn.status = FINISHED
        else:
            alarm = True
        
        # *SID_slow* updates
        if SID_slow.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            SID_slow.frameNStart = frameN  # exact frame index
            SID_slow.tStart = t  # local t and not account for scr refresh
            SID_slow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SID_slow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SID_slow.started')
            SID_slow.setAutoDraw(True)
        if SID_slow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SID_slow.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                SID_slow.tStop = t  # not accounting for scr refresh
                SID_slow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SID_slow.stopped')
                SID_slow.setAutoDraw(False)
        
        # *SID_warn* updates
        if SID_warn.status == NOT_STARTED and alarm:
            # keep track of start time/frame for later
            SID_warn.frameNStart = frameN  # exact frame index
            SID_warn.tStart = t  # local t and not account for scr refresh
            SID_warn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SID_warn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SID_warn.started')
            SID_warn.setAutoDraw(True)
        if SID_warn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SID_warn.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                SID_warn.tStop = t  # not accounting for scr refresh
                SID_warn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SID_warn.stopped')
                SID_warn.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SID1_encodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SID1_encode" ---
    for thisComponent in SID1_encodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response2_2.keys in ['', [], None]:  # No response was made
        response2_2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response2_2.corr = 1;  # correct non-response
        else:
           response2_2.corr = 0;  # failed to respond (incorrectly)
    # store data for SID1_trials (TrialHandler)
    SID1_trials.addData('response2_2.keys',response2_2.keys)
    SID1_trials.addData('response2_2.corr', response2_2.corr)
    if response2_2.keys != None:  # we had a response
        SID1_trials.addData('response2_2.rt', response2_2.rt)
    # Run 'End Routine' code from SID1
    pressIndex = 1
    # the Routine "SID1_encode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "SID1_feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_4
    if response2_2.corr==1:
        feed_path1=feed
    if response2_2.corr==0:
        feed_path1=no_reward
    SID_feed1.setImage(feed_path1)
    # keep track of which components have finished
    SID1_feedbackComponents = [fix_SID1, SID_feed1]
    for thisComponent in SID1_feedbackComponents:
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
    
    # --- Run Routine "SID1_feedback" ---
    while continueRoutine and routineTimer.getTime() < 2.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_SID1* updates
        if fix_SID1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_SID1.frameNStart = frameN  # exact frame index
            fix_SID1.tStart = t  # local t and not account for scr refresh
            fix_SID1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_SID1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_SID1.started')
            fix_SID1.setAutoDraw(True)
        if fix_SID1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_SID1.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fix_SID1.tStop = t  # not accounting for scr refresh
                fix_SID1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_SID1.stopped')
                fix_SID1.setAutoDraw(False)
        # Run 'Each Frame' code from code_4
        if response2_2.keys:
            continueRoutine = True
        else:
            continueRoutine = False
        
        # *SID_feed1* updates
        if SID_feed1.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            SID_feed1.frameNStart = frameN  # exact frame index
            SID_feed1.tStart = t  # local t and not account for scr refresh
            SID_feed1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SID_feed1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SID_feed1.started')
            SID_feed1.setAutoDraw(True)
        if SID_feed1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SID_feed1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                SID_feed1.tStop = t  # not accounting for scr refresh
                SID_feed1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SID_feed1.stopped')
                SID_feed1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SID1_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SID1_feedback" ---
    for thisComponent in SID1_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.300000)
    
    # --- Prepare to start Routine "SID1_ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    SID1_ITIComponents = [fix_ITI_2]
    for thisComponent in SID1_ITIComponents:
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
    
    # --- Run Routine "SID1_ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_ITI_2* updates
        if fix_ITI_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_ITI_2.frameNStart = frameN  # exact frame index
            fix_ITI_2.tStart = t  # local t and not account for scr refresh
            fix_ITI_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_ITI_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_ITI_2.started')
            fix_ITI_2.setAutoDraw(True)
        if fix_ITI_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_ITI_2.tStartRefresh + random () +1.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_ITI_2.tStop = t  # not accounting for scr refresh
                fix_ITI_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_ITI_2.stopped')
                fix_ITI_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SID1_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SID1_ITI" ---
    for thisComponent in SID1_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "SID1_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'SID1_trials'

# get names of stimulus parameters
if SID1_trials.trialList in ([], [None], None):
    params = []
else:
    params = SID1_trials.trialList[0].keys()
# save data for this loop
SID1_trials.saveAsExcel(filename + '.xlsx', sheetName='SID1_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "SID_rest" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
SID_restComponents = [rest_2]
for thisComponent in SID_restComponents:
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

# --- Run Routine "SID_rest" ---
while continueRoutine and routineTimer.getTime() < 60.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_2* updates
    if rest_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        rest_2.frameNStart = frameN  # exact frame index
        rest_2.tStart = t  # local t and not account for scr refresh
        rest_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_2.started')
        rest_2.setAutoDraw(True)
    if rest_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_2.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            rest_2.tStop = t  # not accounting for scr refresh
            rest_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_2.stopped')
            rest_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SID_restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SID_rest" ---
for thisComponent in SID_restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-60.000000)

# --- Prepare to start Routine "MID2_instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
enter1_2.keys = []
enter1_2.rt = []
_enter1_2_allKeys = []
# keep track of which components have finished
MID2_instrComponents = [MID1_inst_2, enter1_2]
for thisComponent in MID2_instrComponents:
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

# --- Run Routine "MID2_instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *MID1_inst_2* updates
    if MID1_inst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MID1_inst_2.frameNStart = frameN  # exact frame index
        MID1_inst_2.tStart = t  # local t and not account for scr refresh
        MID1_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MID1_inst_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'MID1_inst_2.started')
        MID1_inst_2.setAutoDraw(True)
    
    # *enter1_2* updates
    waitOnFlip = False
    if enter1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter1_2.frameNStart = frameN  # exact frame index
        enter1_2.tStart = t  # local t and not account for scr refresh
        enter1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter1_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'enter1_2.started')
        enter1_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter1_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter1_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter1_2.status == STARTED and not waitOnFlip:
        theseKeys = enter1_2.getKeys(keyList=['space'], waitRelease=False)
        _enter1_2_allKeys.extend(theseKeys)
        if len(_enter1_2_allKeys):
            enter1_2.keys = _enter1_2_allKeys[-1].name  # just the last key pressed
            enter1_2.rt = _enter1_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MID2_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MID2_instr" ---
for thisComponent in MID2_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if enter1_2.keys in ['', [], None]:  # No response was made
    enter1_2.keys = None
thisExp.addData('enter1_2.keys',enter1_2.keys)
if enter1_2.keys != None:  # we had a response
    thisExp.addData('enter1_2.rt', enter1_2.rt)
thisExp.nextEntry()
# the Routine "MID2_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
MID2_trials = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('MID2.xlsx'),
    seed=None, name='MID2_trials')
thisExp.addLoop(MID2_trials)  # add the loop to the experiment
thisMID2_trial = MID2_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMID2_trial.rgb)
if thisMID2_trial != None:
    for paramName in thisMID2_trial:
        exec('{} = thisMID2_trial[paramName]'.format(paramName))

for thisMID2_trial in MID2_trials:
    currentLoop = MID2_trials
    # abbreviate parameter names if possible (e.g. rgb = thisMID2_trial.rgb)
    if thisMID2_trial != None:
        for paramName in thisMID2_trial:
            exec('{} = thisMID2_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "MID2_encode" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pra_code_4
    if trial_type==1 or trial_type==2: #金钱奖赏条件
          cue_path=mon_condition
    if trial_type==3 or trial_type==4: #无金钱奖赏条件
          cue_path=mon_no_condition
    if trial_type==5 or trial_type==6: #社会奖赏条件
          cue_path=soci_condition
    if trial_type==7 or trial_type==8: #无社会奖赏条件
          cue_path=soci_no_condition
    cue_4.setImage(cue_path)
    formal_target_3.setImage(images)
    response2_3.keys = []
    response2_3.rt = []
    _response2_3_allKeys = []
    # Run 'Begin Routine' code from MID2
    alarm = False
    # keep track of which components have finished
    MID2_encodeComponents = [fixation2_6, cue_4, fixation2_7, formal_target_3, response2_3, MID2_slow, MID2_warn]
    for thisComponent in MID2_encodeComponents:
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
    
    # --- Run Routine "MID2_encode" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2_6* updates
        if fixation2_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2_6.frameNStart = frameN  # exact frame index
            fixation2_6.tStart = t  # local t and not account for scr refresh
            fixation2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_6.started')
            fixation2_6.setAutoDraw(True)
        if fixation2_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_6.tStop = t  # not accounting for scr refresh
                fixation2_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_6.stopped')
                fixation2_6.setAutoDraw(False)
        
        # *cue_4* updates
        if cue_4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            cue_4.frameNStart = frameN  # exact frame index
            cue_4.tStart = t  # local t and not account for scr refresh
            cue_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue_4.started')
            cue_4.setAutoDraw(True)
        if cue_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_4.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_4.tStop = t  # not accounting for scr refresh
                cue_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue_4.stopped')
                cue_4.setAutoDraw(False)
        
        # *fixation2_7* updates
        if fixation2_7.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            fixation2_7.frameNStart = frameN  # exact frame index
            fixation2_7.tStart = t  # local t and not account for scr refresh
            fixation2_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_7.started')
            fixation2_7.setAutoDraw(True)
        if fixation2_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_7.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_7.tStop = t  # not accounting for scr refresh
                fixation2_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_7.stopped')
                fixation2_7.setAutoDraw(False)
        
        # *formal_target_3* updates
        if formal_target_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            formal_target_3.frameNStart = frameN  # exact frame index
            formal_target_3.tStart = t  # local t and not account for scr refresh
            formal_target_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_target_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_target_3.started')
            formal_target_3.setAutoDraw(True)
        if formal_target_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal_target_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                formal_target_3.tStop = t  # not accounting for scr refresh
                formal_target_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'formal_target_3.stopped')
                formal_target_3.setAutoDraw(False)
        
        # *response2_3* updates
        waitOnFlip = False
        if response2_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            response2_3.frameNStart = frameN  # exact frame index
            response2_3.tStart = t  # local t and not account for scr refresh
            response2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response2_3.started')
            response2_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response2_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response2_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response2_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                response2_3.tStop = t  # not accounting for scr refresh
                response2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response2_3.stopped')
                response2_3.status = FINISHED
        if response2_3.status == STARTED and not waitOnFlip:
            theseKeys = response2_3.getKeys(keyList=["f","j"], waitRelease=False)
            _response2_3_allKeys.extend(theseKeys)
            if len(_response2_3_allKeys):
                response2_3.keys = _response2_3_allKeys[-1].name  # just the last key pressed
                response2_3.rt = _response2_3_allKeys[-1].rt
                # was this correct?
                if (response2_3.keys == str(corrAns)) or (response2_3.keys == corrAns):
                    response2_3.corr = 1
                else:
                    response2_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from MID2
        if pressIndex == 1:
            MID2_warn.status = FINISHED
        else:
            alarm = True
        
        # *MID2_slow* updates
        if MID2_slow.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            MID2_slow.frameNStart = frameN  # exact frame index
            MID2_slow.tStart = t  # local t and not account for scr refresh
            MID2_slow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MID2_slow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'MID2_slow.started')
            MID2_slow.setAutoDraw(True)
        if MID2_slow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MID2_slow.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                MID2_slow.tStop = t  # not accounting for scr refresh
                MID2_slow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'MID2_slow.stopped')
                MID2_slow.setAutoDraw(False)
        
        # *MID2_warn* updates
        if MID2_warn.status == NOT_STARTED and alarm:
            # keep track of start time/frame for later
            MID2_warn.frameNStart = frameN  # exact frame index
            MID2_warn.tStart = t  # local t and not account for scr refresh
            MID2_warn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MID2_warn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'MID2_warn.started')
            MID2_warn.setAutoDraw(True)
        if MID2_warn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MID2_warn.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                MID2_warn.tStop = t  # not accounting for scr refresh
                MID2_warn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'MID2_warn.stopped')
                MID2_warn.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MID2_encodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "MID2_encode" ---
    for thisComponent in MID2_encodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response2_3.keys in ['', [], None]:  # No response was made
        response2_3.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response2_3.corr = 1;  # correct non-response
        else:
           response2_3.corr = 0;  # failed to respond (incorrectly)
    # store data for MID2_trials (TrialHandler)
    MID2_trials.addData('response2_3.keys',response2_3.keys)
    MID2_trials.addData('response2_3.corr', response2_3.corr)
    if response2_3.keys != None:  # we had a response
        MID2_trials.addData('response2_3.rt', response2_3.rt)
    # Run 'End Routine' code from MID2
    pressIndex = 1
    # the Routine "MID2_encode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "MID2_feed" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from setMsg_4
    if corrAns == 'f':
        if trial_type==1:
            if response2_3.corr==1:
                feedback_path2 = mon_feedback
        elif trial_type==3:
            if response2_3.corr==1:
                feedback_path2 = mon_no_feedback
    if response2_3.corr==0:
        feedback_path2 = mon_no_feedback
    
    if corrAns == 'j':
        if trial_type==2:
            if response2_3.corr==1:
                feedback_path2 = mon_feedback
        elif trial_type==4:
            if response2_3.corr==1:
                feedback_path2 = mon_no_feedback
    if response2_3.corr==0:
        feedback_path2 = mon_no_feedback
    formal_fe_3.setImage(feedback_path2)
    # keep track of which components have finished
    MID2_feedComponents = [MID2_polygon, formal_fe_3]
    for thisComponent in MID2_feedComponents:
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
    
    # --- Run Routine "MID2_feed" ---
    while continueRoutine and routineTimer.getTime() < 2.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *MID2_polygon* updates
        if MID2_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MID2_polygon.frameNStart = frameN  # exact frame index
            MID2_polygon.tStart = t  # local t and not account for scr refresh
            MID2_polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MID2_polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'MID2_polygon.started')
            MID2_polygon.setAutoDraw(True)
        if MID2_polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MID2_polygon.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                MID2_polygon.tStop = t  # not accounting for scr refresh
                MID2_polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'MID2_polygon.stopped')
                MID2_polygon.setAutoDraw(False)
        # Run 'Each Frame' code from setMsg_4
        if response2_3.keys:
            continueRoutine = True
        else:
            continueRoutine = False
        
        # *formal_fe_3* updates
        if formal_fe_3.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            formal_fe_3.frameNStart = frameN  # exact frame index
            formal_fe_3.tStart = t  # local t and not account for scr refresh
            formal_fe_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_fe_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_fe_3.started')
            formal_fe_3.setAutoDraw(True)
        if formal_fe_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal_fe_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                formal_fe_3.tStop = t  # not accounting for scr refresh
                formal_fe_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'formal_fe_3.stopped')
                formal_fe_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MID2_feedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "MID2_feed" ---
    for thisComponent in MID2_feedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.300000)
    
    # --- Prepare to start Routine "MID2_ITI_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    MID2_ITI_2Components = [fix_ITI_4]
    for thisComponent in MID2_ITI_2Components:
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
    
    # --- Run Routine "MID2_ITI_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_ITI_4* updates
        if fix_ITI_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_ITI_4.frameNStart = frameN  # exact frame index
            fix_ITI_4.tStart = t  # local t and not account for scr refresh
            fix_ITI_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_ITI_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_ITI_4.started')
            fix_ITI_4.setAutoDraw(True)
        if fix_ITI_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_ITI_4.tStartRefresh + random () +1.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_ITI_4.tStop = t  # not accounting for scr refresh
                fix_ITI_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_ITI_4.stopped')
                fix_ITI_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MID2_ITI_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "MID2_ITI_2" ---
    for thisComponent in MID2_ITI_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "MID2_ITI_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'MID2_trials'

# get names of stimulus parameters
if MID2_trials.trialList in ([], [None], None):
    params = []
else:
    params = MID2_trials.trialList[0].keys()
# save data for this loop
MID2_trials.saveAsExcel(filename + '.xlsx', sheetName='MID2_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "REST3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
REST3Components = [rest_3]
for thisComponent in REST3Components:
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

# --- Run Routine "REST3" ---
while continueRoutine and routineTimer.getTime() < 60.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_3* updates
    if rest_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        rest_3.frameNStart = frameN  # exact frame index
        rest_3.tStart = t  # local t and not account for scr refresh
        rest_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_3.started')
        rest_3.setAutoDraw(True)
    if rest_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_3.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            rest_3.tStop = t  # not accounting for scr refresh
            rest_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_3.stopped')
            rest_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in REST3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "REST3" ---
for thisComponent in REST3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-60.000000)

# --- Prepare to start Routine "SID2_instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
enter2_2.keys = []
enter2_2.rt = []
_enter2_2_allKeys = []
# keep track of which components have finished
SID2_instrComponents = [SID1_instr_2, enter2_2]
for thisComponent in SID2_instrComponents:
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

# --- Run Routine "SID2_instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SID1_instr_2* updates
    if SID1_instr_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        SID1_instr_2.frameNStart = frameN  # exact frame index
        SID1_instr_2.tStart = t  # local t and not account for scr refresh
        SID1_instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SID1_instr_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'SID1_instr_2.started')
        SID1_instr_2.setAutoDraw(True)
    
    # *enter2_2* updates
    waitOnFlip = False
    if enter2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        enter2_2.frameNStart = frameN  # exact frame index
        enter2_2.tStart = t  # local t and not account for scr refresh
        enter2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter2_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'enter2_2.started')
        enter2_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter2_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter2_2.status == STARTED and not waitOnFlip:
        theseKeys = enter2_2.getKeys(keyList=['space'], waitRelease=False)
        _enter2_2_allKeys.extend(theseKeys)
        if len(_enter2_2_allKeys):
            enter2_2.keys = _enter2_2_allKeys[-1].name  # just the last key pressed
            enter2_2.rt = _enter2_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SID2_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SID2_instr" ---
for thisComponent in SID2_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if enter2_2.keys in ['', [], None]:  # No response was made
    enter2_2.keys = None
thisExp.addData('enter2_2.keys',enter2_2.keys)
if enter2_2.keys != None:  # we had a response
    thisExp.addData('enter2_2.rt', enter2_2.rt)
thisExp.nextEntry()
# the Routine "SID2_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SID_trial2 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SID2.xlsx'),
    seed=None, name='SID_trial2')
thisExp.addLoop(SID_trial2)  # add the loop to the experiment
thisSID_trial2 = SID_trial2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSID_trial2.rgb)
if thisSID_trial2 != None:
    for paramName in thisSID_trial2:
        exec('{} = thisSID_trial2[paramName]'.format(paramName))

for thisSID_trial2 in SID_trial2:
    currentLoop = SID_trial2
    # abbreviate parameter names if possible (e.g. rgb = thisSID_trial2.rgb)
    if thisSID_trial2 != None:
        for paramName in thisSID_trial2:
            exec('{} = thisSID_trial2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SID2_enc" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pra_code_5
    if trial_type==5 or trial_type==6: #社会奖赏条件
          cue_path=soci_condition
    if trial_type==7 or trial_type==8: #无社会奖赏条件
          cue_path=soci_no_condition
    cue_5.setImage(cue_path)
    formal_target_4.setImage(images)
    response2_4.keys = []
    response2_4.rt = []
    _response2_4_allKeys = []
    # Run 'Begin Routine' code from SID2
    alarm = False
    # keep track of which components have finished
    SID2_encComponents = [fixation2_5, cue_5, fixation2_8, formal_target_4, response2_4, SID2_slow, SID2_warn]
    for thisComponent in SID2_encComponents:
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
    
    # --- Run Routine "SID2_enc" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2_5* updates
        if fixation2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2_5.frameNStart = frameN  # exact frame index
            fixation2_5.tStart = t  # local t and not account for scr refresh
            fixation2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_5.started')
            fixation2_5.setAutoDraw(True)
        if fixation2_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_5.tStop = t  # not accounting for scr refresh
                fixation2_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_5.stopped')
                fixation2_5.setAutoDraw(False)
        
        # *cue_5* updates
        if cue_5.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            cue_5.frameNStart = frameN  # exact frame index
            cue_5.tStart = t  # local t and not account for scr refresh
            cue_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue_5.started')
            cue_5.setAutoDraw(True)
        if cue_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_5.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_5.tStop = t  # not accounting for scr refresh
                cue_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue_5.stopped')
                cue_5.setAutoDraw(False)
        
        # *fixation2_8* updates
        if fixation2_8.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            fixation2_8.frameNStart = frameN  # exact frame index
            fixation2_8.tStart = t  # local t and not account for scr refresh
            fixation2_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_8.started')
            fixation2_8.setAutoDraw(True)
        if fixation2_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_8.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_8.tStop = t  # not accounting for scr refresh
                fixation2_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_8.stopped')
                fixation2_8.setAutoDraw(False)
        
        # *formal_target_4* updates
        if formal_target_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            formal_target_4.frameNStart = frameN  # exact frame index
            formal_target_4.tStart = t  # local t and not account for scr refresh
            formal_target_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_target_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_target_4.started')
            formal_target_4.setAutoDraw(True)
        if formal_target_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal_target_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                formal_target_4.tStop = t  # not accounting for scr refresh
                formal_target_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'formal_target_4.stopped')
                formal_target_4.setAutoDraw(False)
        
        # *response2_4* updates
        waitOnFlip = False
        if response2_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            response2_4.frameNStart = frameN  # exact frame index
            response2_4.tStart = t  # local t and not account for scr refresh
            response2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response2_4.started')
            response2_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response2_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response2_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response2_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response2_4.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                response2_4.tStop = t  # not accounting for scr refresh
                response2_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response2_4.stopped')
                response2_4.status = FINISHED
        if response2_4.status == STARTED and not waitOnFlip:
            theseKeys = response2_4.getKeys(keyList=["f","j"], waitRelease=False)
            _response2_4_allKeys.extend(theseKeys)
            if len(_response2_4_allKeys):
                response2_4.keys = _response2_4_allKeys[-1].name  # just the last key pressed
                response2_4.rt = _response2_4_allKeys[-1].rt
                # was this correct?
                if (response2_4.keys == str(corrAns)) or (response2_4.keys == corrAns):
                    response2_4.corr = 1
                else:
                    response2_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from SID2
        if pressIndex == 1:
            SID2_warn.status = FINISHED
        else:
            alarm = True
        
        # *SID2_slow* updates
        if SID2_slow.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            SID2_slow.frameNStart = frameN  # exact frame index
            SID2_slow.tStart = t  # local t and not account for scr refresh
            SID2_slow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SID2_slow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SID2_slow.started')
            SID2_slow.setAutoDraw(True)
        if SID2_slow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SID2_slow.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                SID2_slow.tStop = t  # not accounting for scr refresh
                SID2_slow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SID2_slow.stopped')
                SID2_slow.setAutoDraw(False)
        
        # *SID2_warn* updates
        if SID2_warn.status == NOT_STARTED and alarm:
            # keep track of start time/frame for later
            SID2_warn.frameNStart = frameN  # exact frame index
            SID2_warn.tStart = t  # local t and not account for scr refresh
            SID2_warn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SID2_warn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SID2_warn.started')
            SID2_warn.setAutoDraw(True)
        if SID2_warn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SID2_warn.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                SID2_warn.tStop = t  # not accounting for scr refresh
                SID2_warn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SID2_warn.stopped')
                SID2_warn.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SID2_encComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SID2_enc" ---
    for thisComponent in SID2_encComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response2_4.keys in ['', [], None]:  # No response was made
        response2_4.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response2_4.corr = 1;  # correct non-response
        else:
           response2_4.corr = 0;  # failed to respond (incorrectly)
    # store data for SID_trial2 (TrialHandler)
    SID_trial2.addData('response2_4.keys',response2_4.keys)
    SID_trial2.addData('response2_4.corr', response2_4.corr)
    if response2_4.keys != None:  # we had a response
        SID_trial2.addData('response2_4.rt', response2_4.rt)
    # Run 'End Routine' code from SID2
    pressIndex = 1
    # the Routine "SID2_enc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "SID2_fee" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_6
    if response2_4.corr==1:
        feed_path2=feed
    if response2_4.corr==0:
        feed_path2=no_reward
    SID_feed1_2.setImage(feed_path2)
    # keep track of which components have finished
    SID2_feeComponents = [fix_SID1_2, SID_feed1_2]
    for thisComponent in SID2_feeComponents:
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
    
    # --- Run Routine "SID2_fee" ---
    while continueRoutine and routineTimer.getTime() < 2.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_SID1_2* updates
        if fix_SID1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_SID1_2.frameNStart = frameN  # exact frame index
            fix_SID1_2.tStart = t  # local t and not account for scr refresh
            fix_SID1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_SID1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_SID1_2.started')
            fix_SID1_2.setAutoDraw(True)
        if fix_SID1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_SID1_2.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fix_SID1_2.tStop = t  # not accounting for scr refresh
                fix_SID1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_SID1_2.stopped')
                fix_SID1_2.setAutoDraw(False)
        # Run 'Each Frame' code from code_6
        if response2_4.keys:
            continueRoutine = True
        else:
            continueRoutine = False
        
        # *SID_feed1_2* updates
        if SID_feed1_2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            SID_feed1_2.frameNStart = frameN  # exact frame index
            SID_feed1_2.tStart = t  # local t and not account for scr refresh
            SID_feed1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SID_feed1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SID_feed1_2.started')
            SID_feed1_2.setAutoDraw(True)
        if SID_feed1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SID_feed1_2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                SID_feed1_2.tStop = t  # not accounting for scr refresh
                SID_feed1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SID_feed1_2.stopped')
                SID_feed1_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SID2_feeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SID2_fee" ---
    for thisComponent in SID2_feeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.300000)
    
    # --- Prepare to start Routine "SID2_ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    SID2_ITIComponents = [fix_ITI_5]
    for thisComponent in SID2_ITIComponents:
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
    
    # --- Run Routine "SID2_ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_ITI_5* updates
        if fix_ITI_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_ITI_5.frameNStart = frameN  # exact frame index
            fix_ITI_5.tStart = t  # local t and not account for scr refresh
            fix_ITI_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_ITI_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_ITI_5.started')
            fix_ITI_5.setAutoDraw(True)
        if fix_ITI_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_ITI_5.tStartRefresh + random () +1.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_ITI_5.tStop = t  # not accounting for scr refresh
                fix_ITI_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_ITI_5.stopped')
                fix_ITI_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SID2_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SID2_ITI" ---
    for thisComponent in SID2_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "SID2_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'SID_trial2'

# get names of stimulus parameters
if SID_trial2.trialList in ([], [None], None):
    params = []
else:
    params = SID_trial2.trialList[0].keys()
# save data for this loop
SID_trial2.saveAsExcel(filename + '.xlsx', sheetName='SID_trial2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('JY.xlsx'),
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
    
    # --- Prepare to start Routine "jin_encd" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pra_code_7
    if trial_type==1 or trial_type==2: #金钱奖赏条件
          cue_path=mon_condition
    if trial_type==3 or trial_type==4: #无金钱奖赏条件
          cue_path=mon_no_condition
    if trial_type==5 or trial_type==6: #社会奖赏条件
          cue_path=soci_condition
    if trial_type==7 or trial_type==8: #无社会奖赏条件
          cue_path=soci_no_condition
    cue_7.setImage(cue_path)
    formal_target_6.setImage(images)
    response2_6.keys = []
    response2_6.rt = []
    _response2_6_allKeys = []
    # Run 'Begin Routine' code from jin
    alarm = False
    # keep track of which components have finished
    jin_encdComponents = [fixation2_15, cue_7, fixation2_16, formal_target_6, response2_6, jin_slow, jin_warn]
    for thisComponent in jin_encdComponents:
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
    
    # --- Run Routine "jin_encd" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2_15* updates
        if fixation2_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2_15.frameNStart = frameN  # exact frame index
            fixation2_15.tStart = t  # local t and not account for scr refresh
            fixation2_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_15.started')
            fixation2_15.setAutoDraw(True)
        if fixation2_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_15.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_15.tStop = t  # not accounting for scr refresh
                fixation2_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_15.stopped')
                fixation2_15.setAutoDraw(False)
        
        # *cue_7* updates
        if cue_7.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            cue_7.frameNStart = frameN  # exact frame index
            cue_7.tStart = t  # local t and not account for scr refresh
            cue_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue_7.started')
            cue_7.setAutoDraw(True)
        if cue_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_7.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_7.tStop = t  # not accounting for scr refresh
                cue_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue_7.stopped')
                cue_7.setAutoDraw(False)
        
        # *fixation2_16* updates
        if fixation2_16.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            fixation2_16.frameNStart = frameN  # exact frame index
            fixation2_16.tStart = t  # local t and not account for scr refresh
            fixation2_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2_16.started')
            fixation2_16.setAutoDraw(True)
        if fixation2_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2_16.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation2_16.tStop = t  # not accounting for scr refresh
                fixation2_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2_16.stopped')
                fixation2_16.setAutoDraw(False)
        
        # *formal_target_6* updates
        if formal_target_6.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            formal_target_6.frameNStart = frameN  # exact frame index
            formal_target_6.tStart = t  # local t and not account for scr refresh
            formal_target_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_target_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_target_6.started')
            formal_target_6.setAutoDraw(True)
        if formal_target_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal_target_6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                formal_target_6.tStop = t  # not accounting for scr refresh
                formal_target_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'formal_target_6.stopped')
                formal_target_6.setAutoDraw(False)
        
        # *response2_6* updates
        waitOnFlip = False
        if response2_6.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            response2_6.frameNStart = frameN  # exact frame index
            response2_6.tStart = t  # local t and not account for scr refresh
            response2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response2_6.started')
            response2_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response2_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response2_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response2_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response2_6.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                response2_6.tStop = t  # not accounting for scr refresh
                response2_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response2_6.stopped')
                response2_6.status = FINISHED
        if response2_6.status == STARTED and not waitOnFlip:
            theseKeys = response2_6.getKeys(keyList=["f","j"], waitRelease=False)
            _response2_6_allKeys.extend(theseKeys)
            if len(_response2_6_allKeys):
                response2_6.keys = _response2_6_allKeys[-1].name  # just the last key pressed
                response2_6.rt = _response2_6_allKeys[-1].rt
                # was this correct?
                if (response2_6.keys == str(corrAns)) or (response2_6.keys == corrAns):
                    response2_6.corr = 1
                else:
                    response2_6.corr = 0
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from jin
        if pressIndex == 1:
            jin_warn.status = FINISHED
        else:
            alarm = True
        
        # *jin_slow* updates
        if jin_slow.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            jin_slow.frameNStart = frameN  # exact frame index
            jin_slow.tStart = t  # local t and not account for scr refresh
            jin_slow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jin_slow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jin_slow.started')
            jin_slow.setAutoDraw(True)
        if jin_slow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jin_slow.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                jin_slow.tStop = t  # not accounting for scr refresh
                jin_slow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'jin_slow.stopped')
                jin_slow.setAutoDraw(False)
        
        # *jin_warn* updates
        if jin_warn.status == NOT_STARTED and alarm:
            # keep track of start time/frame for later
            jin_warn.frameNStart = frameN  # exact frame index
            jin_warn.tStart = t  # local t and not account for scr refresh
            jin_warn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jin_warn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jin_warn.started')
            jin_warn.setAutoDraw(True)
        if jin_warn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jin_warn.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                jin_warn.tStop = t  # not accounting for scr refresh
                jin_warn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'jin_warn.stopped')
                jin_warn.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jin_encdComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "jin_encd" ---
    for thisComponent in jin_encdComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response2_6.keys in ['', [], None]:  # No response was made
        response2_6.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response2_6.corr = 1;  # correct non-response
        else:
           response2_6.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('response2_6.keys',response2_6.keys)
    trials_2.addData('response2_6.corr', response2_6.corr)
    if response2_6.keys != None:  # we had a response
        trials_2.addData('response2_6.rt', response2_6.rt)
    # Run 'End Routine' code from jin
    pressIndex = 1
    # the Routine "jin_encd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "jin_feed" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from setMsg_6
    if response2_6.corr==1:
        feed_path3=fee
    if response2_6.corr==0:
        feed_path3=no_re
    formal_fe_5.setImage(feed_path3)
    # keep track of which components have finished
    jin_feedComponents = [JIN_polygon, formal_fe_5]
    for thisComponent in jin_feedComponents:
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
    
    # --- Run Routine "jin_feed" ---
    while continueRoutine and routineTimer.getTime() < 2.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *JIN_polygon* updates
        if JIN_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            JIN_polygon.frameNStart = frameN  # exact frame index
            JIN_polygon.tStart = t  # local t and not account for scr refresh
            JIN_polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(JIN_polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'JIN_polygon.started')
            JIN_polygon.setAutoDraw(True)
        if JIN_polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > JIN_polygon.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                JIN_polygon.tStop = t  # not accounting for scr refresh
                JIN_polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'JIN_polygon.stopped')
                JIN_polygon.setAutoDraw(False)
        # Run 'Each Frame' code from setMsg_6
        if response2_6.keys:
            continueRoutine = True
        else:
            continueRoutine = False
        
        # *formal_fe_5* updates
        if formal_fe_5.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            formal_fe_5.frameNStart = frameN  # exact frame index
            formal_fe_5.tStart = t  # local t and not account for scr refresh
            formal_fe_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_fe_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_fe_5.started')
            formal_fe_5.setAutoDraw(True)
        if formal_fe_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > formal_fe_5.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                formal_fe_5.tStop = t  # not accounting for scr refresh
                formal_fe_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'formal_fe_5.stopped')
                formal_fe_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jin_feedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "jin_feed" ---
    for thisComponent in jin_feedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.300000)
    
    # --- Prepare to start Routine "jinITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    jinITIComponents = [fix_ITI_7]
    for thisComponent in jinITIComponents:
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
    
    # --- Run Routine "jinITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_ITI_7* updates
        if fix_ITI_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_ITI_7.frameNStart = frameN  # exact frame index
            fix_ITI_7.tStart = t  # local t and not account for scr refresh
            fix_ITI_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_ITI_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_ITI_7.started')
            fix_ITI_7.setAutoDraw(True)
        if fix_ITI_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_ITI_7.tStartRefresh + random () +1.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_ITI_7.tStop = t  # not accounting for scr refresh
                fix_ITI_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_ITI_7.stopped')
                fix_ITI_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jinITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "jinITI" ---
    for thisComponent in jinITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "jinITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "thanks" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
the_end.keys = []
the_end.rt = []
_the_end_allKeys = []
# keep track of which components have finished
thanksComponents = [end, the_end]
for thisComponent in thanksComponents:
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

# --- Run Routine "thanks" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end* updates
    if end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end.frameNStart = frameN  # exact frame index
        end.tStart = t  # local t and not account for scr refresh
        end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end.started')
        end.setAutoDraw(True)
    
    # *the_end* updates
    waitOnFlip = False
    if the_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        the_end.frameNStart = frameN  # exact frame index
        the_end.tStart = t  # local t and not account for scr refresh
        the_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(the_end, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'the_end.started')
        the_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(the_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(the_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if the_end.status == STARTED and not waitOnFlip:
        theseKeys = the_end.getKeys(keyList=['space'], waitRelease=False)
        _the_end_allKeys.extend(theseKeys)
        if len(_the_end_allKeys):
            the_end.keys = _the_end_allKeys[-1].name  # just the last key pressed
            the_end.rt = _the_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thanks" ---
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if the_end.keys in ['', [], None]:  # No response was made
    the_end.keys = None
thisExp.addData('the_end.keys',the_end.keys)
if the_end.keys != None:  # we had a response
    thisExp.addData('the_end.rt', the_end.rt)
thisExp.nextEntry()
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
