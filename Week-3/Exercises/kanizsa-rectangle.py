# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY
control.set_develop_mode()

# Create an object of class Experiment, set background to grey
exp = design.Experiment(name = "kanizsa rectangle", background_colour = C_GREY)

# Initialize the experiment
control.initialize(exp)

# get screen width, height 
width, height = exp.screen.size

def create_kanizsa_rectangle(aspect_ratio, scale_rectangle, scale_circle):
    # returns something

    rect_width = width // scale_rectangle
    rect_height = height // aspect_ratio

    # CIRCLES
    r = width // scale_circle   # take floor
    upper_left = stimuli.Circle(colour = (0,0,0,), radius = r , position = (-rect_width/2, rect_height/2))
    upper_right = stimuli.Circle(colour = (0,0,0), radius = r, position = (rect_width/2, rect_height/2))
    lower_left = stimuli.Circle(colour = (255,255,255), radius = r, position = (-rect_width/2, -rect_height/2))
    lower_right = stimuli.Circle(colour = (255,255,255), radius = r, position = (rect_width/2, -rect_height/2))

    # RECTANGLE 
    rectangle = stimuli.Rectangle(size = (rect_width, rect_height), colour = C_GREY)

    return(upper_left, upper_right, lower_left, lower_right, rectangle)

upper_left, upper_right, lower_left, lower_right, rectangle = create_kanizsa_rectangle(2, 2, 10)

# Start running the experiment
control.start(subject_id=1)

# Present all stimuli until key is pressed
upper_left.present(clear=True, update=False)
upper_right.present(clear=False, update=False)
lower_left.present(clear=False, update=False)
lower_right.present(clear=False, update=False)
rectangle.present(clear=False, update=True)
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()