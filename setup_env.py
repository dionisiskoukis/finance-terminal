# setup_env.py
import sys
import subprocess

def ensure_dependencies():
    try:
        import h2
    except ImportError:
        print("Installing missing h2 package...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "httpx[http2]", "h2"])
        print("Installation complete! Please run the script one more time.")
        sys.exit()
