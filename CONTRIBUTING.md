# Contributing

Thank you for contributing to this project!

Feel tree to raise tickets on any issues you find with the project. \
If you would like to contribute code, see the open issues for something to work on, or open up a PR.

### Continuous Integration
This project uses [Travis][travis] for continuous integration. Travis will run tests on all opened PRs.

The tests run as follows:
* Code quality
    - Test that code is [blackened][black]
* Unit tests
    - Test board and game logic

Tests are currently only run using Python 3.7 on an Ubuntu Bionic Beaver machine.

### Testing
This project uses [PyTest][pytest] as a unit testing framework.  
To run all unit tests, run `python -m pytest` when in the top level (repository) directory.

Please add unit tests for any code affecting the [`draughts`][draughts] package. Don't unit test machine learning code.

### Code quality
[Black][black] is used to automatically format code. Either run `black .` in the top level directory, or use [pre-commit][precommit].

To set up pre-commit, run `pre-commit install` on the command line. Now code will automatically be 
formatted every time a commit is made.


[black]: https://github.com/psf/black
[precommit]: https://pre-commit.com
[pytest]: https://pytest.org/en/latest/
[travis]: https://travis-ci.com/

[draughts]: alphadraughts/draughts
