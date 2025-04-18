# `lacework alert-profile`

```
Manage alert profiles to define how your LQL queries get consumed into alerts.

An alert profile consists of the ID of the new profile, the ID of an existing profile that
the new profile extends, and a list of alert templates.

Usage:
  lacework alert-profile [command]

Aliases:
  alert-profile, alert-profiles, ap

Available Commands:
  create      Create a new alert profile
  delete      Delete an alert profile
  list        List all alert profiles
  show        Show an alert profile by ID
  update      Update alert templates from an existing alert profile

Flags:
  -h, --help   help for alert-profile

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

Use "lacework alert-profile [command] --help" for more information about a command.
```
