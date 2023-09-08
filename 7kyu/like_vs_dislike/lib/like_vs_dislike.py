# DESCRIPTION
# Create a function that takes in a list of button inputs and returns the final state.

# Examples
# like_or_dislike([Dislike]) ➞ Dislike
# like_or_dislike([Like, Like]) ➞ Nothing
# like_or_dislike([Dislike, Like]) ➞ Like
# like_or_dislike([Like, Dislike, Dislike]) ➞ Nothing

def like_or_dislike(lst):
    click = "Nothing"
    
    for i in lst:
        if click == i:
            click = "Nothing"
        else:
            click = i
        
    return click 