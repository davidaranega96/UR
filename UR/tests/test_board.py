import pytest
from board import Square, Board, PrivateSquare


@pytest.mark.parametrize(
    'safe_squares, expected_result',
    [
        ([1, 3], [Square(2, False), Square(3, True)]),
        ([1, 4], [Square(2, False), Square(3, False)]),
        ([], [Square(2, False), Square(3, False)])
    ],
    ids=['One safe square in the shared ones', 'No safe square in the shared ones', 'No safe squares']
)
def test_create_shared_squares(safe_squares, expected_result):
    board_configuration = {'shared_squares': [2, 3], 'private_squares': [1, 4], 'safe_squares': safe_squares}

    assert Board(1, 2).create_shared_squares(board_configuration) == expected_result


@pytest.mark.parametrize(
    'square_numbers, are_safe, expected_result',
    [
        ([1, 1], [True, True], True),
        ([2, 2], [False, False], True),
        ([1, 2], [True, True], False),
        ([1, 1], [True, False], False),
        ([1, 2], [False, True], False)
    ],
    ids=[
        'The squares are equal, both safe',
        'The squares are equal, none safe',
        'The squares numbers are different',
        'The is_safe option is different',
        'The squares numbers and the is_safe option are different'
    ]
)
def test_squares_are_equal(square_numbers, are_safe, expected_result):
    square_1 = Square(square_numbers[0], are_safe[0])
    square_2 = Square(square_numbers[1], are_safe[1])

    assert (square_1 == square_2) is expected_result


@pytest.mark.parametrize(
    'square_numbers, are_safe, players, expected_result',
    [
        ([1, 1], [True, True], [1, 1], True),
        ([1, 2], [True, True], [1, 1], False),
        ([1, 1], [True, False], [1, 1], False),
        ([1, 2], [False, True], [1, 1], False),
        ([1, 1], [False, False], [1, 2], False),
    ],
    ids=[
        'The squares are equal',
        'The squares numbers are different',
        'The is_safe option is different',
        'The squares numbers and the is_safe option are different',
        'The players are different'
    ]
)
def test_private_squares_are_equal(square_numbers, are_safe, players, expected_result):
    square_1 = PrivateSquare(square_numbers[0], players[0], are_safe[0])
    square_2 = PrivateSquare(square_numbers[1], players[1], are_safe[1])

    assert (square_1 == square_2) is expected_result
