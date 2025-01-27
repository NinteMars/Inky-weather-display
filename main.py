# Python program to display weather data on a Rasberry Pi with
# Inky wHAT display
# ! Currently in pre-alpha stage
from current_weather import CurrentWeather
from draw_temperature import DisplayTemperature


def main() -> None:
    test: CurrentWeather = CurrentWeather('01854')
    temp = test.get_current_temp()
    print(f"The current temperature in Lowell is {temp}")
    disp_temp: DisplayTemperature = DisplayTemperature(temp)
    disp_temp.draw_temp()


if __name__ == "__main__":
    main()