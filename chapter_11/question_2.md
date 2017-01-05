# Question

## Random Crashes

You have an application which crashes when it runs. You find it never crashes in the same spot. It is single threaded and uses standard libraries. WHat errors could be causing this crash?

# Solution

Possible errors:

1. System/OS is killing the application for some reason. You can test this by running strace with the application to see why it dies
2. Memory leak causing program to run out of memory
3. The application has a random variable that is not fixed for all runs (like user input or random number)
4. External dependencies

Questions like these are important to show a logical, structured manner not just throwing things at the wall and seeing what sticks



