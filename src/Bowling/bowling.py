

class bowling:

    def __init__(self):
        self.frames = []
        self.current_frame = []
        self.frame_count = 0
        self.total_score = 0

    def roll(self, pins):
        if len(self.current_frame) == 2 and self.frame_count != 9:
            self.frames.append(self.current_frame)
            self.frame_count += 1
            self.current_frame = []    
        elif len(self.current_frame) == 2 and self.frame_count == 9:
            if pins == 10:
                self.current_frame.append('X')
                self.frames.append(self.current_frame)
                self.frame_count += 1
                return    
            elif self.current_frame[1] != 'X' and self.current_frame[1] + pins == 10:
                self.current_frame.append('/')
                self.frames.append(self.current_frame)
                self.frame_count += 1
                return
            else:
                self.current_frame.append(pins)
                self.frames.append(self.current_frame)
                self.frame_count += 1
                return

        if pins == 10 and len(self.current_frame) == 1 and self.frame_count != 9:
            self.current_frame = [0, '/']
            self.frames.append(self.current_frame)
            self.frame_count += 1
            self.current_frame = []
        elif pins == 10 and self.frame_count != 9:
            self.current_frame = ['X']
            self.frames.append(self.current_frame)
            self.frame_count += 1
            self.current_frame = []
        elif pins == 10 and self.frame_count == 9:
            self.current_frame.append('X')
        elif len(self.current_frame) == 1 and self.frame_count != 9 and self.current_frame[0] + pins > 10:
            raise ValueError("There can only be ten pins in a single frame.....")
        elif len(self.current_frame) == 1 and self.frame_count != 9 and self.current_frame[0] + pins == 10:
            self.current_frame = [self.current_frame[0], '/']
            self.frames.append(self.current_frame)
            self.frame_count += 1
            self.current_frame = []
        elif len(self.current_frame) == 1  and self.frame_count == 9 and self.current_frame[0] != 'X' and self.current_frame[0] + pins == 10:
            self.current_frame.append('/')
        else:
            self.current_frame.append(pins)
 
    def score(self):
        total_score = 0
        count = 0
        for frame in self.frames:
            if count == 9:
                if frame[0] == 'X' and frame[2] == '/':
                    total_score += 20
                elif frame[0] == 'X' and frame[1] == 'X' and frame[2] == 'X':
                    total_score += 30
                elif frame[0] == 'X' and frame[1] == 'X':
                    total_score += (20 + frame[2])
                elif frame[0] == 'X':
                    total_score += (10 + frame[1] + frame[2])
                elif frame[1] == '/' and frame[2] == 'X':
                    total_score += 20
                elif frame[1] == '/':
                    total_score += (10 + frame[2]) 
                elif frame[2] == '/':
                    total_score += (10 + frame[0])
                else:
                    total_score += (frame[0] + frame[1] + frame[2])
            else:
                if frame[0] == 'X' and self.frames[count + 1][0] == 'X' and self.frames[count + 2][0] == 'X':
                    total_score += 30
                elif frame[0] == 'X' and self.frames[count + 1][0] == 'X' and self.frames[count + 2][1] == '/':
                    total_score += 20
                elif frame[0] == 'X':
                    total_score += (10 + self.frames[count + 1][0] + self.frames[count + 1][1])
                elif frame[1] == '/' and self.frames[count + 1][0] == 'X':
                    total_score += 20
                elif frame[1] == '/':
                    total_score += (10 + self.frames[count + 1][0]) 

                else:
                    total_score += (frame[0] + frame[1])
            
            count += 1
        self.total_score = total_score
        print("This games total score was", total_score)



if __name__ == "__main__":
    # Example game:
    test_game = bowling()
    test_game.roll(5)
    test_game.roll(5)

    test_game.roll(2)
    test_game.roll(4)

    test_game.roll(0)
    test_game.roll(10)

    test_game.roll(4)
    test_game.roll(6)

    test_game.roll(7)
    test_game.roll(3)

    test_game.roll(7)
    test_game.roll(1)

    test_game.roll(5)
    test_game.roll(3)
    
    test_game.roll(5)
    test_game.roll(2)

    test_game.roll(4)
    test_game.roll(4)
    
    test_game.roll(5)
    test_game.roll(5)
    test_game.roll(10)

    count = 1
    for frame in test_game.frames:
        print("Frame", str(count) + ":", frame)
        count += 1

    test_game.score()

