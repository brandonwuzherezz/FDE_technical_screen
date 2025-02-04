# FDE technical screening

This code has a function sort that takes width, height, length, mass of a package and returns a string determining which stack the package must go.

The sort function first must determine if a package is bulky by checking to see if any of its dimensions is greater than or equal to 150 OR if the volume of the package (Width * Height * Length) is greater than or equal to 1000000.

It then determines if the package is heavy by checking to see if the mass of the package is greater than or equal to 20.

The program sets the state of heavy and bulky in a boolean. And at the end of the program it checks the state of heavy and bulky to determine the return value. 

If its neither Heavy or Bulky we return "STANDARD"

If its either Heavy or Bulky we return "SPECIAL"

If its both Heavy and Bulky we return "REJECTED"

At the end of the program I have 6 different test cases to determine whether or not the code works the way it should and testing all edge cases.
