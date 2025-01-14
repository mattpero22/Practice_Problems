'''
PROBLEM: https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

Initial Thoughts:
    We need to iterate through all items in our given intervals and check for overlap for each, storing a master interval list
        can be made a bit easier if we knew that our intervals were in ascending order => sort it
    We can then go through the sorted array and check if the start of the current interval is overlapping with the end of the last interval
    If there is an overlap we need to see if the end needs to be updated to a larger point.
    If not, we can add on the current index safely with no overlap
    Then when we get through all intervals, we need to sum their ranges and give back the value

'''
def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    
    combined = []
    for s,e in intervals:
        if len(combined) == 0: combined.append([s,e])
        if combined[-1][1] < s:
            combined.append([s,e])
        else:
            new_e = max([e, combined[-1][1]])
            combined[-1] = [combined[-1][0], new_e]
        
    sum = 0
    for val in combined:
        sum += val[1] - val[0]

    return sum


'''
COMPLETED: 45 min

Time complexity:
    sorting in python -> O(nlogn) where n is length of intervals
    iterate through the list of intervals performing constant time operations -> O(n)
    iterate through the combined list (worst case combined length = n) -> O(n)

    Total -> nlogn + 2n; Reduced O(nlogn)

Space Complexity:
    let sizeof(int) = 1
    let sizeof(arr[1,1]) = 2

    intervals => implicit storage, sort probably uses some heap memory with a temp variable during sort
    worst case for combined is when combined = intervals -> 2n
    sum takes up sizeof(int) -> 1

    Total -> 2n + 1; Reduced O(n)

'''