# `lacework policy-exception create`

```
Create a new policy exception. 

To create a new policy exception, run the command:

    lacework policy-exception create [policy_id]

If you run the command without providing the policy_id, a
list of policies is displayed in an interactive prompt.

Usage:
  lacework policy-exception create [policy_id] [flags]

Aliases:
  create, rm

Flags:
  -h, --help   help for create

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
