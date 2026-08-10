## 2256B : DOMINO TILES

Nygglatho returns from the market with an old box of tiles whose painted marks have begun to fade. Before she can put it away, Chtholly and the young fairies have already spread the tiles across the dining table and turned them into a puzzle.

There is a row of n
 tiles. Each tile should be marked with either 0
 or 1
. However, some of the marks have faded away.

The current row is represented by a string s
 of length n
. Each character of s
 is 0
, 1
, or ?
. Chtholly must replace every ?
 with either 0
 or 1
.

After replacement, for every 1≤i<n
, the two neighboring tiles $s_i$
 and $s_{i+1}$
 form a domino of weight $(s_i+s_{i+1})$
. Note that two consecutive dominoes share exactly one tile. The completed row is valid if every two consecutive dominoes have different weights.

Determine the number of different∗
 ways to replace all ?
 characters so that the completed row is valid. Output the answer modulo 998244353
.

∗
Two ways of replacement are considered different if the resulting strings are different.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 $(1≤t≤10^4
)$. The description of the test cases follows.

The first line of each test case contains one integer n
 $(2≤n≤2⋅10^5
)$ — the number of tiles.

The second line contains the string s
 of length n
, where $s_i=0$
, 1
, or ?
.

It is guaranteed that the sum of n
 over all test cases does not exceed $2⋅10^5$
.

### Output
For each test case, output one integer — the number of valid ways to replace all ?
 characters, modulo 998244353
.
