# text from https://microbit-micropython.readthedocs.io/en/latest/microbit_micropython_api.html

from typing import List, Any, overload

def sleep(ms: int):
    """sleep for the given number of milliseconds."""

def running_time() -> int:
    """returns the number of milliseconds since the micro:bit was last switched on."""

def panic(error_code: int):
   """makes the micro:bit enter panic mode (this usually happens when the DAL runs out of memory, and causes a sad face to be drawn on the display). The error # code can be any arbitrary integer value."""

def reset():
    """resets the micro:bit."""

class Button:
    def is_pressed(self) -> bool:
        """returns True or False to indicate if the button is pressed at the time of the method call."""
    def was_pressed(self) -> bool:
        """returns True or False to indicate if the button was pressed since the device started or the last time this method was called."""
    def get_presses(self) -> int:
        """returns the running total of button presses, and resets this counter to zero"""

button_a: Button
button_b: Button

class Display:
    def get_pixel(self, x: int, y: int) -> int:
        """Get the brightness the brightness of the pixel (x,y). Brightness can be from 0 (the pixel is off) to 9 (the pixel is at maximum brightness)."""
    def set_pixel(self, x: int, y: int, val: int):
        """sets the brightness of the pixel (x,y) to val (between 0 [off] and 9 [max brightness], inclusive)."""
    def clear(self):
        """clears the display."""
    def show(self, image, delay: int = 0, wait: bool = True, loop: bool = False, clear: bool = False):
        """shows the image."""
    def show(self, iterable: Any, delay: int = 400, wait: bool = True, loop: bool = False, clear: bool = False):
        """shows each image or letter in the iterable, with delay ms. in between each."""
    def scroll(self, string: str, delay: int = 400):
        """scrolls a string across the display (more exciting than display.show for written messages)."""

display: Display

class MicroBitPin:
    def write_digital(self, value: int):
        """value can be 0, 1, False, True"""
    def read_digital(self) -> int:
        """returns either 1 or 0"""
    def write_analog(self, value: int):
        """value is between 0 and 1023"""
    def read_analog(self) -> int:
        """returns an integer between 0 and 1023"""
    def set_analog_period(self, int):
        """sets the period of the PWM output of the pin in milliseconds (see https://en.wikipedia.org/wiki/Pulse-width_modulation)"""
    def set_analog_period_microseconds(self, int):
        """sets the period of the PWM output of the pin in microseconds (see https://en.wikipedia.org/wiki/Pulse-width_modulation)"""
    def is_touched(self) -> bool:
        """"""

pin1: MicroBitPin
pin2: MicroBitPin
pin3: MicroBitPin
pin4: MicroBitPin
pin5: MicroBitPin
pin6: MicroBitPin
pin7: MicroBitPin
pin8: MicroBitPin
pin9: MicroBitPin
pin10: MicroBitPin
pin11: MicroBitPin
pin12: MicroBitPin
pin13: MicroBitPin
pin14: MicroBitPin
pin15: MicroBitPin
pin16: MicroBitPin
pin19: MicroBitPin
pin20: MicroBitPin

# to do: Images

class Image:
    """
    The Image class is used to create images that can be displayed easily on the device’s LED matrix. Given an image object it’s possible to display it via the display API:
    
        display.show(Image.HAPPY)
    """
    HEART: 'Image'
    HEART_SMALL: 'Image'
    HAPPY: 'Image'
    SMILE: 'Image'
    SAD: 'Image'
    CONFUSED: 'Image'
    ANGRY: 'Image'
    ASLEEP: 'Image'
    SURPRISED: 'Image'
    SILLY: 'Image'
    FABULOUS: 'Image'
    MEH: 'Image'
    YES: 'Image'
    NO: 'Image'
    CLOCK12: 'Image'
    CLOCK11: 'Image'
    CLOCK10: 'Image'
    CLOCK9: 'Image'
    CLOCK8: 'Image'
    CLOCK7: 'Image'
    CLOCK6: 'Image'
    CLOCK5: 'Image'
    CLOCK4: 'Image'
    CLOCK3: 'Image'
    CLOCK2: 'Image'
    CLOCK1: 'Image'
    ARROW_N: 'Image'
    ARROW_NE: 'Image'
    ARROW_E: 'Image'
    ARROW_SE: 'Image'
    ARROW_S: 'Image'
    ARROW_SW: 'Image'
    ARROW_W: 'Image'
    ARROW_NW: 'Image'
    TRIANGLE: 'Image'
    TRIANGLE_LEFT: 'Image'
    CHESSBOARD: 'Image'
    DIAMOND: 'Image'
    DIAMOND_SMALL: 'Image'
    SQUARE: 'Image'
    SQUARE_SMALL: 'Image'
    RABBIT: 'Image'
    COW: 'Image'
    MUSIC_CROTCHET: 'Image'
    MUSIC_QUAVER: 'Image'
    MUSIC_QUAVERS: 'Image'
    PITCHFORK: 'Image'
    XMAS: 'Image'
    PACMAN: 'Image'
    TARGET: 'Image'
    TSHIRT: 'Image'
    ROLLERSKATE: 'Image'
    DUCK: 'Image'
    HOUSE: 'Image'
    TORTOISE: 'Image'
    BUTTERFLY: 'Image'
    STICKFIGURE: 'Image'
    GHOST: 'Image'
    SWORD: 'Image'
    GIRAFFE: 'Image'
    SKULL: 'Image'
    UMBRELLA: 'Image'
    SNAKE: 'Image'

    ALL_CLOCKS: List['Image']
    ALL_ARROWS: List['Image']

    @overload
    def __init__(self, string: str) -> None:
        """If `string` is used, it has to consist of digits 0-9 arranged into lines, describing the image, for example:
            image = Image("90009:"
                          "09090:"
                          "00900:"
                          "09090:"
                          "90009")
        will create a 5×5 image of an X.
        The end of a line is indicated by a colon.
        It’s also possible to use a newline (n) to indicate the end of a line like this:
            image = Image("90009\n"
                          "09090\n"
                          "00900\n"
                          "09090\n"
                          "90009")
        """

    @overload
    def __init__(self, width: int = None, height: int = None, buffer: Any = None) -> None:
        """Creates an empty image with `width` columns and `height` rows.
        Optionally `buffer` can be an array of `width * height` integers in range 0-9 to initialize the image:
            Image(2, 2, b'\x08\x08\x08\x08')
        or
            Image(2, 2, bytearray([9,9,9,9]))
        will create a 2 x 2 pixel image at full brightness.
        """
    def width(self) -> int:
        """Return the number of columns in the image."""
    def height(self) -> int:
        """Return the numbers of rows in the image."""
    def set_pixel(self, x, y, value):
        """Set the brightness of the pixel at column `x` and row `y` to the value, which has to be between 0 (dark) and 9 (bright).
        This method will raise an exception when called on any of the built-in read-only images, like `Image.HEART`."""

# to do: The accelerometer
# to do: The compass
# to do: I2C bus
# to do: UART
