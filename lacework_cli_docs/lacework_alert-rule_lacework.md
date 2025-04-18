# `lacework alert-rule lacework`

```
Manage alert rules to route events to the appropriate people or tools.

An alert rule has three parts:

  1. Alert channel(s) that should receive the event notification
  2. Event severity and categories to include
  3. Resource group(s) containing the subset of your environment to consider

Usage:
  lacework alert-rule [command]

Aliases:
  alert-rule, alert-rules, ar

Available Commands:
  create      Create a new alert rule
  delete      Delete a alert rule
  list        List all alert rules
  show        Show an alert rule by ID

Flags:
  -h, --help   help for alert-rule

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

Use "lacework alert-rule [command] --help" for more information about a command.
```
