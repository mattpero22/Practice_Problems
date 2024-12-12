/* 
Problem: https://www.codewars.com/kata/53dc54212259ed3d4f00071c

Sum two arrays, straightforward

plan of attack:
    1. define a placeholder for our sum
    2. iterate through each number
    3. add each number to our sum
    4. return sum

*/


#include <stddef.h>
#include <stdio.h>

int sum_array(const int *values, size_t count)
{
  float sum = 0.0;
  for(size_t i=0; i<count; i++)
  {
    sum = sum + values[i];
  }

  return sum;
}