# `lacework agent aws-install`

```
Install the datacollector agent on all remote AWS hosts

Usage:
  lacework agent aws-install [command]

Available Commands:
  ec2ic       Use EC2InstanceConnect to securely connect to EC2 instances
  ec2ssh      Use SSH to securely connect to EC2 instances
  ec2ssm      Use SSM to securely install the Lacework agent on EC2 instances

Flags:
  -h, --help   help for aws-install

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

Use "lacework agent aws-install [command] --help" for more information about a command.
```
