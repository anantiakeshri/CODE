# Striver - 1.1.3 - Switch

from typing import *

def areaSwitchCase(ch: int, a: List[float]):
# Write your code here
    if ch == 1:
        area_cir = 3.14159265359 * a[0] * a[0]
        round_cir = round(area_cir, 5)
        return round_cir

    elif ch == 2:
        area = a[0] * a[1]
        formatted_result = "{:.5f}".format(area)
        return formatted_result

