# `lacework resource-group`

```
Manage Lacework-identifiable assets via the use of resource groups.

Usage:
  lacework resource-group [command]

Aliases:
  resource-group, resource-groups, rg

Available Commands:
  create      Create a new resource group
  delete      Delete a resource group
  list        List all resource groups
  show        Get resource group by ID

Flags:
  -h, --help   help for resource-group

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

Use "lacework resource-group [command] --help" for more information about a command.
```
