# `lacework team-member team-member,`

```
Manage Team Members to grant or restrict access to multiple Lacework Accounts. 
			  Team members can also be granted organization-level roles.

Usage:
  lacework team-member [command]

Aliases:
  team-member, team-members, tm

Available Commands:
  create      Create a new team member
  delete      Delete a team member
  list        List all team members
  show        Show a team member by id

Flags:
  -h, --help   help for team-member

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

Use "lacework team-member [command] --help" for more information about a command.
```
