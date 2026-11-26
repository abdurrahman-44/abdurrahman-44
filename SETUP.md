# Developer Lab V2 setup

Upload README.md, assets/, scripts/ and .github/workflows/ to the root of the existing public profile repository. Replace the old snake workflow rather than keeping duplicates. Do not upload secrets. Run each workflow manually in Actions. Each generated feature uses a separate output branch (snake retains output). Images may be missing until first successful run. For metrics create an empty metrics-output branch if the action cannot create it. Enable Actions and allow repository write permissions if required.

## Metrics
Create a GitHub personal access token with only the access needed for public metrics (classic token without additional scopes for public data where supported). Save as repository Actions secret METRICS_TOKEN. Private metrics are not enabled. See https://github.com/lowlighter/metrics for permissions and troubleshooting.

## Spotify
Create an app at https://developer.spotify.com/dashboard and register a redirect URI allowed by Spotify, e.g. http://127.0.0.1:8888/callback. Use the authorization code flow documented at https://developer.spotify.com/documentation/web-api/tutorials/code-flow with scope user-read-currently-playing. Authorize your own account and exchange the code for a refresh token. Store client ID, client secret and refresh token as Actions secrets SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REFRESH_TOKEN. Never commit tokens. Spotify app eligibility and API restrictions may apply. Run Spotify lab radio manually. The card is a public snapshot refreshed approximately every 30 minutes, not live streaming; GitHub scheduling and image caching can delay it. It publishes track and artist names, so omit the section and disable the workflow if you prefer privacy. No credentials produces an offline card.

## Notes
Third-party actions and image services may change or fail. Review their source and pin to verified commit SHAs before production use; versions in this package are not live verified. GitHub may cache SVGs and browser animation support varies. The profile counter is approximate. To disable any feature remove its README section and disable its workflow. GitHub scheduled workflows may be delayed or disabled after inactivity.
