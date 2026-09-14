#!/usr/bin/env python3
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
VALID_STATUSES = {"active", "testing", "disabled"}
VALID_RELIABILITY = {"verified", "verified-with-warnings", "testing"}

def load(rel):
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)

def require(ok, message):
    if not ok:
        raise SystemExit("ERROR: " + message)

def valid_https(value):
    p = urlparse(value)
    return p.scheme == "https" and bool(p.netloc)

manifest = load("manifest.json")
require(manifest.get("schemaVersion") == 2, "manifest must be schemaVersion 2")
require(valid_https(manifest["catalogUrl"]), "catalogUrl must use HTTPS")

catalog = load("providers/index.json")
require(catalog.get("schemaVersion") == 2, "providers/index.json must be schemaVersion 2")

count = 0
ids = set()

for country in catalog["countries"]:
    cc = country["countryCode"]
    require(len(cc) == 2 and cc.isupper(), f"invalid countryCode {cc}")
    for rel in country.get("providers", []):
        count += 1
        p = load(rel)
        require(p["schemaVersion"] == 2, f"{rel}: wrong schemaVersion")
        require(p["countryCode"] == cc, f"{rel}: country mismatch")
        require(p["id"] not in ids, f"{rel}: duplicate provider id")
        ids.add(p["id"])
        require(p["status"] in VALID_STATUSES, f"{rel}: invalid status")
        require(p["reliability"]["level"] in VALID_RELIABILITY,
                f"{rel}: invalid reliability level")
        require(valid_https(p["staticGtfs"]["url"]), f"{rel}: static GTFS URL must be HTTPS")
        for key, value in p.get("realtime", {}).items():
            if key in {"availability", "maxAgeMinutes", "publishedUpdateSecondsApprox"}:
                continue
            if isinstance(value, str):
                require(valid_https(value), f"{rel}: realtime {key} must use HTTPS")
        policy = p["appPolicy"]
        if not policy["allowDirectStaticGtfsFetch"]:
            require(p["staticGtfs"]["downloadPolicy"] == "processor-only",
                    f"{rel}: static direct fetch disabled but policy is not processor-only")
        if p["status"] == "testing":
            require(p["reliability"]["level"] == "testing",
                    f"{rel}: testing provider must use testing reliability")

print(f"Sleep2U-Transit v2 catalog OK: {count} providers across {len(catalog['countries'])} countries.")
