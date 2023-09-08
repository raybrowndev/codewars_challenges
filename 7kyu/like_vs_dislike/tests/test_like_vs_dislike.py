from lib.like_vs_dislike import *


def test1():
    assert like_or_dislike(["Dislike"]) == "Dislike"
def test2():
    assert like_or_dislike(["Like", "Like"]) == "Nothing"
    
def test3():
    assert like_or_dislike(["Dislike", "Dislike"]) == "Nothing"
    
def test4():
    assert like_or_dislike(["Like", "Like", "Like"]) == "Like"
    
def test5():
    assert like_or_dislike(["Like", "Dislike"]) == "Dislike"
    
def test6():
    assert like_or_dislike(["Dislike", "Like"]) == "Like"
    
def test7():
    assert like_or_dislike(["Like", "Dislike", "Dislike"]) == "Nothing"
    
def test8():
    assert like_or_dislike(["Dislike", "Like", "Dislike"]) == "Dislike"
    
def test9():
    assert like_or_dislike(["Like", "Like", "Dislike", "Like", "Like", "Like", "Like", "Dislike"]) == "Dislike"
    
def test10():
    assert like_or_dislike([]) == "Nothing"

