import main


# First approach
def test_same_structure_as():
    cases = (
            ([[1,[1,1]], [2,[2,2]]], True),
            ([[1,[1,1]], [[2,2],2]], False)
      )

    for x, y in cases:
        # First approach
        assert main.same_structure_as(x[0], x[1]) == y
