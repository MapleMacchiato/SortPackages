# SortPackages


This is a quick little project asked by a company.
It follows these rules:
## Rules

### Sort the packages using the following criteria:
* A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
* A package is heavy when its mass is greater or equal to 20 kg.
* STANDARD: standard packages (those that are not bulky or heavy) can be handled normally.
* SPECIAL: packages that are either heavy or bulky can't be handled automatically.
* REJECTED: packages that are both heavy and bulky are rejected.

## To use:
There is a test file called test_sort.py, this tests all the main edge cases I could think of, in addition to normal use cases. To run this project, clone it locally and run python3 main.py, and the tests will run.

To use the function in another file add this to the top of the file:
`from package_sort import sort`
and then proceed to use sort with the following variables:
`sort(width, height, length, mass)`

That's it!
