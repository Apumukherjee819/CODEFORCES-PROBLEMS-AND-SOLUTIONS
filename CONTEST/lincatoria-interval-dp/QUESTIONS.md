## A : BALLS

You are given an array of $N$
 balls. Each ball has some color $c_i$
. Balls are numbered from 1
 to $N$
.

In one operation, you can pick any ball and delete it. Balls on either side will come together, becoming neighbours. If these two balls have the same color, they will break! This process will continue as long as two neighbouring balls have the same color.

Your taks is to find the minimal number of operations to delete the entire array. Note, that only manual deletions count.


### INPUT :

First line contains a single integer $N (3≤N≤200)$
 - number of balls.

Second line contains $N$
 integers separated with spaces $c_i (1≤ci≤N)$
 - colors of balls. It is guaranteed that no two consecutive balls have the same color.

### OUTPUT:

Output should contain a single number - minimal number of operations to delete the entire array.


## B : PEBBLE AUTOMATION 

A Pebble Automaton is a grid of cells. Each cell can contain some number of stones. In every iteration, each cell can move some number of stones up, right, down and left. Each cell only knows two things, based on which it will make its decision:

Its position in the grid
The number of stones in the cell
It knows nothing about other cells, previous or current iteration. It just moves the stones based on how many stones it has.



Your task is to define these functions for every cell, such that in the end you calculate something!

For each task, the grid is initially empty. Then, A
 stones are placed in the top left corner and B
 stones are placed in the top right corner. After that, the iterations start. Each iteration, every cell moves its stones simultaneously. If during some iteration no stones were moved, the Pebble Automaton stops and the final grid state is considered the output.

You need to solve 5
 separate tasks:

(10
 points) A+B
 stones in the bottom right corner
(20
 points) |A−B|
 stones in the bottom right corner
(15
 points) min(A,B)
 stones in the bottom right corner
(15
 points) max(A,B)
 stones in the bottom right corner
(40
 points) 1
 stone in the bottom left corner if A>B
 and 1
 stone in the bottom right corner if B>A
. If A=B
, then both corners must contain 0
 stones.
For each task, remaining cells in the grid can have any number of stones. You will get 50%
 of points for a task if you only solve it for odd grid size N
.

Constraints:

1≤A,B≤100
,
Total number of iterations before stopping is at most 103
Cells can never move stones outside of the grid
Input
First line contains two numbers – S(1≤S≤5)
 and N(5≤N≤10)
. S
 is the number of the task, N
 is the size of the grid. The grid is always square.

Interaction
The grader will ask you some number of queries. Each query is 3
 numbers – x
, y
 (1≤x,y≤N
) and count
 (0≤count≤200
). Each query asks about the cell in row x
 and column y
 with count
 stones.

The output for each query is 4
 numbers separated by spaces – u
, r
, d
 and l
. This is the number of stones moved up, right, down and left respectively. The remaining stones will stay in this cell. Each query must be answered on a separate line with flushed output.

To read queries, use while(cin >> x >> y >> count) in C++ or for line in sys.stdin in Python.

**Note**
The queries will be called in any order so you don't have any information about the other cells or the previous iteration.


