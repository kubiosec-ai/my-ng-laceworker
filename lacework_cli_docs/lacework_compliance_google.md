# `lacework compliance google`

```
Manage compliance reports for Google Cloud.

To list all GCP organizations and projects configured in your account:

    lacework compliance gcp list

To list all GCP projects from an organization, use the command:

    lacework compliance gcp list-projects <organization_id>

To get the latest GCP compliance assessment report, use the command:

    lacework compliance gcp get-report <organization_id> <project_id>

These reports run on a regular schedule, typically once a day.

Usage:
  lacework compliance google [command]

Aliases:
  google, gcp

Available Commands:
  get-report     Get the latest GCP compliance report
  list           List gcp projects and organizations
  list-projects  List projects from an organization
  scan           Scan triggers a new resource inventory scan

Flags:
  -h, --help   help for google

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

Use "lacework compliance google [command] --help" for more information about a command.
```
