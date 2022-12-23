from plyer import notification
import time


class water:
    def __init__(self):
        inp = int(input("Enter Reminder Time : "))
        time.sleep(inp)
        notification.notify(
            title="Water Reminder",
            message="Please drink water",
            app_name="pog_water",
            timeout=3
        )


while True:
    w = water()
