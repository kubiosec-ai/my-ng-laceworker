# `lacework policy update`

```
Update a policy.

A policy identifier is required to update a policy.

A policy identifier can be specified via:

1.  A policy update command argument

    lacework policy update my-policy-1

2. The policy update payload

    {
        "policy_id": "my-policy-1",
        "severity": "critical"
    }

A policy identifier specified via command argument always takes precedence over
a policy identifer specified via payload.

The severity of many policies can be updated at once by passing a list of policy identifiers:

	lacework policy update my-policy-1 my-policy-2 --severity critical

Usage:
  lacework policy update [policy_id...] [flags]

Flags:
  -f, --file string       path to a policy to update
  -h, --help              help for update
      --severity string   update the policy severity
  -u, --url string        url to a policy to update

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
