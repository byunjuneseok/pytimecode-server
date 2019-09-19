framerate_available_list = [23.976, 24, 25, 29.97, 30]


class Timecode:
    def __init__(self, framerate, df):
        self._framerate = framerate
        self._df = False
        self._current_hours = 0
        self._current_minutes = 0
        self._current_seconds = 0
        self._current_ms = 0         # 1s = 1000 ms
        self._current_frame = 0

    @property
    def framerate(self):
        return self._framerate

    @framerate.setter
    def framerate(self, framerate):
        if framerate in framerate_available_list:
            self._framerate = framerate
        else:
            raise Exception('Framerate error exception.')

    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, df):
        if self._framerate == 29.97:
            self._df = df
        else:
            self._df = False

    def set_current_time(self, hour=0, minute=0, second=0, millisecond=0):
        self._current_hours = hour
        self._current_minutes = minute
        self._current_seconds = second
        self._current_ms = millisecond

    def start(self):
        """ TO-DO"""
