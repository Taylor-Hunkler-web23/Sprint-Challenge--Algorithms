#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)This run time is O(n) Linear. As n increases the run time will also increase.


b)This runtime is O(n log n). There is a loop running O(n) and a inner loop.


c)This run time is O(n) Linear. It runs (n) times. It is recursive.

## Exercise II


Use binary search. O(log n)

First find the middle floor of the building.

Go to the middle floor and drop the egg to see if it breaks.

If the egg breaks, then find the floor that is half way between the current floor and the bottom and drop the egg from there.


If the egg does not break when dropped from the middle floor, find the floor halfway between the current floor and the top floor and drop from there.

Continue dropping the egg and moving to the middle floor, either above or below depending on if egg breaks, until you find which floor the egg will break when dropped from.
