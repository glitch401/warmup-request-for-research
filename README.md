# Warmups - [Request for Research 2.0](https://openai.com/blog/requests-for-research-2/)

[![N|Solid](https://avatars0.githubusercontent.com/u/14957082?s=200&v=4)](https://openai.com/)


---
## Warmup 1:
Train an LSTM to solve the XOR problem: that is, given a sequence of bits, determine its parity. The LSTM should consume the sequence, one bit at a time, and then output the correct answer at the sequence’s end. Test the two approaches below:
  - Generate a dataset of random 100,000 binary strings of length 50. Train the LSTM; what performance do you get?
  - Generate a dataset of random 100,000 binary strings, where the length of each string is independently and randomly chosen between 1 and 50. Train the LSTM. Does it succeed? What explains the difference?

## Solution:

The solution to the above mentioned problem in warmup requires `numpy` & `keras` installed to run.

Install the dependencies to start testing, with the following:

```sh
$ pyton warmup1.py
```
---
## Warmup 2:
 Implement a clone of the classic Snake game as a Gym environment, and solve it with a reinforcement learning algorithm of your choice. Tweet us videos of the agent playing. Were you able to train a policy that wins the game?

## Solution:

The solution to the above mentioned problem in warmup requires `gym` & `keras` installed to run.

Install the dependencies to start testing, with the following:

```sh
$ pyton warmup2.py
```
---
### Todos

 - Warmup2 is not ready yet

License
----

GNU