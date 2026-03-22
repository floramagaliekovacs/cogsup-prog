# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY
control.set_develop_mode()

# Create an object of class Experiment, set background to grey
exp = design.Experiment(name = "kanizsa square", background_colour = C_GREY)

# Initialize the experiment
control.initialize(exp)

# get screen width, height 
width, height = exp.screen.size

side = width*0.25

# create stimuli 
upper_left = stimuli.Circle(colour = (0,0,0,), radius = width*0.05, position = (-side/2, side/2))
upper_right = stimuli.Circle(colour = (0,0,0), radius = width*0.05, position = (side/2, side/2))
lower_left = stimuli.Circle(colour = (255,255,255), radius = width*0.05, position = (-side/2, -side/2))
lower_right = stimuli.Circle(colour = (255,255,255), radius = width*0.05, position = (side/2, -side/2))

square = stimuli.Rectangle(size = (side, side), colour = C_GREY)

# Start running the experiment
control.start(subject_id=1)

# Present all stimuli until key is pressed
upper_left.present(clear=True, update=False)
upper_right.present(clear=False, update=False)
lower_left.present(clear=False, update=False)
lower_right.present(clear=False, update=False)
square.present(clear=False, update=True)
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()