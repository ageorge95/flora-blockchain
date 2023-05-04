from __future__ import annotations

import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("FLORA_ROOT", "~/.flora/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("FLORA_KEYS_ROOT", "~/.flora_keys"))).resolve()

SIMULATOR_ROOT_PATH = Path(
    os.path.expanduser(os.getenv("FLORA_SIMULATOR_ROOT", f"{DEFAULT_ROOT_PATH.parent}/simulator"))
).resolve()
