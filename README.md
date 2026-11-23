# World of Games (WoG)

A console games application with persistent scoring, a Flask score service packaged in Docker, and a Selenium browser test.

## Project structure
```
.
├── app/
│   ├── MainGame.py              # console entry point
│   ├── Live.py                  # welcome message, menu, runs the selected game
│   ├── MemoryGame.py            # Memory Game
│   ├── GuessGame.py             # Guess Game
│   ├── CurrencyRouletteGame.py  # Currency Roulette (uses an exchange-rate API)
│   ├── Score.py                 # reads and writes the score
│   ├── Utils.py                 # shared settings and screen cleaner
│   └── MainScores.py            # Flask score service
├── tests/
│   ├── e2e.py                   # Selenium browser test
│   └── test_score.txt           # test score file (100) for the isolated test
├── Dockerfile
├── docker-compose.yml
├── docker-run-command.txt
└── requirements.txt
```

## Components
| Component | Responsibility |
|-----------|----------------|
| Console app (`app/MainGame.py`) | Lets the player choose a game and a difficulty from 1 to 5. A win adds `(difficulty * 3) + 5` points to the saved score. A loss or a cancelled round adds nothing. |
| Scoring layer (`app/Score.py`) | The only place that reads and writes the score file. A corrupt file or a failed write produces a clear error and never resets the score. |
| Score service (`app/MainScores.py`) | Flask app. `GET /` reads the score on every request and shows it in an element with `id="score"`. If the score cannot be read, it returns a red error message with HTTP 500. |
| Browser test (`tests/e2e.py`) | Opens the service in headless Chrome, waits for the `score` element and checks that it is a whole number from 1 to 1000. |

## Requirements
- Python 3.14 (tested on Ubuntu under WSL)
- Docker and Docker Compose
- Google Chrome (only for the browser test)

Python dependencies are listed in `requirements.txt` with pinned versions.

## Installation
On Ubuntu, install the venv module once:
```bash
sudo apt install python3.14-venv
```

Create a virtual environment and install the dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run `source .venv/bin/activate` in every new terminal before running the project.

## Configuration

### Currency API key
Currency Roulette gets the USD to ILS rate from [ExchangeRate-API](https://www.exchangerate-api.com). Get a free API key there and set it as an environment variable:

Linux / macOS / WSL:
```bash
export EXCHANGE_API_KEY="your-key-here"
```

Windows PowerShell:
```powershell
$env:EXCHANGE_API_KEY="your-key-here"
```

To keep it after closing the terminal, add the `export` line to `~/.bashrc` or `~/.zshrc`.

If the key is missing or wrong, the round is cancelled with an error message and no points are added. The other games work without it.

### Score file location
| Where | Score file |
|-------|-----------|
| Console app and local service | `Scores.txt` in the project root, no matter which directory you run from |
| Override | Set `SCORES_FILE` to another path |
| Docker container | `/Scores.txt`. The image includes an initial score of `0` |

`Scores.txt` must contain one non-negative whole number. If it does not exist, it is created with the first win.

## Running the console games
From the project root:
```bash
python3 app/MainGame.py
```

## Running the score service

### With Docker Compose
```bash
docker compose up --build
```
Open http://localhost:8777. The service listens on port 5000 inside the container, mapped to port 8777 on the host.

Stop it with:
```bash
docker compose down
```

### With docker run
See `docker-run-command.txt` for the build and run commands without Compose.

### Without Docker
```bash
python3 app/MainScores.py
```
Open http://localhost:5000. This reads the same `Scores.txt` that the console app writes, so a new win shows up after refreshing the page.

## Browser test
The test runs against a container that uses a separate test score file, so real game scores are never touched.

1. Make sure the test score file exists. If it is missing, Docker creates a directory in its place and the service will not start.
   ```bash
   echo 100 > tests/test_score.txt
   ```
2. Stop the Compose service if it is running, then start the container with the test file mounted at `/Scores.txt`:
   ```bash
   docker run -d --name wog-test -p 8777:5000 -v "$(pwd)/tests/test_score.txt:/Scores.txt" lidory4/wog-score:1.0
   ```
3. Run the test and check the exit code:
   ```bash
   python tests/e2e.py
   echo $?
   ```
4. Remove the test container:
   ```bash
   docker rm -f wog-test
   ```

Exit code `0` means the test passed. Any nonzero code means it failed. The test returns `-1`, which Linux shows as `255`. The test fails on a navigation error, a missing `score` element, non-numeric text, or a value outside 1 to 1000. The range 1 to 1000 applies only to this test, not to the game score.
