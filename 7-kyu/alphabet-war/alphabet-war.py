def alphabet_war(s):
​
    left = {'s': 1, 'b': 2, 'p': 3, 'w': 4}
    right = {'z': 1, 'd': 2, 'q': 3, 'm': 4}
    score_left = 0
    score_right = 0
    
    for x in s.lower():
        if x in left:
            score_left += left.get(x)
    for x in s.lower():
        if x in right:
            score_right += right.get(x)
             
    return 'Left side wins!' if score_left > score_right else 'Right side wins!' if score_left < score_right else "Let's fight again!"
​
print(alphabet_war("wwwwzzzzzzzz"))
​