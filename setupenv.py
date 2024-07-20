import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    import fastapi
    import uvicorn
except ImportError:
    print("FastAPI or Uvicorn not found. Installing...")
    install("fastapi")
    install("uvicorn")

print("All required packages are installed.")
