
class API:
    def __init__(self, name):
        self.name = name


nasa = API('Nasa API')
cdo = API('Climate Data Online (NOAA)')

wwo = API('World Weather Online')
wwo.local_weather = 'weather'
wwo.historical_local = 'past-weather'
wwo.marine = 'marine'
wwo.historical_marine = 'past-marine'
wwo.ski = 'ski'
wwo.time_zone = 'tz'
wwo.search = 'search'


