# `lacework`

```
The Lacework Command Line Interface is a tool that helps you manage the
Lacework cloud security platform. Use it to manage compliance reports,
external integrations, vulnerability scans, and other operations.

Start by configuring the Lacework CLI with the command:

    lacework configure

This will prompt you for your Lacework account and a set of API access keys.

Usage:
  lacework [command]

Available Commands:
  access-token            Generate temporary API access tokens
  account                 Manage accounts in an organization (org admins only)
  agent                   Manage Lacework agents
  alert                   Inspect and manage alerts
  alert-channel           Manage alert channels
  alert-profile           Manage alert profiles
  alert-rule              Manage alert rules
  api                     Helper to call Lacework's API
  cloud-account           Manage cloud accounts
  completion              Generate the autocompletion script for the specified shell
  compliance              Manage compliance reports
  component               Manage components
  configure               Configure the Lacework CLI
  container-registry      Manage container registries
  generate                Generate code to onboard your account
  help                    Help about any command
  policy                  Manage policies
  policy-exception        Manage policy exceptions
  query                   Run and manage queries
  report-rule             Manage report rules
  resource-group          Manage resource groups
  team-member             Manage team members
  version                 Print the Lacework CLI version
  vulnerability           Container and host vulnerability assessments
  vulnerability-exception Manage vulnerability exceptions

Flags:
  -a, --account string      account subdomain of URL (i.e. <ACCOUNT>.lacework.net)
  -k, --api_key string      access key id
  -s, --api_secret string   secret access key
      --api_token string    access token (replaces the use of api_key and api_secret)
      --debug               turn on debug logging
  -h, --help                help for lacework
      --json                switch commands output from human-readable to json format
      --nocache             turn off caching
      --nocolor             turn off colors
      --noninteractive      turn off interactive mode (disable spinners, prompts, etc.)
      --organization        access organization level data sets (org admins only)
  -p, --profile string      switch between profiles configured at ~/.lacework.toml
      --subaccount string   sub-account name inside your organization (org admins only)

Use "lacework [command] --help" for more information about a command.
```
