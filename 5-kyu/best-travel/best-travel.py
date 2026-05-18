from itertools import combinations
​
def choose_best_sum(t, k, ls):
   
    result = [list(c) for c in combinations(ls, k)] 
    return max((sum(x) for x in result if sum(x) <= t), default = None)
    
print(choose_best_sum(214, 1, [313, 388, 387, 177, 478, 128, 228, 42, 346, 100]))