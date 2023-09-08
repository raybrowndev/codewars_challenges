from lib.nesting_structure_comparison import same_structure_as


def test1():
    assert same_structure_as([1,[1,1]],[2,[2,2]]) == True

def test2():
    assert same_structure_as([1,[1,1]],[[2,2],2]) == False

def test3():
    assert same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] ) == False

def test4():
    assert same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ) == False




