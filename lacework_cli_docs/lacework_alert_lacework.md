# `lacework alert`

```
Inspect and manage alerts.

Lacework provides real-time alerts that are interactive and manageable.

Each alert contains various metadata information, such as severity level, type,
status, alert category, and associated tags.

You can also post a comment to an alert's timeline; or change an alert status
from Open to Closed.

For more information about alerts, visit:

https://docs.lacework.com/console/alerts-overview

To view all alerts in your Lacework account.

    lacework alert ls

To show an alert.

    lacework alert show <alert_id>

To close an alert.

    lacework alert close <alert_id>

Usage:
  lacework alert [command]

Aliases:
  alert, alerts

Available Commands:
  close       Close an alert
  comment     Add a comment
  list        List all alerts
  open        Open a specified alert in a web browser
  show        Show details about a specific alert

Flags:
  -h, --help   help for alert

Global Flags:
  -a, --account string      account subdomain of URL (i.e. <ACCOUNT>.lacework.net)
  -k, --api_key string      access key id
  -s, --api_secret string   secret access key
      --api_token string    access token (replaces the use of api_key and api_secret)
      --debug               turn on debug logging
      --json                switch commands output from human-readable to json format
      --nocache             turn off caching
      --nocolor             turn off colors
      --noninteractive      turn off interactive mode (disable spinners, prompts, etc.)
      --organization        access organization level data sets (org admins only)
  -p, --profile string      switch between profiles configured at ~/.lacework.toml
      --subaccount string   sub-account name inside your organization (org admins only)

Use "lacework alert [command] --help" for more information about a command.
```
