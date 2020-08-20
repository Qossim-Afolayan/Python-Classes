class Emotion():
    def __init__(self, positivity, negativity):
        self.positivity = positivity
        self.negativity = negativity

    def __bool__(self):
        return self.positivity > self.negativity

my_emotional_state = Emotion(positivity = 60, negativity = 80)

if my_emotional_state:
    print("This will not print!")

my_emotional_state.positivity = 100
if my_emotional_state:
    print("This will print!")


