/* 
Problem: https://www.codewars.com/kata/57eae65a4321032ce000002d/train/c

Given a string of digits, replace any difit below 5 with 0 and any above or including 5 to 1. Return the result as a string.

Assumptions:
    - input will never be an empty string

plan of attack:
    1. get the length of our input string using strlen
    2. iterate through the string char by char
    3. get the current char and store as an int
    4. compare the int to 5 and if it is greater, add a 1 to our binary, otherwise 0

*/

#include <string.h>

void fakeBin(const char *digits, char *binary) {
    for (int i=0; digits[i] != '\0'; i++) {
        if (digits[i] >= '5') {
            binary[i] = '1';
        } else {
            binary[i] = '0';
        }
    }

 	binary[strlen(digits)] = '\0';
}

/*
Results: COMPLETED  14 minutes

Notes:
    - C is trickier than I remember. Had to look up the condition for my for loop (digits[i] != '\0') as it couldnt use strlen like I initially thought
        -- this means that we go until we hit a null character in our input digit string

*/