/*
Problem: https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/c

given a boolean convert to its string representation ("true"/"false")
*/

#include <stdbool.h>

//The returned string should be statically allocated and it won't be freed
const char *boolean_to_string(bool b)
{
    return b ? "true" : "false";
}


/*
Completed: 1 minute
time complexity: O(1) -> performing one logical operation
space complexity: O(1) -> within the stack of our function, we have the boolean b and nothing
*/