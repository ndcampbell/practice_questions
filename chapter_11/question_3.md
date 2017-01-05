# Question

## Chess Test

you have a chess game with the following method: `boolean canMoveTo(int x, int y)`. This method is part of the Piece classand returns whether or not a piece can move to position (x,y) How would you test this?

# Solution

Extreme case validation:
1. Test with negative x and y values
2. test with x or y larger than the board
3. test with a full board
4. with with empty board

Ask interviewer if you want to throw an exception or just return false. Validate that the outcome is correct

General testing:
We can not test every possible scenario but we could test against every other type of piece and make sure the return is what is expected
