"""Test your functions from Week 2 assignment.
"""
import preclass_assignment.functions as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    bed_size = 139  # test input to function
    exp_out = 'Too small!\n'  # expected output
    # when
    fxn.goldilocks(bed_size)  # see goldilocks reaction
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == exp_out # throw error if actual and expected output don't match


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    inp = 30
    exp_out = [1, 1, 2, 3, 5, 8, 13, 21]  # expected output
    # when
    out = fxn.fibonacci_stop(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match

def test_clean_pitch(capsys):
    """Check clean_pitch works as expected."""
    # given
    x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
    status = [1, 0, 0, 0]  # status signal

    exp_out = '[-999, 2, 6, 95]\n'  # expected output
    # when
    fxn.clean_pitch(x, status) #see output of clean_pitch
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == exp_out  # throw error if actual and expected output don't match
