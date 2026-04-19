def check_exam(correct, student):
    if not (correct and student and len(correct) == len(student)):
        return 0
    score= 0
    for x, y in zip(correct, student):
        if x == y:
            score += 4
        elif y == '':
             score += 0
        else:
                score -= 1
    
    return score if score > 0 else 0
print(check_exam(['a', 'b', 'b', 'c'], ['b', '', 'b', '']))