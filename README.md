# Sleep2U-Transit — bootstrap v2

European transit provider catalog for **Sleep2U / Travel2U**.

The Android app remains small: this repository tells Travel2U which public transport sources exist, what they cover, and how trustworthy/current they should be treated.

## v2 coverage

- 🇳🇱 Netherlands — OVapi national scheduled + realtime
- 🇪🇸 Catalonia/Barcelona — Generalitat interurban bus, FGC, TMB
- 🇮🇹 Rome — scheduled + realtime
- 🇮🇹 Milan — scheduled
- 🇬🇷 Athens — OASA bus/trolley scheduled; STASY metro/tram included as testing until current service dates pass validation

See [`docs/PROVIDERS.md`](docs/PROVIDERS.md) and [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Entry point

`https://raw.githubusercontent.com/GetMe2026/Sleep2U-Transit/main/manifest.json`

## Important

GitHub is the catalog/pack layer, not a dynamic live route-planning server. Personal data never belongs here.

## Validate locally

```bash
python scripts/validate_catalog.py
```

The included GitHub Action validates the catalog after pushes/pull requests and once per day.
