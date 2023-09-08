# DESCRIPTION

# Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

# For example:

# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ) = True
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ) = False

def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list):
        if len(original) != len(other):
            return False

        for i in range(len(original)):
            if not same_structure_as(original[i], other[i]):
                return False
        return True
    elif not isinstance(original, list) and not isinstance(other, list):
        return True
    else:
        return False