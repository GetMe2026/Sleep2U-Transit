# Provider matrix — bootstrap v2

| Country/region | Provider | Scheduled | Realtime | Bootstrap status | Reliability |
|---|---|---:|---:|---|---|
| Netherlands | OVapi national | Yes | Yes | Active | High, verified with feed warnings |
| Catalonia | Generalitat interurban bus | Yes | Not configured | Active | High, verified with source warnings |
| Catalonia | FGC | Yes | Not configured | Active | High |
| Barcelona | TMB | Yes | Credential-required services available | Active | High |
| Rome | Roma Servizi per la Mobilità | Yes | Yes | Active | High |
| Milan | Comune di Milano / AMAT | Yes | Not configured | Active | High |
| Athens | OASA road (bus/trolley) | Yes | Not configured | Active | High |
| Athens | STASY metro/tram | Yes | Not configured | Testing | Medium until service-date validation |

## Reliability semantics

- **verified** — source identity and current feed provenance are verified.
- **verified-with-warnings** — source is legitimate and usable, but current source/feed validation contains warnings or known data-quality issues.
- **testing** — provider is known, but Travel2U must not present it as fully current until runtime/build-time checks pass.

This distinction is intentional. Sleep2U should always prefer a truthful “Dienstregeling” or “Beta” badge over presenting stale data as live.
