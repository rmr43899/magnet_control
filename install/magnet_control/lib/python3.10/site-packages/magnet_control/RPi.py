class GPIO:
    BCM = 0
    OUT = 0
    LOW = 0
    HIGH = 1

    @staticmethod
    def setmode(mode):
        print("GPIO setmode called with mode:", mode)

    @staticmethod
    def setup(channel, mode):
        print("GPIO setup called for channel:", channel, "with mode:", mode)

    @staticmethod
    def output(channel, state):
        print("GPIO output set for channel:", channel, "to state:", state)

    @staticmethod
    def cleanup():
        print("GPIO cleanup called")
