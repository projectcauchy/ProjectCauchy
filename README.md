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
