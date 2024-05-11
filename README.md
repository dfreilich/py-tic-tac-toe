# py-tic-tac-toe
Python Tic Tac Toe Simulation

## Running:
To run the code, execute:
```commandline
make random # starts the random API docker container
make run
```
This will start the Tic Tac Toe game with two plays making random moves, until the game ends.

### Development
For development, it's recommended to set up pre-commit hooks to ensure code quality. Install pre-commit using:

```bash
pip install pre-commit
```

Then, initialize pre-commit in your repository:
```bash
pre-commit install
```

## Instructions:
Develop a Tic Tac Toe simulation.

### Technical Requirements
* There is no human input. Both player moves are simulated
* Moves should be determined using an external service, [Random API](https://github.com/brendanmaguire/random) (this service should be run locally; there is no deployed version to query)
* The game should stop as soon as there is a winner
* The winner and cells of the boards should be returned
* The interface to the solution can be either a CLI or a RESTful API

### Non-Functional Requirements
You should spend no more than 2-3 hours developing a solution. Feel free to add a `Next Steps` section to the README or `TODO` comments in the code with ideas for future
improvements.

### What will be evaluated?
The test is deliberately not complicated. It is designed to evaluate how the candidate structures their solution to a simple problem.
The submitted solution will be evaluated in the following areas:
* Functionality
* Code & README Clarity
* Testing (Unit tests are sufficient, integration tests are not required)
