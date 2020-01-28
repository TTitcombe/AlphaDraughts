[![Build Status](https://travis-ci.com/TTitcombe/AlphaDraughts.svg?branch=master)](https://travis-ci.com/TTitcombe/AlphaDraughts)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# AlphaDraughts

AlphaDraughts is a PyTorch implementation of [AlphaGo Zero][alphago_zero] applied to the game of Draughts. \
Draughts, or Checkers, is a far easier game to solve compared to Go, and even to Chess: it has an 8x8 playing board, 
but only two types of pieces. Additionally, Draughts has been [weakly solved][solved_games]. This means that Draughts
should present less of a burden to train than AlphaGo (although just how much less is to be determined).

The board game has been implemented. The AI is to follow.

### Requirements
Alphadraughts has been developed with python 3.7, however other 3.x versions should work.

Currently, alphadraughts can be installed via local pip installation. Clone the repo, navigate to it, and run:

```bash
pip install -e .
```

### How to run
Run `python -m scripts.play_game` to play a human-vs-human game. This script accepts user input
of the form "start-end", where *start* and *end* are board square numbers.

To play a "bot" which randomly selects a move, run `python -m scripts.play_bot`.\
We are currently implementing more challenging bots.

### Project Structure
```
|-- .github - Contains github actions
|-- alphadraughts
|   |-- algorithms - Algorithms for training and running the AI
|   |-- draughts - Code to implement the game
|   |-- models - PyTorch nets used in algorithms
|   |-- utils - shared code, or code which doesn't fit anywhere in particular
|-- docs - Rules of the game, notes on how to train or use the AI etc.
|-- models - Trained models capable of playing draughts
|-- results - Videos, graphs, data etc. of AI training and testing
|-- scripts - Handy scripts for playing games and training the AI
|-- tests - CI tests
|-- travis - Files used by Travis to run the tests
```

### Contributing
Contributions to this project are more than welcome. Please see the [contributing guide][contributing].

[alphago_zero]: https://www.nature.com/articles/nature24270.epdf?author_access_token=VJXbVjaSHxFoctQQ4p2k4tRgN0jAjWel9jnR3ZoTv0PVW4gB86EEpGqTRDtpIz-2rmo8-KG06gqVobU5NSCFeHILHcVFUeMsbvwS-lxjqQGg98faovwjxeTUgZAUMnRQ
[solved_games]: https://en.wikipedia.org/wiki/Solved_game#Solved_games

[contributing]: CONTRIBUTING.md