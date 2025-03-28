# `lacework container-registry`

```
Manage container registry integrations with Lacework

Usage:
  lacework container-registry [command]

Aliases:
  container-registry, container-registries, cr

Available Commands:
  create      Create a new container registry integration
  delete      Delete a container registry integration
  list        List all available container registry integrations
  show        Show a single container registry integration

Flags:
  -h, --help   help for container-registry

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

Use "lacework container-registry [command] --help" for more information about a command.
```
