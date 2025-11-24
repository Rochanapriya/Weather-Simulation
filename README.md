Weather Pattern Simulation – Markov Chain Model

This project implements a stochastic weather simulation using a Markov-chain model with configurable state transition probabilities and state holding durations.
The model generates long-term synthetic weather patterns and computes empirical state distributions using probabilistic transitions.

📌 Overview

The simulator models weather as a set of states, such as:

Sunny

Rainy

Cloudy

Stormy

Each state has:

A transition probability distribution into other states

A number of days it “holds” before transitioning

The system evolves over time using a stochastic process driven by NumPy’s random sampling.

🧠 Core Features

✔ Markov-chain transition logic
✔ Configurable weather states
✔ Support for holding durations
✔ Infinite generator mode
✔ Long-term simulation
✔ Empirical state distribution output
✔ Fully object-oriented

🧮 Methodology

Model type:
Discrete-time Markov-Chain with deterministic state durations

Transitions:
Randomized, probabilistic, constrained to sums = 1

Holding duration:
Individually configurable per state

Simulation output:
Percentages of time spent in each state over a defined period
