# `lacework cloud-account`

```
Manage cloud account integrations with Lacework

Usage:
  lacework cloud-account [command]

Aliases:
  cloud-account, cloud-accounts, cloud, ca

Available Commands:
  create       Create a new cloud account integration
  delete       Delete a cloud account integration
  list         List all available cloud account integrations
  migrate      Mark a GCPv1 (storage-based) cloud account integration for migration
  show         Show a single cloud account integration

Flags:
  -h, --help   help for cloud-account

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

Use "lacework cloud-account [command] --help" for more information about a command.
```
