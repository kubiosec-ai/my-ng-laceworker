# `lacework configure lacework`

```
Configure settings that the Lacework CLI uses to interact with the Lacework
platform. These include your Lacework account, API access key and secret.

To create a set of API keys, log in to your Lacework account via WebUI and
navigate to Settings > API Keys and click + Create New. Enter a name for
the key and an optional description, then click Save. To get the secret key,
download the generated API key file.

Use the flag --json_file to preload the downloaded API key file.

If this command is run with no flags, the Lacework CLI will store all
settings under the default profile. The information in the default profile
is used any time you run a Lacework CLI command that doesn't explicitly
specify a profile to use.

You can configure multiple profiles by using the --profile flag. If a
config file does not exist (the default location is ~/.lacework.toml),
the Lacework CLI will create it for you.

Usage:
  lacework configure [flags]
  lacework configure [command]

Available Commands:
  list           List all configured profiles at ~/.lacework.toml
  show           Show current configuration data
  switch-profile Switch between configured profiles

Flags:
  -h, --help               help for configure
  -j, --json_file string   loads the API key JSON file downloaded from the WebUI

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

Use "lacework configure [command] --help" for more information about a command.
```
