import asyncio

class state_machine():
    def __init__(self):
        self.state = 0
        print("State machine created")

    def update(self):
        self.state = self.state + 1


state_machine = state_machine()

for i in range(10):
    state_machine.update()
    print(state_machine.state)
