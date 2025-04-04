# `lacework compliance azure`

```
Manage compliance reports for Azure Cloud.

To list all Azure tenants configured in your account:

    lacework compliance azure list-tenants

To list all Azure subscriptions from a tenant, use the command:

    lacework compliance azure list-subscriptions <tenant_id>

To get the latest Azure compliance assessment report, use the command:

    lacework compliance azure get-report <tenant_id> <subscription_id>

These reports run on a regular schedule, typically once a day.

Usage:
  lacework compliance azure [command]

Aliases:
  azure, az

Available Commands:
  get-report         Get the latest Azure compliance report
  list               List Azure tenants and subscriptions
  list-subscriptions List subscriptions `<tenant-id>`
  scan               Scan triggers a new resource inventory scan

Flags:
  -h, --help   help for azure

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

Use "lacework compliance azure [command] --help" for more information about a command.
```
