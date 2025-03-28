# `lacework configure show`

```
Prints the current computed configuration data from the specified configuration
key. The order of precedence to compute the configuration is flags, environment
variables, and the configuration file ~/.lacework.toml. 

The available configuration keys are:

* profile
* account
* subaccount
* api_secret
* api_key

To show the configuration from a different profile, use the flag --profile.

    lacework configure show account --profile my-profile

Usage:
  lacework configure show <config_key> [flags]

Flags:
  -h, --help   help for show

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
