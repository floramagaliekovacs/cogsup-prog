# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Display edges")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# get screen width, height 
width, height = exp.screen.size

side = width*0.05

# create stimuli (one square in each corner)
upper_left = stimuli.Rectangle( size= (side, side), line_width=1, colour = (255,0,0), position = ((-width+side)/2 , (height-side)/2))
upper_right = stimuli.Rectangle(size= (side, side), line_width=1, colour = (255,0,0), position = ((width-side)/2 , (height-side)/2))
lower_left = stimuli.Rectangle(size= (side, side), line_width=1, colour = (255,0,0), position = ((-width+side)/2, (-height+side)/2))
lower_right = stimuli.Rectangle(size= (side, side), line_width=1, colour = (255,0,0), position = ((width-side)/2 , (-height+side)/2))


# Start running the experiment
control.start(subject_id=1)

# Pesent all stimuli until key is pressed
upper_left.present(clear=True, update=False)
upper_right.present(clear=False, update=False)
lower_left.present(clear=False, update=False)
lower_right.present(clear=False, update=True)
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()
