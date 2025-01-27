# Python program to display weather data on a Rasberry Pi with
# Inky wHAT display
# ! Currently in pre-alpha stage
from current_weather import CurrentWeather
from draw_temperature import DisplayWeather


def main() -> None:
    test: CurrentWeather = CurrentWeather('01854')
    test.refresh()
    temp = test.get_current_temp()
    print(f"The current temperature in Lowell is {temp}")
    print(f"The current condition is {test.get_current_condition()}")
    disp_temp: DisplayWeather = DisplayWeather(test)
    disp_temp.RefreshDisplay()


if __name__ == "__main__":
    main()