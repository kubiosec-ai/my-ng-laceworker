# `lacework compliance aws`

```
Manage compliance reports for Amazon Web Services (AWS).

To list all AWS accounts configured in your account:

    lacework compliance aws list-accounts

To get the latest AWS compliance assessment report:

    lacework compliance aws get-report <account_id>

These reports run on a regular schedule, typically once a day.

Usage:
  lacework compliance aws [command]

Available Commands:
  get-report     Get the latest AWS compliance report
  list-accounts  List all AWS accounts configured
  scan           Scan triggers a new resource inventory scan
  search         Search for all known violations of a given resource arn

Flags:
  -h, --help   help for aws

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

Use "lacework compliance aws [command] --help" for more information about a command.
```
