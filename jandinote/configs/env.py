from pathlib import Path
import environ


env = environ.Env()


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"

if Path(ENV_FILE).exists():
    env.read_env(str(ENV_FILE))