"""Mirror validated upstream Quantumult X AdvertisingLite rules verbatim."""

from __future__ import annotations

from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master"
FILES = {
    "QuantumultX/AdvertisingLite.conf": "rewrite/QuantumultX/AdvertisingLite/AdvertisingLite.conf",
    "QuantumultX/AdvertisingLite.list": "rewrite/QuantumultX/AdvertisingLite/AdvertisingLite.list",
    "LICENSE": "LICENSE",
}


def fetch(path: str) -> bytes:
    request = Request(f"{BASE}/{path}", headers={"User-Agent": "quantumultx-adblock-sync"})
    with urlopen(request, timeout=30) as response:
        if response.status != 200:
            raise ValueError(f"HTTP {response.status}: {path}")
        return response.read()


def validate(name: str, data: bytes) -> None:
    text = data.decode("utf-8-sig")
    if "<html" in text[:1000].lower() or "<!doctype" in text[:1000].lower():
        raise ValueError(f"HTML returned for {name}")
    if name.endswith(".conf"):
        if len(text.splitlines()) < 500 or "# NAME: AdvertisingLite" not in text or " url reject" not in text:
            raise ValueError(f"Invalid rewrite rules: {name}")
    elif name.endswith(".list"):
        if len(text.splitlines()) < 100 or "# NAME: AdvertisingLite" not in text:
            raise ValueError(f"Invalid filter rules: {name}")
    elif "GNU GENERAL PUBLIC LICENSE" not in text or "Version 2" not in text:
        raise ValueError("Unexpected upstream license")


def main() -> None:
    # Validate every download before writing any file.
    files = {name: fetch(source) for name, source in FILES.items()}
    for name, data in files.items():
        validate(name, data)
    for name, data in files.items():
        destination = ROOT / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists() or destination.read_bytes() != data:
            destination.write_bytes(data)
            print(f"updated {name}")
        else:
            print(f"unchanged {name}")


if __name__ == "__main__":
    main()
