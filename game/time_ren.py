"""renpy
init python:
"""

class Time:
    def __init__(self):
        self.t = 0.0
    def init(self, t):
        self.t = t
    def passed(self, dt):
        self.t += dt

time_now = Time()
