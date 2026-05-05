def stairs_in_20(arr):
    one_year_total = 0
    for x in arr:
        one_year_total += sum(x)
    return one_year_total *20
print(stairs_in_20([
    [10, 20, 30],
    [5, 15],             
    [100],               
    [1, 2, 3, 4],        
    [50, 60],            
    [7, 8, 9],           
    [200, 300, 400]]))