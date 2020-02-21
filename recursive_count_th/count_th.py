'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, occur=0):
#if there are less than 2, there can not be "th"
    if len(word) < 2:
        return occur
#check if the first 2 indexes have "th"
    if word[0:2] == "th":
        
    # if they do add 1 to occur
        occur = occur + 1

# return, checking if the next 2 letters have "th"
    return count_th(word[1:], occur)
    
    # TBC
    
    
