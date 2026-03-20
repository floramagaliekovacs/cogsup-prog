# Michottean launching 

# Import the main modules of expyriment
from expyriment import design, control, stimuli
# control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two Square")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create green and red squares and Set positions (separate by 200 pixels)
square = stimuli.Rectangle(size=(50,50), colour=(0,255,0))  # green
square2 = stimuli.Rectangle(size=(50, 50), colour = (255,0,0), position=(-450,0))  # red

# Start running the experiment
control.start(subject_id=1)

# Display both squares until key is pressed
square.present(clear=True, update=False)
square2.present(clear=False, update=True)
exp.clock.wait(1000)

# move red square until it reaches green square, 20 pixels at a time
for i in range(40):
    i += 1
    square2.position = (-450+10*i,0)
    square2.present(clear=True, update=False)
    square.present(clear=False, update=True)
    exp.clock.wait(20)

# after 'collision', move green square to the right by 450 pixels
for k in range(40):
    k += 1
    square.position = (0+10*k,0)
    square.present(clear=True, update=False)
    square2.present(clear=False, update=True)
    exp.clock.wait(20)

# End the current session and quit expyriment
control.end()

