

class bowling:

    def __init__(self):
        self.frames = []
        self.current_frame = []
        self.frame_count = 0

    def roll(self, pins):
        # this means the current frame is an open frame
        if len(self.current_frame) == 2:
            self.frames.append(self.current_frame)
            self.current_frame = []        
        
        if pins == 10 and len(self.current_frame) == 0:
            self.current_frame = ['X']
            self.frames.append(self.current_frame)
            self.current_frame = []
        elif pins == 10 and len(self.current_frame) == 1:
            self.current_frame = [0, '/']
            self.frames.append(self.current_frame)
            self.current_frame = []

        if len(self.current_frame) == 1 and self.current_frame[0] + pins > 10:
            raise ValueError("There can only be ten pins in a single frame.....")
        elif len(self.current_frame) == 1 and self.current_frame[0] + pins == 10:
            self.current_frame = [self.current_frame[0], '/']
            self.frames.append(self.current_frame)
            self.current_frame = []

        self.current_frame.append(pins)

    def score(self):
        pass

    def play(self):
        pass


if __name__ == "__main__":
    print("Bowl!")

    bowling_game = bowling()

    bowling_game.roll(6)
    bowling_game.roll(4)
    bowling_game.roll(3)
    print(bowling_game.frames, bowling_game.current_frame)