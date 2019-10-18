import sys
sys.path.insert(1, '.')
import api.utils as utils
import api.apis as apis
from analysis import weather

u = weather.do_something()
print(u)
