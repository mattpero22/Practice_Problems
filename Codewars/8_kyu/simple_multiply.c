/*
Problem: https://www.codewars.com/kata/583710ccaa6717322c000105/train/c

Super straightforward. Return even numbers multiplied by 8, return odds by 9

1. take the modulus 2 of the input
2. determine if it is even or odd based on result.
3. if modulus is 0 its even, otherwise odd
4. return and multiply in one line
*/

int simple_multiplication(int number) {
    if (number % 2 == 0) {
      return number * 8;
    } else {
      return number * 9;
    }
}

/*
Completed: 2 minutes

Time complexity = O(1)
space complexity = O(1) -> only need to store number


*/