## 2253A : THE BEST CARD

In a card game, there are n
 cards with values 2,3,4,…,n+1
.

To determine which of two cards with values x
 and y
 wins, apply the following rules:

if one of the numbers x
 and y
 is divisible by the other, the card with the smaller value wins;
otherwise, the card with the larger value wins.
For example, between cards 2
 and 6
, card 2
 wins because 6
 is divisible by 2
. Between cards 4
 and 6
, card 6
 wins because neither of these numbers is divisible by the other.

Determine whether there exists a card that wins against every other card.

### Input
The first line contains an integer $t$
 $(1≤t≤10^4
)$ — the number of test cases.

The only line of each test case contains an integer $n$
 $(2≤n≤2⋅10^5
)$ — the number of cards in the game.

Additional constraints on the input:

the sum of n
 over all test cases does not exceed $3⋅10^6$
.
### Output
For each test case, print YES if there is a card that wins against all other cards, and NO otherwise.

Each letter may be printed in either case. For example, YES, yes, and yEs are all recognized as a positive answer.
