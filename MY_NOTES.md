# My initial ideas
    - Create a random array of random numbers using random library
    - Implement a bubble sort
    - To print a bar inside the terminal, we could do '##'*n+1, with n being the number. the +1 makes it so that 0 is allowed.
    - Re-implement the bubble sort so that it returns the position and array every step. We can achieve that using yield, exporting current index and array. This will be done twice.
    - Because yield runs twice, we can check for differences between two array at the location of the index. If the index are swapped, we color it differently. We also want to color the index differently too.

# Possible bugs
    - The random generated number array can contain negative number. Since the length of the bar is positive, we have to change the limit so it is not negative.
    - Also make sure the limit isnt too big (ie, upper limit is 1000). This is to make sure The bar isnt too long, and does not take too long to print