### Formal Languages and Automata theory :computer_mouse:
# Lambda NFA to DFA visualizer

**Assignment**: Write an algorithm that has as input a non-deterministic finite automaton with some λ-transitions. Display the finite deterministic automaton resulting from the application of the conversion algorithm on the automaton given as input. 

The symbol for lambda is #, therefore it cannot be used as a transition symbol with another meaning.

When running the code, a folder with images capturing the step-by-step transitions will be created, and in the folder where main.py is found, a video called 'videoclip.avi' will be saved, which represents a slideshow with all the generated images.

## How to run 
In order to run this program, you will have to install 2 packages:

``` python
pip install opencv-python
pip install graphviz
```

## How to write the input
We read from file date.in:

n (number of states), m (number of transition)

m transition (start node, destination node, transition)

source node

number of final nodes, final nodes

number of strings

the strings.

> _Example_

_Input_
``` python
11 12
0 1 #
1 2 #
2 3 a
3 6 #
6 7 #
7 8 a
8 9 b
9 10 b
1 4 #
4 5 b
5 6 #
0 7 #
0
1 10
```
_Output_

The result can be seen in videoclip.avi.
