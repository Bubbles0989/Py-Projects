

class bowling:

    def __init__(self):
        self.frames = []
        self.current_frame = []
        self.frame_count = 1

    def roll(self, pins):
        if pins == 10 and len(self.current_frame) == 1:
            self.current_frame = [0, '/']
            self.frames.append(self.current_frame)
            self.frame_count += 1
            self.current_frame = []
        elif pins == 10:
            self.current_frame = ['X']
            self.frames.append(self.current_frame)
            self.frame_count += 1
            self.current_frame = []
        elif len(self.current_frame) == 2 and self.frame_count != 9:
            self.frames.append(self.current_frame)
            self.frame_count += 1
            self.current_frame = []
            self.current_frame.append(pins)
        elif len(self.current_frame) == 2 and self.frame_count == 9:
            self.current_frame.append(pins)
            self.frames.append(self.current_frame)
            self.frame_count += 1
        elif len(self.current_frame) == 1 and self.current_frame[0] + pins > 10:
            raise ValueError("There can only be ten pins in a single frame.....")
        elif len(self.current_frame) == 1 and self.current_frame[0] + pins == 10:
            self.current_frame = [self.current_frame[0], '/']
            self.frames.append(self.current_frame)
            self.frame_count += 1
            self.current_frame = []
        else:
            self.current_frame.append(pins)

    def score(self):
        pass

    def play(self):
        pass


if __name__ == "__main__":
    print("Bowl!")
