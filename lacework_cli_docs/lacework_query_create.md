# `lacework query create`

```
There are multiple ways you can create a query:

  * Typing the query into your default editor (via $EDITOR)
  * Piping a query to the Lacework CLI command (via $STDIN)
  * From a local file on disk using the flag '--file'
  * From a URL using the flag '--url'

There are also multiple formats you can use to define a query:

  * Javascript Object Notation (JSON)
  * YAML Ain't Markup Language (YAML)

To launch your default editor and create a new query.

    lacework lql create

The following example checks for unrestricted ingress to TCP port 445:

    ---
    queryId: LW_Custom_UnrestrictedIngressToTCP445
    queryText: |-
      {
          source {
              LW_CFG_AWS_EC2_SECURITY_GROUPS a,
              array_to_rows(a.RESOURCE_CONFIG:IpPermissions) as (ip_permissions),
              array_to_rows(ip_permissions:IpRanges) as (ip_ranges)
          }
          filter {
              ip_permissions:IpProtocol = 'tcp'
              and ip_permissions:FromPort = 445
              and ip_permissions:ToPort = 445
              and ip_ranges:CidrIp = '0.0.0.0/0'
          }
          return distinct {
              ACCOUNT_ALIAS,
              ACCOUNT_ID,
              ARN as RESOURCE_KEY,
              RESOURCE_REGION,
              RESOURCE_TYPE,
              SERVICE
          }
      }

A query is represented using JSON or YAML markup and must specify both 'queryId'
and 'queryText' keys. The above query uses YAML, specifies an identifier of
'LW_Custom_UnrestrictedIngressToTCP445', and identifies AWS EC2 security groups with
unrestricted access to TCP port 445. The queryText is expressed in Lacework Query
Language (LQL) syntax which is delimited by '{ }' and contains three sections:

  * Source data is specified in the 'source' clause. The source of data is the
  'LW_CFG_AWS_EC2_SECURITY_GROUPS' datasource. LQL queries generally refer to other 
  datasources, and customizable policies always target a suitable datasource.

  * Records of interest are specified by the 'filter' clause. In the example, the
  records available in 'LW_CFG_AWS_EC2_SECURITY_GROUPS' are filtered for those whose IP
  protocol is 'tcp', whose from and to port is '445', and CidrIP is '0.0.0.0/0'.
  The syntax for this filtering expression strongly resembles SQL.

  * The fields this query exposes are listed in the 'return' clause. Because there
  may be unwanted duplicates among result records when Lacework composes them from
  just these four columns, the distinct modifier is added. This behaves like a SQL
  'SELECT DISTINCT'. Each returned column in this case is just a field that is present
  in 'LW_CFG_AWS_EC2_SECURITY_GROUPS', but you can compose results by manipulating strings, 
  dates, JSON and numbers as well.

The resulting dataset is shaped like a table. The table's columns are named with the
names of the columns selected. If desired, you could alias them to other names as well.

For more information about LQL, visit:

  https://docs.lacework.com/lql-overview

Usage:
  lacework query create [flags]

Flags:
  -f, --file string   path to a query to create
  -h, --help          help for create
  -u, --url string    url to a query to create

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
