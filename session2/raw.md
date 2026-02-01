# Feb 1, 2026

## Session by Dr. Uma

---

## Probability

Probability is just a math word for "how likely" something is to happen. It's a way to put a number on a guess!

The Probability Scale
Probability is always a number between 0 and 1.

0 (0%): It is Impossible. (Like picking a green jellybean when there are only red and blue ones).

0.5 (50%): It is Even Stevens. (Like flipping a coin—it's just as likely to be Heads as it is Tails).

1 (100%): It is Certain. (Like the sun rising tomorrow).

### EXPERIMENT

Any procedure that is repeated several number of times is called Experiment

### Trial

if you do 1 time then it's called trial

**Fair coin**

If you flip the coin 100 time, then if you get 50 head and 50 tails, then its a fair coin; But if you get 80 head and 20 tails, then we call it a biased coin

### Types of Experiment:
- **Deterministic Experiment** : Certain about the outcome; outcome are known
- **Random Experiment**: Has random output; outcomes are unknown before starting the experiment

### EVENT
An Event is the specific result you are rooting for. If you want the coin to land on "Heads," your Event is {Heads}.

1. **Sample Space** ($S$)The Sample Space is a list of every possible result that could happen. For a single coin flip, there are only two possibilities: Heads or Tails.Sample Space ($S$): {Heads, Tails}

2. **Cardinality of Sample Space** ($n(S)$)Cardinality is just a fancy math word for "count." It is the total number of items inside your sample space.For one coin, the cardinality is 2.If you flipped two coins, the outcomes would be {HH, HT, TH, TT}, so the cardinality would be 4.

For Event
```
                     n(E)      Count of outcomes in the Event 
Probability P(E) = -------- = --------------------------------------
                     n(S)      Total count in the Sample Space
```

For Experiment
```
                     n(E)      aka. number of favourable outcomes
Probability P(E) = -------- = --------------------------------------
                     n(S)      aka. number of all possible outcomes
```
NOTE:
The letter inside the parentheses is just a "name tag" for the event you are looking at.
  - $A$ is commonly used as the standard label for a single event.
  - $E$ is often used because it stands for the word Event.

P(Heads) = 1 / 2

Using Dices (2 dice):

**Sample space**  ($S$):

```math
S = { (1,1), (1,2), (1,3), (1,4), (1,5), (1,6),
      (2,1), (2,2), (2,3), (2,4), (2,5), (2,6),
      (3,1), (3,2), (3,3), (3,4), (3,5), (3,6),
      (4,1), (4,2), (4,3), (4,4), (4,5), (4,6),
      (5,1), (5,2), (5,3), (5,4), (5,5), (5,6),
      (6,1), (6,2), (6,3), (6,4), (6,5), (6,6) }
```

**Cardinality of sample space** ($n(S)$):
```
n(S) = 6 (sides on die 1) × 6 (sides on die 2) = 36
```


Example Event ($E$) and its Cardinality ($n(E)$)
Let’s say your Event is: "Rolling a sum of 11."

The Event Set: $E = \{ (5,6), (6,5) \}$Cardinality of the Event: $n(E) = 2$

```
          n(E)       2        1
P(11) = -------- = ------ = ------
          n(S)      36       18
```


---

## Independant events ($A \cap B$)
Lets take two events A, B are 2 events, If A & B are said to be independant. If the occurance of A does not affect occurance of B then its called independant event.

E.G: Tossing of two coins, where the outcome of coin A does not affect coin B.

Measure the independant event using:
P($A \cap B$) = P(A) * P(B)


## Mutually Exclusive:
Lets take two events A, B are 2 events, If A & B are said to be mutually exclusive, When one event occurs, the other does not occur.

## Impossible Event
Rolling a dice and getting 7, is impossible, Thus such event is called impossible event, where probability = 0

## Sure Event
Rolling a dice and getting a value between 1 - 6, is a sure event


--- 

# QST 1:

While rolling two dice,
Event A is defined as first trial occurance of a number > 3
Event B is defined as occurance of a number > 3


($A \cap B$) = [
    (4,4), (4,5), (4,6)
    (5,4), (5,5), (5,6)
    (6,4), (6,5), (6,6)
]

P($A \cap B$) = n($A \cap B$) / n(s) = 9/36 = 1/4

P(A) = n(A)/n(s) = 3/6 = 1/2
P(B) = n(B)/n(s) = 3/6 = 1/2

therfore this is an independant event, as 


---

# QST 2:
If A and B are independant with P(A) & P(B), both non zero, the A&B cannot be mutually exclusive

**Experiment:**
Toss a fair coin and roll a fair dice
A - coin shows head
B - dice shows an even number
Check if they are independant

A = {head}
B = { 2, 4, 6}
($A \cap B$) = [
    (h,2), (h,4), (h,6),
  ]

P($A \cap B$) = n($A \cap B$)/n(s) = 3/12 = 1/4

since their proabilit is != 0, they cannot be mutually exclusive


---

# QST 3:

if A and b are mutally exclusive and both have non zero probability, then they cannot be independant

Experiment:
Rolling a dice
A - getting 3
B - getting 6

**ANS:**

Let's look at your dice example:Event A: Rolling a 3. $P(A) = 1/6$Event B: Rolling a 6. $P(B) = 1/6$1. Are they Mutually Exclusive?Yes. A single die cannot be a 3 and a 6 at the same time.MarkdownA ∩ B = { } (The empty set)
n(A ∩ B) = 0
This means the probability of both happening is 0.2. Are they Independent?To be independent, the formula $P(A) \times P(B)$ must equal $P(A \cap B)$.Let's do the math:MarkdownP(A) × P(B) = (1/6) × (1/6) = 1/36
But we already know that $P(A \cap B) = 0$.Because $1/36$ does not equal $0$, these events are not independent.


## Conditional probability

Finding likelyhood of other event, when a event has already occured

P(A|B) = P(A ∩ B) /P(B), where B has already occured

P(B|A) = P(B ∩ A) /P(A), where A has already occured

## Bayes Theorem (! Important)

P(A|B) = P(B|A) * P(A) / P(B)

the left part - posterior probability
P(B|A) - likelihood
P(A) - Prior
P(B) - evidence (should be expressed using total probabilty theorm/law)

---

Probability of Glaucoma given eyes are Red
P(Glaucoma | Red eyes) = P(RE|glaucoma) * P(glaucoma) / P(RE)

Probability of person getting covid given test result is positive 
P(covid | test result is positive) 

## Disjoint events

## Total probability theorem

## Addition theorem

if A and B are two events,  then 

P(A U B) = P(A) + P(B) - P(A ∩ B)

## Multiplication theorem

if A and B are two events,  then 

P(A | B) = P(A ∩ B) / P(B)

or 

P(A ∩ B) = P(A/B) * P(B) or P(B ∩ A) = P(B/A) * P(A) , based on whichever is given

---

PROBLEM 1:
If the letters of the word "AABRAAKAADAABRAA" are arranged at random, find the probability that, all 10 A occur together?
to solve this
- find count of all distinct characters
  - A - 10
  - B - 2
  - R - 2
  - K - 1
  - D - 1
Total = 16

if A is the event where A appears 10 times
then 
P(A) = Number of occurance / total no of occurance = (n*m)!/n! * m! = 10! / (10! * 2! * 2! * 1! * 1!) 


PROBLEM 2:
Find the probability of all the words together in the word "missisippi"


---
PROBLEM 3:

A kitchen set contains 10 knifes, out of which 3 are defective, 2 knifes are drawn at random with replacement. Find the probability that none of the two knifes is defective.


---

# Random variable

should be written in cap letter only