# `lacework policy policy,`

```
Manage policies in your Lacework account.

Policies add annotated metadata to queries for improving the context of alerts,
reports, and information displayed in the Lacework Console.

Policies also facilitate the scheduled execution of Lacework queries.

Queries let you interactively request information from specified
curated datasources. Queries have a defined structure for authoring detections.

Lacework ships a set of default LQL policies that are available in your account.

Limitations:
  * The maximum number of records that each policy will return is 1000
  * The maximum number of API calls is 120 per hour for on-demand LQL query executions

To view all the policies in your Lacework account.

    lacework policy ls

To view more details about a single policy.

    lacework policy show <policy_id>

To view the LQL query associated with the policy, use the query ID.

    lacework query show <query_id>

**Note: LQL syntax may change.**

Usage:
  lacework policy [command]

Aliases:
  policy, policies

Available Commands:
  create      Create a policy
  delete      Delete a policy
  disable     Disable policies
  enable      Enable policies
  list        List all policies
  list-tags   List policy tags
  show        Show details about a policy
  update      Update a policy

Flags:
  -h, --help   help for policy

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

Use "lacework policy [command] --help" for more information about a command.
```
