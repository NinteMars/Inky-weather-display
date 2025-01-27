import sys

from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from current_weather import CurrentWeather

class DisplayWeather:
    def __init__(self, cur_weather: CurrentWeather):
        self._temp: str = f"{str(cur_weather.get_current_temp())}°"
        self._condition: str = cur_weather.get_current_condition()

        min_max: list[int, int] = cur_weather.get_min_max_temp()

        self._min: str = f"{str(min_max[0])}°"
        self._max: str = f"{str(min_max[1])}°"
    
    def RefreshDisplay(self) -> None:
        # Initialize the display
        inky_display = auto()
        inky_display.set_border(inky_display.WHITE)
        FONT_NAME: str = "FredokaOne-Regular.ttf"
        BORDER_SIZE: int = 20

        img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        # Add the main temperature to the display

        font = ImageFont.truetype("FredokaOne-Regular.ttf", 60)
        _, _, w, _ = font.getbbox(self._temp)
        x = 20
        y = 20
        TEMPERATURE_LEN = w

        draw.text((x, y), self._temp, inky_display.BLACK, font)

        # Add the current condition

        condition_font = ImageFont.truetype("FredokaOne-Regular.ttf", 25)
        _, _, w, h, = font.getbbox(self._condition)
        x = 20
        y = 85

        draw.text((x, y), self._condition, inky_display.BLACK, condition_font)

        # Add the min and max temperatures for the day

        min_max_font = ImageFont.truetype(FONT_NAME, 24)

        left, top, right, bottom = min_max_font.getbbox(self._min)
        x = BORDER_SIZE + TEMPERATURE_LEN + 5
        y = 40

        draw.text((x, y), self._min, inky_display.BLACK, min_max_font)

        # Because of the degree symbol, the spacing between the slash and the
        # minimum temperature seems larger than it actually is. Shrink the spacing
        # a bit to make it look more even between the min-slash and slash-max
        x = x + right - 5
        y = y + 12
        left, top, right, bottom = min_max_font.getbbox("/")
        draw.text((x, y), '/', inky_display.BLACK, min_max_font)

        x = x + right
        y = y + 12
        draw.text((x, y), self._max, inky_display.BLACK, min_max_font)

        # Load the image corresponding to the current condition
        condition_image = Image.open("images/cloudy.png")

        img.paste(condition_image, (inky_display.WIDTH - condition_image.width - BORDER_SIZE, 20))

        inky_display.set_image(img)
        inky_display.show()