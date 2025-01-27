import sys

from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from current_weather import CurrentWeather

class DisplayTemperature:
    def __init__(self, cur_weather: CurrentWeather):
        self._temp: str = f"{str(cur_weather.get_current_temp())}°"
        self._condition: str = cur_weather.get_current_condition()
    
    def draw_temp(self) -> None:
        # Initialize the display
        inky_display = auto()
        inky_display.set_border(inky_display.WHITE)

        img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        # Add the main temperature to the display

        font = ImageFont.truetype("FredokaOne-Regular.ttf", 60)
        _, _, w, h = font.getbbox(self._temp)
        x = 20
        y = 20

        draw.text((x, y), self._temp, inky_display.BLACK, font)

        # Add the current condition

        condition_font = ImageFont.truetype("FredokaOne-Regular.ttf", 24)
        _, _, w, h, = font.getbbox(self._condition)
        x = 20
        y = 85

        draw.text((x, y), self._condition, inky_display.BLACK, condition_font)

        inky_display.set_image(img)
        inky_display.show()