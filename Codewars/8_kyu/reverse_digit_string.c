/* 
Problem: https://www.codewars.com/kata/53dc54212259ed3d4f00071c

Given a random non-negative number, return the digits of the number within an array in reverse order

Assumptions:
    - only given an integer

plan of attack:
    1. get our integer and check if it is already 0. If it is we can return the trivial solution.
    2. If it is not zero, we need to start getting the digits for the larger number
    3. add the digit to our array in memory
    4. reduce our given integer to get the next digit.
    5. we repeat the process until we have reduced the number down to the last digit

*/
#include <stddef.h>
#include <inttypes.h>

void digitize (uint64_t n, uint8_t digits[], size_t *length_out)
{
  if (n == 0)   // handle the trivial case
  {
    digits[0] = 0;
    *length_out = 1;
  }
  else
  {
    *length_out = 0;    // counter for the number of digits, and to access the next array index
    while (n > 0)
    {
      digits[*length_out] = n % 10; // will return a number 0 to 10, corresponding to the last digit of the number
      n /= 10;                      // reduce by a factor of 10 to get to the next digit place for a decimal based number
      *length_out += 1;             // increment our counter variable via pointer
    }
  }
}

/*
RESULTS: Completed 20 minutes

COMMENTS:
    - was definitely a challenge after not working with C in a while. SO much easier to do in JS or Python.
    - needed to look up the proper method for getting the digits using tyhe modulo operator

*/
