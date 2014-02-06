Spellcheck Challenge
===

*Solution by Andrew Wessels Feb. 2, 2014*

The problem
---
The program recieves input words through stdin and attempts to correct spelling mistakes based on a provided dictionary.

It detects three types of errors:

- Case (upper/lower) errors: "inSIDE" => "inside"
- Repeated letters: "jjoobbb" => "job"
- Incorrect vowels: "weke" => "wake"

If a corrected string cannot be determined, the program should output "NO SOLUTION".

The program must be faster than O(n), meaning you can't scan the dictionary every time you want to spellcheck a word.

My Solution
---
I quickly realized that I would need to build some kind of tree structure. I designed it something like a state machine, where each state transition represents a letter in the word. Each node/state knows about several possible paths it could take, based on the input. The program uses a simple depth-first approach to finding a viable solution.

The problem asks me to determine the time complexity of my solution. I believe my solution is O(log(n)) as is the case with binary search, which this is pretty similar to.

Running the program
---
The problem asks that my solution be able to run in the command line, and continually prompt the user for more input until killed. You can achieve this functionality by running `run.py`.

I also added a pretty print version of the above. It's called `pretty.py` and it  basically does the same thing, but it includes more output and prompting.

The problem also asks that I test my solution against a set of words that have been randomly altered based on the acceptable defects described above. The test program should determine that each of these test cases return the corrected string rather than "NO SOLUTION". You can run the test by running `test.py`. Note: The problem doesn't mention testing false-positive cases, so I left that out, though I think it would be a good idea to include if you want to thoroughly test the code.

The bulk of the code is contained within spellcheck.py, and so the class can be used in other scripts.

Configuration
---
I added a configuration file (`config.py`) which allows you to specify the input file used as the dictionary. This file will be used when generating the tests and when you otherwise run the program.