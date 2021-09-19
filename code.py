import board
import time
import terminalio
from digitalio import DigitalInOut, Pull
from adafruit_debouncer import Debouncer
from adafruit_matrixportal.matrixportal import MatrixPortal

# Modules
from cupid.cupid import Cupid

# Hardware initialization
pin_down = DigitalInOut(board.BUTTON_DOWN)
pin_down.switch_to_input(pull=Pull.UP)


DEBUG_MODE = False


# Constants
SLEEP_DURATION = 4*3600

# Variables
refresh_time = None

####################
###### Modules #####
####################

# Names
modules = {
  "cupid": 0,
}

# Initializers
cupid = Cupid()

# Active module controller
active_module = 0
change_module = False

################
##### Main #####
################

matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=DEBUG_MODE)

# Create the message label with the color and text selected
matrixportal.add_text(
    text_font="/fonts/GrechenFuemen-Regular-24.bdf",
    text_position=(0, (matrixportal.graphics.display.height // 2) - 5),
    scrolling=True,
)

# Create the static 'Connecting' text label
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(2, (matrixportal.graphics.display.height // 2) - 1),
    text_color=0x3d1f5c,
    text_scale=0,
)

##### Functions #####

# Refresh the display
def refresh_display():
    if active_module == modules["cupid"]:
        if(DEBUG_MODE): print('refreshing cupid')
        cupid.refresh(matrixportal)


# Update modules data
def update_modules():    
    try:
        matrixportal.set_text("Connecting...", 1)
        matrixportal.network.connect()
        cupid.update(matrixportal)
        matrixportal.set_text(" ", 1)

    except (ValueError, RuntimeError) as e:
        matrixportal.set_text(e, 1)


refresh_time = time.monotonic()
update_modules()
refresh_display()


################
##### Loop #####
################

while True:
    current_time = time.monotonic()

    if (current_time - refresh_time) > SLEEP_DURATION:
        refresh_time = time.monotonic()
        update_modules()
        refresh_display()

    # Force refresh with down button press
    if not pin_down.value:
        refresh_time = time.monotonic()
        update_modules()
        refresh_display()
    
    matrixportal.scroll_text(frame_delay=0.05)
    
