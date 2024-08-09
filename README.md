# Project Cauchy

More details:

[https://blog.cauchy.dad/posts/projectcauchy/](https://blog.cauchy.dad/posts/projectcauchy/)

# Getting Started

### Developing the `game-server`

```bash
cd game-server
# run in a virtual environment
pip install -r requirements.txt
uvicorn server.app:app
```

1. Game logic should live on `game-server/games` directory.
2. All FastAPI logic should live on `game-server/server` directory.
3. All modules in `games-server/games` should return a dataclass. Converting it to `json` will be handled by `games-server/server`
4. We can *intentionally* introduce errors into the game logic so that, when using machine learning, we can detect suspicious transactions.

### Developing the `app-server`
```bash
cd app-server
# run in a virtual environment
pip install -r requirements.txt
python server/app.py
```

1. ETL Pipeline logic should live on `app-server/games` directory
2. All invocation of ETL Pipeline for each game should live on `app-server/server` directory.
