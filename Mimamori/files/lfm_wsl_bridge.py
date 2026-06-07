import sys, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNNERS = ROOT / "models" / "audio_jp" / "runners"

def win_to_wsl(path):
    s = str(path)
    if len(s) >= 3 and s[1] == ":":
        drive = s[0].lower()
        rest = s[2:].replace("\\", "/")
        return f"/mnt/{drive}{rest}"
    return s.replace("\\", "/")

def convert_arg(a):
    p = Path(a)
    if p.exists():
        return win_to_wsl(str(p.resolve()))
    if len(a) >= 3 and a[1] == ":":
        return win_to_wsl(a)
    return a

candidates = list(RUNNERS.rglob("llama-liquid-audio-cli"))
if not candidates:
    print("ERROR: llama-liquid-audio-cli not found under runners.", file=sys.stderr)
    sys.exit(2)

runner_wsl = win_to_wsl(str(candidates[0].resolve()))
subprocess.run(["wsl", "chmod", "+x", runner_wsl], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

cmd = ["wsl", runner_wsl] + [convert_arg(a) for a in sys.argv[1:]]
proc = subprocess.run(cmd)
sys.exit(proc.returncode)
