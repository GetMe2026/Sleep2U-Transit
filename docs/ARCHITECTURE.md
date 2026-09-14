# Travel2U transit architecture — v2

## Goal

Travel2U builds a door-to-door morning/travel plan without making the Sleep2U APK carry Europe-wide timetable databases.

The repository is a public catalog and future Travel-Pack build source. Personal travel information stays on the device.

## Privacy boundary

Never commit:
- home/work addresses;
- hotel addresses tied to a user;
- calendar events;
- flight reservations or booking references;
- device identifiers;
- API keys, developer secrets or tokens.

## Provider selection

Travel2U selects a provider by:
1. country;
2. region/city;
3. supported mode;
4. status/reliability;
5. availability of a cached Travel Pack;
6. optional realtime availability.

A provider may be `active` even when realtime is unavailable. In that case the UI must label data as **Dienstregeling**, not **Live**.

## Travel Packs

Full GTFS archives are normally `processor-only`. A future GitHub Action or dedicated processor:
- downloads the original GTFS;
- validates required files;
- removes unused shapes/data for the requested pack;
- produces compact regional/date-scoped artifacts;
- publishes checksums and metadata.

The Android app downloads only the relevant pack, preferably on Wi‑Fi before travel.

## Realtime

Realtime is never required for the alarm engine.

Near a planned journey:
- if GTFS-RT is configured, fetch a small live update;
- merge it into the scheduled itinerary;
- expire it quickly;
- fall back to scheduled data if unavailable.

## Travel example

For a trip Netherlands → Eindhoven Airport → Girona Airport → Lloret de Mar:
- Netherlands leg: OVapi national Travel Pack (+ GTFS-RT when useful);
- Catalonia arrival leg: Generalitat interurban bus schedule;
- additional FGC/TMB providers only when the itinerary enters their coverage.

The app should never download “all of Spain” for one Costa Brava trip.

## Battery policy

- no continuous transit polling;
- no permanent location service;
- refresh only at app open, evening plan, alarm dismissal, or shortly before departure;
- realtime refresh is optional below low-battery thresholds;
- the exact alarm engine is completely isolated from transit/network failures.
