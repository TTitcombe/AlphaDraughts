# Contributing

Thank you for contributing to this project!

Feel tree to raise tickets on any issues you find with the project. \
If you would like to contribute code, see the open issues for something to work on, or open up a PR.

### Continuous Integration
This project uses [Travis][travis] for continuous integration. Travis will run tests on all opened PRs.

### Testing
This project uses [PyTest][pytest] as a unit testing framework.  
To run all unit tests, run `python -m pytest` when in the top level (repository) directory.

Please add unit tests for any code affecting the [`draughts`][draughts] package. Don't unit test machine learning code.

### Code quality
[Black][black] is used to automatically format code. Either run `black .` in the top level directory, or use [precommit][precommit].


[black]: https://github.com/psf/black
[precommit]: https://pre-commit.com
[pytest]: https://pytest.org/en/latest/

[draughts]: alphadraughts/draughts
