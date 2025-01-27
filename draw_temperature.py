import sys

from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw

class DisplayTemperature:
    def __init__(self, temp: int):
        self._temp: str = f"{str(temp)}°"
    
    def draw_temp(self) -> None:
        inky_display = auto()
        inky_display.set_border(inky_display.WHITE)

        img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype("FredokaOne-Regular.ttf", 50)
        _, _, w, h = font.getbbox(self._temp)
        x = 20
        y = 20

        draw.text((x, y), self._temp, inky_display.BLACK, font)
        inky_display.set_image(img)
        inky_display.show()