# Fixable

Fixable is a lightweight, transparent browser diagnostics page with a tiny JSON health endpoint.

## Current architecture
- `index.html` — client-only diagnostics UI
- `api/main.py` — Vercel-compatible Python health endpoint
- `api/requirements.txt` — intentionally dependency-free

## Privacy and security
The original project was based on a Discord image logger. Its implementation attempted to collect IP/device/location information, contained browser-crashing behavior, and hard-coded a Discord webhook. The project has been replaced with a transparent diagnostics implementation.

Fixable now:
- performs browser diagnostics locally;
- does not request GPS;
- does not intentionally capture or forward visitor IP addresses;
- contains no Discord webhook credentials;
- contains no browser-crashing code;
- does not use stealth redirects;
- exposes only `GET /api/health` server-side.

## Deploying
The layout is designed for Vercel. No environment variables or third-party runtime dependencies are required.

## Development
Open `index.html` locally to use the client UI. The API endpoint requires a Python-capable serverless runtime.

## License
Add a project license before distributing Fixable.
