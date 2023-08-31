from bowling import bowling
import pytest
import unittest

@pytest.fixture(scope="session", autouse=True)
def test_bowl_with_frames():
    test_game = bowling()
    test_game.roll(5)
    test_game.roll(3)
    test_game.roll(4)
    test_game.roll(5)
    test_game.roll(10)
    return test_game

def test_roll_appends_full_frame_to_frames(test_bowl_with_frames):
    test_game = test_bowl_with_frames
    assert test_game.frames[0] == [5, 3]

def test_roll_appends_pin_number_to_current_frame():
    test_game = bowling()
    test_game.roll(3)
    assert test_game.current_frame == [3]

def test_roll_strike():
    test_game = bowling()
    test_game.roll(10)
    assert test_game.frames[-1] == ['X']

def test_roll_spare_with_0():
    test_game = bowling()
    test_game.roll(0)
    test_game.roll(10)
    assert test_game.frames[-1] == [0, '/']

def test_roll_spare_with_6():
    test_game = bowling()
    test_game.roll(6)
    test_game.roll(4)
    assert test_game.frames[-1] == [6, '/']

def test_roll_incorrect_frame_numbers():
    test_game = bowling()
    test_game.roll(6)
    assert ValueError, test_game.roll(6)

def test_tenth_frame():
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
    test_game.roll(2)

    test_game.roll(3)
    test_game.roll(2)

    test_game.roll(5)
    test_game.roll(3)
    
    test_game.roll(1)
    test_game.roll(2)

    test_game.roll(4)
    test_game.roll(4)
    
    test_game.roll(5)
    test_game.roll(3)
    test_game.roll(1)

    assert test_game.current_frame == [5, 3, 1]


