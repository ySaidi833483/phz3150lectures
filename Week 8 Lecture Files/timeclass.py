"""a module of time-related functions"""

# This file is the code example from chapter 16 of:

# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
# Copyright 2015 Allen Downey
# License: http://creativecommons.org/licenses/by/4.0/


# This function is the only one not operating on a Time.  It cannot be
# in the class Time, because its "self" argument would be undefined
# when called.  So, it appears out here, in the module, but not in the
# class.

def int_to_time(seconds):
    time = Time()
    minutes,   time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

class Time:
    """Represents the time of day."""
    
    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True
    
    def print_time(self):
        print('%02d:%02d:%02d' % (self.hour, self.minute, self.second))
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes   * 60 + self.second
        return seconds
        
    def increment(self, seconds):
        if not self.valid_time():
            raise ValueError("Invalid Time object in add_time()")
        seconds = self.time_to_int() + seconds
        return int_to_time(seconds)
    
    # These require two Time arguments.  By convention, these are
    # called "self" and "other":
    
    def add_time(self, other):
        if not self.valid_time() or not other.valid_time():
            raise ValueError("Invalid Time object in add_time()")
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other):
        if not self.valid_time() or not other.valid_time():
            raise ValueError("Invalid Time object in add_time()")
        return self.time_to_int() > other.time_to_int()
    
    # There are some special methods, which have pairs of underscores:
    
    # The __init__ method is called when you create an object.
    # (Remember that you can call keyword arguments without using
    # their names, if the order is preserved.)
    def __init__(self, hour=0, minute=0, second=0):
        self.hour   = hour
        self.minute = minute
        self.second = second
    
    # The __str__ method is called by print() to print the object.
    def __str__(self):
        return '%02d:%02d:%02d' % (self.hour, self.minute, self.second)
    
    #__add__ says what to do when we are operated on by +
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    
    # ...and __radd__ says what to do if the time object only appears
    # on the right (the time object is still identified by "self".
    
    def __radd__(self, other):
        return self.__add__(other)


# It's good practice to start writing new classes by writing the
# __init__ and __str__ methods.
