# `lacework agent token`

```
Manage agent access tokens in your account.

Agent tokens should be treated as secret and not published. A token uniquely identifies
a Lacework customer. If you suspect your token has been publicly exposed or compromised,
generate a new token, update the new token on all machines using the old token. When
complete, the old token can safely be disabled without interrupting Lacework services.

Usage:
  lacework agent token [command]

Aliases:
  token, tokens

Available Commands:
  create      Create a new agent access token
  list        List all agent access tokens
  show        Show details about an agent access token
  update      Update an agent access token

Flags:
  -h, --help   help for token

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

Use "lacework agent token [command] --help" for more information about a command.
```
