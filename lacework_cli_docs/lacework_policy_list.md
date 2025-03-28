# `lacework policy list`

```
List all registered policies in your Lacework account.

Usage:
  lacework policy list [flags]

Aliases:
  list, ls

Flags:
      --alert_enabled     only show alert_enabled policies
      --enabled           only show enabled policies
  -h, --help              help for list
      --severity string   filter policies by severity threshold (critical, high, medium, low, info)
      --tag string        only show policies with the specified tag

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
```
