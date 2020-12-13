# text from https://microbit-micropython.readthedocs.io/en/latest/microbit_micropython_api.html

from collections.abc import Iterable
from typing import Union, Literal

digitalValue = Union[Literal[1], Literal[0]]

def sleep(ms: int):
    """sleep for the given number of milliseconds."""

def running_time() -> int:
    """returns the number of milliseconds since the micro:bit was last switched on."""

def panic(error_code: int):
   """makes the micro:bit enter panic mode (this usually happens when the DAL runs out of memory, and causes a sad face to be drawn on the display). The error # code can be any arbitrary integer value."""

def reset():
    """resets the micro:bit."""

class _Button:
    def is_pressed(self) -> bool:
        """returns True or False to indicate if the button is pressed at the time of the method call."""
    def was_pressed(self) -> bool:
        """returns True or False to indicate if the button was pressed since the device started or the last time this method was called."""
    def get_presses(self) -> int:
        """returns the running total of button presses, and resets this counter to zero"""

button_a = _Button()
button_b = _Button()

class _Display:
    def get_pixel(self, x: int, y: int) -> int:
        """Get the brightness the brightness of the pixel (x,y). Brightness can be from 0 (the pixel is off) to 9 (the pixel is at maximum brightness)."""
    def set_pixel(self, x: int, y: int, val: int):
        """sets the brightness of the pixel (x,y) to val (between 0 [off] and 9 [max brightness], inclusive)."""
    def clear(self):
        """clears the display."""
    def show(self, image, delay: int = 0, wait: bool = True, loop: bool = False, clear: bool = False):
        """shows the image."""
    def show(self, iterable: Iterable, delay: int = 400, wait: bool = True, loop: bool = False, clear: bool = False):
        """shows each image or letter in the iterable, with delay ms. in between each."""
    def scroll(self, string: str, delay: int = 400):
        """scrolls a string across the display (more exciting than display.show for written messages)."""

display = _Display()

class _MicroBitPin:
    def write_digital(self, value: Union[bool, digitalValue]):
        """value can be 0, 1, False, True"""
    def read_digital(self) -> digitalValue:
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

pin1 = _MicroBitPin()
pin2 = _MicroBitPin()
pin3 = _MicroBitPin()
pin4 = _MicroBitPin()
pin5 = _MicroBitPin()
pin6 = _MicroBitPin()
pin7 = _MicroBitPin()
pin8 = _MicroBitPin()
pin9 = _MicroBitPin()
pin10 = _MicroBitPin()
pin11 = _MicroBitPin()
pin12 = _MicroBitPin()
pin13 = _MicroBitPin()
pin14 = _MicroBitPin()
pin15 = _MicroBitPin()
pin16 = _MicroBitPin()
pin19 = _MicroBitPin()
pin20 = _MicroBitPin()

# to do: Images
# to do: The accelerometer
# to do: The compass
# to do: I2C bus
# to do: UART
