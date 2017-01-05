# Question

## Mistake

find the mistakes in the following code:

    unsigned int 1;
    for (i = 100; i >= 0; i--)
        printf("%d\n", i);

# Solution

Since `i` is an unsigned int, it will by defination always be >= 0.
You would need `i > 0` in the for condition to properly exit the loop.
also, printf should have `%u` for unsigned int.




