from datetime import datetime, timedelta


class Clock:
    def __init__(self, hour, minute):
        self._time = datetime(2022, 1, 1, 0, 0)
        self.__add__(hour * 60)
        self.__add__(minute)

    def __repr__(self):
        return f"Clock({self._time.hour}, {self._time.minute})"

    def __str__(self):
        return self._time.strftime('%H:%M')

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __add__(self, minutes):
        self._time += timedelta(minutes=minutes)
        return self

    def __sub__(self, minutes):
        self._time -= timedelta(minutes=minutes)
        return self
