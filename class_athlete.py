class Athlete:
    def __init__(self, value='Jane'):
        self.inner_value = value
        print(self.inner_value)

    def getInnerValue(self):
        return self.inner_value

class Temp(Athlete):
    def __init__(self):
        super()

athlete = Athlete()      # == Athlete.__init__()

print(athlete.getInnerValue())

