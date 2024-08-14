try:
    from .poker import poker_pipeline
except ImportError as e:
    print(f"Could not import poker_pipeline: {e}")

try:
    from .roulette import roulette_pipeline
except ImportError as e:
    print(f"Could not import roulette_pipeline: {e}")

try:
    from .baccarat import pipeline_baccarat
except ImportError as e:
    print(f"Could not import pipeline_baccarat: {e}")

try:
    from .blackjack import blackjack_pipeline
except ImportError as e:
    print(f"Could not import blackjack_pipeline: {e}")
