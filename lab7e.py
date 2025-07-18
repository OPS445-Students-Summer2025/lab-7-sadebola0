#!/usr/bin/env python3
# Student ID: sadebola

class Time:
    """Simple object type for time of the day."""

    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.min = m
        self.sec = s

    def __str__(self):
        '''return a string representation for the object self'''
        return "{:02d}:{:02d}:{:02d}".format(self.hour, self.min, self.sec)


    def print_time(self):
        '''print the time represented by self'''
        print(self.__str__())


    def __repr__(self):
        '''return a string representation using . instead of :'''
        return f'{self.hour:02d}.{self.min:02d}.{self.sec:02d}'

    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def change_time(self, seconds):
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second
        return None

    def sum_times(self, t2):
        total_sec = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_sec)

    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

