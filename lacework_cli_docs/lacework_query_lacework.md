# `lacework query lacework`

```
Run and manage Lacework Query Language (LQL) queries.

LQL is a SQL-like query language for specifying the selection, filtering, and 
manipulation of data. Queries let you interactively request information from 
specified curated datasources.

Lacework ships a set of default LQL queries that are available in your account.

For more information about LQL, visit:

  https://docs.lacework.com/lql-overview

To view all LQL queries in your Lacework account.

    lacework query ls

To show a query.

    lacework query show <query_id>

To execute a query.

    lacework query run <query_id>

**Note: LQL syntax may change.**

Usage:
  lacework query [command]

Aliases:
  query, lql, queries

Available Commands:
  create         Create a query
  delete         Delete a query
  list           List queries
  list-sources   List Lacework query datasources
  preview-source Preview Lacework query datasource
  run            Run a query
  show           Show a query
  show-source    Show Lacework query datasource
  update         Update a query
  validate       Validate a query

Flags:
  -h, --help   help for query

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

Use "lacework query [command] --help" for more information about a command.
```
