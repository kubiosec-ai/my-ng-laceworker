# Lacework CLI Documentation

This file contains combined documentation for all Lacework CLI commands.

## Table of Contents

- [lacework](#lacework)
- [lacework access-token](#lacework-access-token)
- [lacework access-token lacework](#lacework-access-token-lacework)
- [lacework account](#lacework-account)
- [lacework account account,](#lacework-account-account,)
- [lacework account lacework](#lacework-account-lacework)
- [lacework account list](#lacework-account-list)
- [lacework agent](#lacework-agent)
- [lacework agent aws-install](#lacework-agent-aws-install)
- [lacework agent gcp-install](#lacework-agent-gcp-install)
- [lacework agent install](#lacework-agent-install)
- [lacework agent lacework](#lacework-agent-lacework)
- [lacework agent list](#lacework-agent-list)
- [lacework agent token](#lacework-agent-token)
- [lacework alert-channel](#lacework-alert-channel)
- [lacework alert-channel alert-channel,](#lacework-alert-channel-alert-channel,)
- [lacework alert-channel create](#lacework-alert-channel-create)
- [lacework alert-channel delete](#lacework-alert-channel-delete)
- [lacework alert-channel lacework](#lacework-alert-channel-lacework)
- [lacework alert-channel list](#lacework-alert-channel-list)
- [lacework alert-channel show](#lacework-alert-channel-show)
- [lacework alert-profile](#lacework-alert-profile)
- [lacework alert-profile alert-profile,](#lacework-alert-profile-alert-profile,)
- [lacework alert-profile create](#lacework-alert-profile-create)
- [lacework alert-profile delete](#lacework-alert-profile-delete)
- [lacework alert-profile lacework](#lacework-alert-profile-lacework)
- [lacework alert-profile list](#lacework-alert-profile-list)
- [lacework alert-profile show](#lacework-alert-profile-show)
- [lacework alert-profile update](#lacework-alert-profile-update)
- [lacework alert-rule](#lacework-alert-rule)
- [lacework alert-rule 1.](#lacework-alert-rule-1.)
- [lacework alert-rule 2.](#lacework-alert-rule-2.)
- [lacework alert-rule 3.](#lacework-alert-rule-3.)
- [lacework alert-rule alert-rule,](#lacework-alert-rule-alert-rule,)
- [lacework alert-rule create](#lacework-alert-rule-create)
- [lacework alert-rule delete](#lacework-alert-rule-delete)
- [lacework alert-rule lacework](#lacework-alert-rule-lacework)
- [lacework alert-rule list](#lacework-alert-rule-list)
- [lacework alert-rule show](#lacework-alert-rule-show)
- [lacework alert](#lacework-alert)
- [lacework alert alert,](#lacework-alert-alert,)
- [lacework alert close](#lacework-alert-close)
- [lacework alert comment](#lacework-alert-comment)
- [lacework alert lacework](#lacework-alert-lacework)
- [lacework alert list](#lacework-alert-list)
- [lacework alert open](#lacework-alert-open)
- [lacework alert show](#lacework-alert-show)
- [lacework api](#lacework-api)
- [lacework api lacework](#lacework-api-lacework)
- [lacework cloud-account](#lacework-cloud-account)
- [lacework cloud-account cloud-account,](#lacework-cloud-account-cloud-account,)
- [lacework cloud-account create](#lacework-cloud-account-create)
- [lacework cloud-account delete](#lacework-cloud-account-delete)
- [lacework cloud-account lacework](#lacework-cloud-account-lacework)
- [lacework cloud-account list](#lacework-cloud-account-list)
- [lacework cloud-account migrate](#lacework-cloud-account-migrate)
- [lacework cloud-account show](#lacework-cloud-account-show)
- [lacework completion](#lacework-completion)
- [lacework completion bash](#lacework-completion-bash)
- [lacework completion fish](#lacework-completion-fish)
- [lacework completion lacework](#lacework-completion-lacework)
- [lacework completion powershell](#lacework-completion-powershell)
- [lacework completion zsh](#lacework-completion-zsh)
- [lacework compliance](#lacework-compliance)
- [lacework compliance aws](#lacework-compliance-aws)
- [lacework compliance azure](#lacework-compliance-azure)
- [lacework compliance compliance,](#lacework-compliance-compliance,)
- [lacework compliance google](#lacework-compliance-google)
- [lacework compliance lacework](#lacework-compliance-lacework)
- [lacework component](#lacework-component)
- [lacework component component,](#lacework-component-component,)
- [lacework component install](#lacework-component-install)
- [lacework component lacework](#lacework-component-lacework)
- [lacework component list](#lacework-component-list)
- [lacework component show](#lacework-component-show)
- [lacework component uninstall](#lacework-component-uninstall)
- [lacework component update](#lacework-component-update)
- [lacework configure](#lacework-configure)
- [lacework configure lacework](#lacework-configure-lacework)
- [lacework configure list](#lacework-configure-list)
- [lacework configure show](#lacework-configure-show)
- [lacework configure switch-profile](#lacework-configure-switch-profile)
- [lacework container-registry](#lacework-container-registry)
- [lacework container-registry container-registry,](#lacework-container-registry-container-registry,)
- [lacework container-registry create](#lacework-container-registry-create)
- [lacework container-registry delete](#lacework-container-registry-delete)
- [lacework container-registry lacework](#lacework-container-registry-lacework)
- [lacework container-registry list](#lacework-container-registry-list)
- [lacework container-registry show](#lacework-container-registry-show)
- [lacework generate](#lacework-generate)
- [lacework generate cloud-account](#lacework-generate-cloud-account)
- [lacework generate generate,](#lacework-generate-generate,)
- [lacework generate k8s](#lacework-generate-k8s)
- [lacework generate lacework](#lacework-generate-lacework)
- [lacework help](#lacework-help)
- [lacework help lacework](#lacework-help-lacework)
- [lacework lacework](#lacework-lacework)
- [lacework policy-exception](#lacework-policy-exception)
- [lacework policy-exception create](#lacework-policy-exception-create)
- [lacework policy-exception delete](#lacework-policy-exception-delete)
- [lacework policy-exception lacework](#lacework-policy-exception-lacework)
- [lacework policy-exception list](#lacework-policy-exception-list)
- [lacework policy-exception policy-exception,](#lacework-policy-exception-policy-exception,)
- [lacework policy-exception show](#lacework-policy-exception-show)
- [lacework policy](#lacework-policy)
- [lacework policy create](#lacework-policy-create)
- [lacework policy delete](#lacework-policy-delete)
- [lacework policy disable](#lacework-policy-disable)
- [lacework policy enable](#lacework-policy-enable)
- [lacework policy lacework](#lacework-policy-lacework)
- [lacework policy list-tags](#lacework-policy-list-tags)
- [lacework policy list](#lacework-policy-list)
- [lacework policy policy,](#lacework-policy-policy,)
- [lacework policy show](#lacework-policy-show)
- [lacework policy update](#lacework-policy-update)
- [lacework query](#lacework-query)
- [lacework query create](#lacework-query-create)
- [lacework query delete](#lacework-query-delete)
- [lacework query lacework](#lacework-query-lacework)
- [lacework query list-sources](#lacework-query-list-sources)
- [lacework query list](#lacework-query-list)
- [lacework query preview-source](#lacework-query-preview-source)
- [lacework query query,](#lacework-query-query,)
- [lacework query run](#lacework-query-run)
- [lacework query show-source](#lacework-query-show-source)
- [lacework query show](#lacework-query-show)
- [lacework query update](#lacework-query-update)
- [lacework query validate](#lacework-query-validate)
- [lacework report-rule](#lacework-report-rule)
- [lacework report-rule 1.](#lacework-report-rule-1.)
- [lacework report-rule 2.](#lacework-report-rule-2.)
- [lacework report-rule 3.](#lacework-report-rule-3.)
- [lacework report-rule 4.](#lacework-report-rule-4.)
- [lacework report-rule create](#lacework-report-rule-create)
- [lacework report-rule delete](#lacework-report-rule-delete)
- [lacework report-rule lacework](#lacework-report-rule-lacework)
- [lacework report-rule list](#lacework-report-rule-list)
- [lacework report-rule report-rule,](#lacework-report-rule-report-rule,)
- [lacework report-rule show](#lacework-report-rule-show)
- [lacework resource-group](#lacework-resource-group)
- [lacework resource-group create](#lacework-resource-group-create)
- [lacework resource-group delete](#lacework-resource-group-delete)
- [lacework resource-group lacework](#lacework-resource-group-lacework)
- [lacework resource-group list](#lacework-resource-group-list)
- [lacework resource-group resource-group,](#lacework-resource-group-resource-group,)
- [lacework resource-group show](#lacework-resource-group-show)
- [lacework team-member](#lacework-team-member)
- [lacework team-member create](#lacework-team-member-create)
- [lacework team-member delete](#lacework-team-member-delete)
- [lacework team-member lacework](#lacework-team-member-lacework)
- [lacework team-member list](#lacework-team-member-list)
- [lacework team-member show](#lacework-team-member-show)
- [lacework team-member team-member,](#lacework-team-member-team-member,)
- [lacework version](#lacework-version)
- [lacework version lacework](#lacework-version-lacework)
- [lacework vulnerability-exception](#lacework-vulnerability-exception)
- [lacework vulnerability-exception create](#lacework-vulnerability-exception-create)
- [lacework vulnerability-exception delete](#lacework-vulnerability-exception-delete)
- [lacework vulnerability-exception lacework](#lacework-vulnerability-exception-lacework)
- [lacework vulnerability-exception list](#lacework-vulnerability-exception-list)
- [lacework vulnerability-exception show](#lacework-vulnerability-exception-show)
- [lacework vulnerability-exception vulnerability-exception,](#lacework-vulnerability-exception-vulnerability-exception,)
- [lacework vulnerability](#lacework-vulnerability)
- [lacework vulnerability container](#lacework-vulnerability-container)
- [lacework vulnerability host](#lacework-vulnerability-host)
- [lacework vulnerability lacework](#lacework-vulnerability-lacework)
- [lacework vulnerability vulnerability,](#lacework-vulnerability-vulnerability,)

---

## lacework

```
The Lacework Command Line Interface is a tool that helps you manage the
Lacework cloud security platform. Use it to manage compliance reports,
external integrations, vulnerability scans, and other operations.

Start by configuring the Lacework CLI with the command:

    lacework configure

This will prompt you for your Lacework account and a set of API access keys.

Usage:
  lacework [command]

Available Commands:
  access-token            Generate temporary API access tokens
  account                 Manage accounts in an organization (org admins only)
  agent                   Manage Lacework agents
  alert                   Inspect and manage alerts
  alert-channel           Manage alert channels
  alert-profile           Manage alert profiles
  alert-rule              Manage alert rules
  api                     Helper to call Lacework's API
  cloud-account           Manage cloud accounts
  completion              Generate the autocompletion script for the specified shell
  compliance              Manage compliance reports
  component               Manage components
  configure               Configure the Lacework CLI
  container-registry      Manage container registries
  generate                Generate code to onboard your account
  help                    Help about any command
  policy                  Manage policies
  policy-exception        Manage policy exceptions
  query                   Run and manage queries
  report-rule             Manage report rules
  resource-group          Manage resource groups
  team-member             Manage team members
  version                 Print the Lacework CLI version
  vulnerability           Container and host vulnerability assessments
  vulnerability-exception Manage vulnerability exceptions

Flags:
  -a, --account string      account subdomain of URL (i.e. <ACCOUNT>.lacework.net)
  -k, --api_key string      access key id
  -s, --api_secret string   secret access key
      --api_token string    access token (replaces the use of api_key and api_secret)
      --debug               turn on debug logging
  -h, --help                help for lacework
      --json                switch commands output from human-readable to json format
      --nocache             turn off caching
      --nocolor             turn off colors
      --noninteractive      turn off interactive mode (disable spinners, prompts, etc.)
      --organization        access organization level data sets (org admins only)
  -p, --profile string      switch between profiles configured at ~/.lacework.toml
      --subaccount string   sub-account name inside your organization (org admins only)

Use "lacework [command] --help" for more information about a command.
```

---

## lacework access-token

```
Generates a temporary API access token that can be used to access the
Lacework API. The token will be valid for the duration that you specify.

Usage:
  lacework access-token [flags]

Flags:
  -d, --duration_seconds int   duration in seconds that the access token should remain valid (default 3600)
  -h, --help                   help for access-token

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

---

## lacework access-token lacework

```
Generates a temporary API access token that can be used to access the
Lacework API. The token will be valid for the duration that you specify.

Usage:
  lacework access-token [flags]

Flags:
  -d, --duration_seconds int   duration in seconds that the access token should remain valid (default 3600)
  -h, --help                   help for access-token

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

---

## lacework account

```
Manage accounts inside your Lacework organization.

An organization can contain multiple accounts so you can also manage components
such as alerts, resource groups, team members, and audit logs at a more granular
level inside an organization. A team member may have access to multiple accounts
and can easily switch between them.

To enroll your Lacework account in an organization follow the documentation:

  https://docs.lacework.com/organization-overview

Usage:
  lacework account [command]

Aliases:
  account, accounts, acc

Available Commands:
  list        List all accounts

Flags:
  -h, --help   help for account

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

Use "lacework account [command] --help" for more information about a command.
```

---

## lacework account account,

```
Manage accounts inside your Lacework organization.

An organization can contain multiple accounts so you can also manage components
such as alerts, resource groups, team members, and audit logs at a more granular
level inside an organization. A team member may have access to multiple accounts
and can easily switch between them.

To enroll your Lacework account in an organization follow the documentation:

  https://docs.lacework.com/organization-overview

Usage:
  lacework account [command]

Aliases:
  account, accounts, acc

Available Commands:
  list        List all accounts

Flags:
  -h, --help   help for account

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

Use "lacework account [command] --help" for more information about a command.
```

---

## lacework account lacework

```
Manage accounts inside your Lacework organization.

An organization can contain multiple accounts so you can also manage components
such as alerts, resource groups, team members, and audit logs at a more granular
level inside an organization. A team member may have access to multiple accounts
and can easily switch between them.

To enroll your Lacework account in an organization follow the documentation:

  https://docs.lacework.com/organization-overview

Usage:
  lacework account [command]

Aliases:
  account, accounts, acc

Available Commands:
  list        List all accounts

Flags:
  -h, --help   help for account

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

Use "lacework account [command] --help" for more information about a command.
```

---

## lacework account list

```
List all accounts in your organization.

Usage:
  lacework account list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework agent

```
Manage agents and agent access tokens in your account.

To analyze application, host, and user behavior, Lacework uses a lightweight agent,
which securely forwards collected metadata to the Lacework cloud for analysis. The
agent requires minimal system resources and runs on most 64-bit Linux distributions.

For a complete list of supported operating systems, visit:

  https://docs.lacework.com/supported-operating-systems

Usage:
  lacework agent [command]

Available Commands:
  aws-install Install the datacollector agent on all remote AWS hosts
  gcp-install Install the datacollector agent on all remote GCE hosts
  install     Install the datacollector agent on a remote host
  list        List all hosts with a running agent
  token       Manage agent access tokens

Flags:
  -h, --help   help for agent

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

Use "lacework agent [command] --help" for more information about a command.
```

---

## lacework agent aws-install

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

---

## lacework agent gcp-install

```
Install the datacollector agent on all remote GCE hosts

Usage:
  lacework agent gcp-install [command]

Available Commands:
  osl         Use OSLogin to securely connect to GCE instances

Flags:
  -h, --help   help for gcp-install

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

Use "lacework agent gcp-install [command] --help" for more information about a command.
```

---

## lacework agent install

```
For single host installation of the Lacework agent via Secure Shell (SSH).

When this command is executed without any additional flag, an interactive prompt will be
launched to help gather the necessary authentication information to access the remote host.

To authenticate to the remote host with a username and password.

    lacework agent install <host> --ssh_username <your-user> --ssh_password <secret>

To authenticate to the remote host with an identity file instead.

    lacework agent install <user@host> -i /path/to/your/key

To provide an agent access token of your choice, use the command 'lacework agent token list',
select a token and pass it to the '--token' flag.

    lacework agent install <user@host> -i /path/to/your/key --token <token>

To authenticate to the remote host on a non-standard SSH port use the '--ssh_port' flag or
pass it directly via the argument.

    lacework agent install <user@host:port>

To explicitly specify the server URL that the agent will connect to:

    lacework agent install --server_url https://your.server.url.lacework.net

To list all active agents in your environment. 

    lacework agent list

NOTE: New agents could take up to an hour to report back to the platform.

Usage:
  lacework agent install <[user@]host[:port]> [flags]

Flags:
      --force                  override any pre-installed agent
  -h, --help                   help for install
  -i, --identity_file string   identity (private key) for public key authentication (default "~/.ssh/id_rsa")
      --server_url https://    server URL that agents will talk to, prefixed with https:// (default "https://agent.lacework.net")
      --ssh_password string    password for authentication
      --ssh_port int           port to connect to on the remote host (default 22)
      --ssh_username string    username to login with
      --token string           agent access token
      --trust_host_key         automatically add host keys to the ~/.ssh/known_hosts file

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

---

## lacework agent lacework

```
Manage agents and agent access tokens in your account.

To analyze application, host, and user behavior, Lacework uses a lightweight agent,
which securely forwards collected metadata to the Lacework cloud for analysis. The
agent requires minimal system resources and runs on most 64-bit Linux distributions.

For a complete list of supported operating systems, visit:

  https://docs.lacework.com/supported-operating-systems

Usage:
  lacework agent [command]

Available Commands:
  aws-install Install the datacollector agent on all remote AWS hosts
  gcp-install Install the datacollector agent on all remote GCE hosts
  install     Install the datacollector agent on a remote host
  list        List all hosts with a running agent
  token       Manage agent access tokens

Flags:
  -h, --help   help for agent

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

Use "lacework agent [command] --help" for more information about a command.
```

---

## lacework agent list

```
List all hosts that have a running agent in your environment.

You can use 'key:value' pairs to filter the list of hosts with the --filter flag.

    lacework agent list --filter 'os:Linux' --filter 'tags.VpcId:vpc-72225916'

**NOTE:** The value can be a regular expression such as 'hostname:db-server.*'

To filter hosts with a running agent version '5.8.0'.

    lacework agent list --filter 'agentVersion:5.8.0.*' --filter 'status:ACTIVE'

The available keys for this command are:
    * agentVersion
    * hostname
    * ipAddr
    * mid
    * mode
    * os
    * status
    * tags.arch
    * tags.ExternalIp
    * tags.Hostname
    * tags.InstanceId
    * tags.InternalIp
    * tags.LwTokenShort
    * tags.os
    * tags.VmInstanceType
    * tags.VmProvider
    * tags.Zone
    * tags.Account
    * tags.AmiId
    * tags.Name
    * tags.SubnetId
    * tags.VpcId
    * tags.Cluster
    * tags.cluster-location
    * tags.cluster-name
    * tags.cluster-uid
    * tags.created-by
    * tags.enable-oslogin
    * tags.Env
    * tags.GCEtags
    * tags.gci-ensure-gke-docker
    * tags.gci-update-strategy
    * tags.google-compute-enable-pcid
    * tags.InstanceName
    * tags.InstanceTemplate
    * tags.kube-labels
    * tags.lw_KubernetesCluster
    * tags.NumericProjectId
    * tags.ProjectId

Usage:
  lacework agent list [flags]

Aliases:
  list, ls

Flags:
      --filter strings   filter results by key:value pairs (e.g. 'hostname:db-server.*')
  -h, --help             help for list

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

---

## lacework agent token

```
Manage agent access tokens in your account.

Agent tokens should be treated as secret and not published. A token uniquely identifies
a Lacework customer. If you suspect your token has been publicly exposed or compromised,
generate a new token, update the new token on all machines using the old token. When
complete, the old token can safely be disabled without interrupting Lacework services.

Usage:
  lacework agent token [command]

Aliases:
  token, tokens

Available Commands:
  create      Create a new agent access token
  list        List all agent access tokens
  show        Show details about an agent access token
  update      Update an agent access token

Flags:
  -h, --help   help for token

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

Use "lacework agent token [command] --help" for more information about a command.
```

---

## lacework alert-channel

```
Manage alert channels integrations with Lacework

Usage:
  lacework alert-channel [command]

Aliases:
  alert-channel, alert-channels, ac

Available Commands:
  create      Create a new alert channel integration
  delete      Delete a alert channel integration
  list        List all available alert channel integrations
  show        Show a single alert channel integration

Flags:
  -h, --help   help for alert-channel

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

Use "lacework alert-channel [command] --help" for more information about a command.
```

---

## lacework alert-channel alert-channel,

```
Manage alert channels integrations with Lacework

Usage:
  lacework alert-channel [command]

Aliases:
  alert-channel, alert-channels, ac

Available Commands:
  create      Create a new alert channel integration
  delete      Delete a alert channel integration
  list        List all available alert channel integrations
  show        Show a single alert channel integration

Flags:
  -h, --help   help for alert-channel

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

Use "lacework alert-channel [command] --help" for more information about a command.
```

---

## lacework alert-channel create

```
Create a new alert channel integration

Usage:
  lacework alert-channel create [flags]

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

---

## lacework alert-channel delete

```
Delete a alert channel integration

Usage:
  lacework alert-channel delete [flags]

Aliases:
  delete, rm

Flags:
  -h, --help   help for delete

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

---

## lacework alert-channel lacework

```
Manage alert channels integrations with Lacework

Usage:
  lacework alert-channel [command]

Aliases:
  alert-channel, alert-channels, ac

Available Commands:
  create      Create a new alert channel integration
  delete      Delete a alert channel integration
  list        List all available alert channel integrations
  show        Show a single alert channel integration

Flags:
  -h, --help   help for alert-channel

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

Use "lacework alert-channel [command] --help" for more information about a command.
```

---

## lacework alert-channel list

```
List all available alert channel integrations

Usage:
  lacework alert-channel list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework alert-channel show

```
Show a single alert channel integration

Usage:
  lacework alert-channel show [flags]

Aliases:
  show, get

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

---

## lacework alert-profile

```
Manage alert profiles to define how your LQL queries get consumed into alerts.

An alert profile consists of the ID of the new profile, the ID of an existing profile that
the new profile extends, and a list of alert templates.

Usage:
  lacework alert-profile [command]

Aliases:
  alert-profile, alert-profiles, ap

Available Commands:
  create      Create a new alert profile
  delete      Delete an alert profile
  list        List all alert profiles
  show        Show an alert profile by ID
  update      Update alert templates from an existing alert profile

Flags:
  -h, --help   help for alert-profile

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

Use "lacework alert-profile [command] --help" for more information about a command.
```

---

## lacework alert-profile alert-profile,

```
Manage alert profiles to define how your LQL queries get consumed into alerts.

An alert profile consists of the ID of the new profile, the ID of an existing profile that
the new profile extends, and a list of alert templates.

Usage:
  lacework alert-profile [command]

Aliases:
  alert-profile, alert-profiles, ap

Available Commands:
  create      Create a new alert profile
  delete      Delete an alert profile
  list        List all alert profiles
  show        Show an alert profile by ID
  update      Update alert templates from an existing alert profile

Flags:
  -h, --help   help for alert-profile

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

Use "lacework alert-profile [command] --help" for more information about a command.
```

---

## lacework alert-profile create

```
Create a new alert profile

Usage:
  lacework alert-profile create [flags]

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

---

## lacework alert-profile delete

```
Delete a single alert profile by its ID.

Usage:
  lacework alert-profile delete <alert_profile_id> [flags]

Flags:
  -h, --help   help for delete

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

---

## lacework alert-profile lacework

```
Manage alert profiles to define how your LQL queries get consumed into alerts.

An alert profile consists of the ID of the new profile, the ID of an existing profile that
the new profile extends, and a list of alert templates.

Usage:
  lacework alert-profile [command]

Aliases:
  alert-profile, alert-profiles, ap

Available Commands:
  create      Create a new alert profile
  delete      Delete an alert profile
  list        List all alert profiles
  show        Show an alert profile by ID
  update      Update alert templates from an existing alert profile

Flags:
  -h, --help   help for alert-profile

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

Use "lacework alert-profile [command] --help" for more information about a command.
```

---

## lacework alert-profile list

```
List all alert profiles configured in your Lacework account.

Usage:
  lacework alert-profile list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework alert-profile show

```
Show a single alert profile by its ID.

Usage:
  lacework alert-profile show <alert_profile_id> [flags]

Aliases:
  show, get

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

---

## lacework alert-profile update

```
Update alert templates from an existing alert profile

Usage:
  lacework alert-profile update [alert_profile_id] [flags]

Flags:
  -h, --help   help for update

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

---

## lacework alert-rule

```
Manage alert rules to route events to the appropriate people or tools.

An alert rule has three parts:

  1. Alert channel(s) that should receive the event notification
  2. Event severity and categories to include
  3. Resource group(s) containing the subset of your environment to consider

Usage:
  lacework alert-rule [command]

Aliases:
  alert-rule, alert-rules, ar

Available Commands:
  create      Create a new alert rule
  delete      Delete a alert rule
  list        List all alert rules
  show        Show an alert rule by ID

Flags:
  -h, --help   help for alert-rule

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

Use "lacework alert-rule [command] --help" for more information about a command.
```

---

## lacework alert-rule 1.

```
Manage alert rules to route events to the appropriate people or tools.

An alert rule has three parts:

  1. Alert channel(s) that should receive the event notification
  2. Event severity and categories to include
  3. Resource group(s) containing the subset of your environment to consider

Usage:
  lacework alert-rule [command]

Aliases:
  alert-rule, alert-rules, ar

Available Commands:
  create      Create a new alert rule
  delete      Delete a alert rule
  list        List all alert rules
  show        Show an alert rule by ID

Flags:
  -h, --help   help for alert-rule

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

Use "lacework alert-rule [command] --help" for more information about a command.
```

---

## lacework alert-rule 2.

```
Manage alert rules to route events to the appropriate people or tools.

An alert rule has three parts:

  1. Alert channel(s) that should receive the event notification
  2. Event severity and categories to include
  3. Resource group(s) containing the subset of your environment to consider

Usage:
  lacework alert-rule [command]

Aliases:
  alert-rule, alert-rules, ar

Available Commands:
  create      Create a new alert rule
  delete      Delete a alert rule
  list        List all alert rules
  show        Show an alert rule by ID

Flags:
  -h, --help   help for alert-rule

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

Use "lacework alert-rule [command] --help" for more information about a command.
```

---

## lacework alert-rule 3.

```
Manage alert rules to route events to the appropriate people or tools.

An alert rule has three parts:

  1. Alert channel(s) that should receive the event notification
  2. Event severity and categories to include
  3. Resource group(s) containing the subset of your environment to consider

Usage:
  lacework alert-rule [command]

Aliases:
  alert-rule, alert-rules, ar

Available Commands:
  create      Create a new alert rule
  delete      Delete a alert rule
  list        List all alert rules
  show        Show an alert rule by ID

Flags:
  -h, --help   help for alert-rule

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

Use "lacework alert-rule [command] --help" for more information about a command.
```

---

## lacework alert-rule alert-rule,

```
Manage alert rules to route events to the appropriate people or tools.

An alert rule has three parts:

  1. Alert channel(s) that should receive the event notification
  2. Event severity and categories to include
  3. Resource group(s) containing the subset of your environment to consider

Usage:
  lacework alert-rule [command]

Aliases:
  alert-rule, alert-rules, ar

Available Commands:
  create      Create a new alert rule
  delete      Delete a alert rule
  list        List all alert rules
  show        Show an alert rule by ID

Flags:
  -h, --help   help for alert-rule

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

Use "lacework alert-rule [command] --help" for more information about a command.
```

---

## lacework alert-rule create

```
Create a new alert rule

Usage:
  lacework alert-rule create [flags]

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

---

## lacework alert-rule delete

```
Delete a single alert rule by it's ID.

Usage:
  lacework alert-rule delete <alert_rule_id> [flags]

Flags:
  -h, --help   help for delete

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

---

## lacework alert-rule lacework

```
Manage alert rules to route events to the appropriate people or tools.

An alert rule has three parts:

  1. Alert channel(s) that should receive the event notification
  2. Event severity and categories to include
  3. Resource group(s) containing the subset of your environment to consider

Usage:
  lacework alert-rule [command]

Aliases:
  alert-rule, alert-rules, ar

Available Commands:
  create      Create a new alert rule
  delete      Delete a alert rule
  list        List all alert rules
  show        Show an alert rule by ID

Flags:
  -h, --help   help for alert-rule

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

Use "lacework alert-rule [command] --help" for more information about a command.
```

---

## lacework alert-rule list

```
List all alert rules configured in your Lacework account.

Usage:
  lacework alert-rule list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework alert-rule show

```
Show a single alert rule by it's ID.

Usage:
  lacework alert-rule show <alert_rule_id> [flags]

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

---

## lacework alert

```
Inspect and manage alerts.

Lacework provides real-time alerts that are interactive and manageable.

Each alert contains various metadata information, such as severity level, type,
status, alert category, and associated tags.

You can also post a comment to an alert's timeline; or change an alert status
from Open to Closed.

For more information about alerts, visit:

https://docs.lacework.com/console/alerts-overview

To view all alerts in your Lacework account.

    lacework alert ls

To show an alert.

    lacework alert show <alert_id>

To close an alert.

    lacework alert close <alert_id>

Usage:
  lacework alert [command]

Aliases:
  alert, alerts

Available Commands:
  close       Close an alert
  comment     Add a comment
  list        List all alerts
  open        Open a specified alert in a web browser
  show        Show details about a specific alert

Flags:
  -h, --help   help for alert

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

Use "lacework alert [command] --help" for more information about a command.
```

---

## lacework alert alert,

```
Inspect and manage alerts.

Lacework provides real-time alerts that are interactive and manageable.

Each alert contains various metadata information, such as severity level, type,
status, alert category, and associated tags.

You can also post a comment to an alert's timeline; or change an alert status
from Open to Closed.

For more information about alerts, visit:

https://docs.lacework.com/console/alerts-overview

To view all alerts in your Lacework account.

    lacework alert ls

To show an alert.

    lacework alert show <alert_id>

To close an alert.

    lacework alert close <alert_id>

Usage:
  lacework alert [command]

Aliases:
  alert, alerts

Available Commands:
  close       Close an alert
  comment     Add a comment
  list        List all alerts
  open        Open a specified alert in a web browser
  show        Show details about a specific alert

Flags:
  -h, --help   help for alert

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

Use "lacework alert [command] --help" for more information about a command.
```

---

## lacework alert close

```
Use this command to change the status of an alert to closed.

The reason for closing the alert must be provided from the following options:

  * 0 - Other
  * 1 - False positive
  * 2 - Not enough information
  * 3 - Malicious and have resolution in place
  * 4 - Expected because of routine testing.

Reasons may be provided inline or via prompt.

If you choose Other, a comment is required and should contain a brief explanation of why the alert is closed.
Comments may be provided inline or via editor.

**Note: A closed alert cannot be reopened. You will be prompted to confirm closure of the alert.  
This prompt can be bypassed with the --noninteractive flag**

Usage:
  lacework alert close <alert_id> [flags]

Flags:
  -c, --comment string   a comment to associate with the alert closure
  -h, --help             help for close
  -r, --reason int       the reason for closing the alert (default -1)

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

---

## lacework alert comment

```
Post a user comment on an alert's timeline .

Comments may be provided inline or via editor.

Usage:
  lacework alert comment <alert_id> [flags]

Flags:
  -c, --comment string   a comment to add to the alert
  -h, --help             help for comment

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

---

## lacework alert lacework

```
Inspect and manage alerts.

Lacework provides real-time alerts that are interactive and manageable.

Each alert contains various metadata information, such as severity level, type,
status, alert category, and associated tags.

You can also post a comment to an alert's timeline; or change an alert status
from Open to Closed.

For more information about alerts, visit:

https://docs.lacework.com/console/alerts-overview

To view all alerts in your Lacework account.

    lacework alert ls

To show an alert.

    lacework alert show <alert_id>

To close an alert.

    lacework alert close <alert_id>

Usage:
  lacework alert [command]

Aliases:
  alert, alerts

Available Commands:
  close       Close an alert
  comment     Add a comment
  list        List all alerts
  open        Open a specified alert in a web browser
  show        Show details about a specific alert

Flags:
  -h, --help   help for alert

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

Use "lacework alert [command] --help" for more information about a command.
```

---

## lacework alert list

```
List all alerts.

By default, alerts are shown for the last 24 hours.
Use a custom time range by suppling a range flag...

    lacework alert ls --range "last 7 days"

Or by specifying start and end flags.

    lacework alert ls --start "-7d@d" --end "now"

Start and end times may be specified in one of the following formats:
    A. A relative time specifier
    B. RFC3339 date and time
    C. Epoch time in milliseconds

To list open alerts of type "NewViolations" with high or critical severity.

    lacework alert ls --status Open --severity high --type NewViolations

Usage:
  lacework alert list [flags]

Aliases:
  list, ls

Flags:
      --end string        end time for alerts (default "now")
  -h, --help              help for list
      --range string      natural time range for alerts
      --severity string   filter alerts by severity threshold (critical, high, medium, low, info)
      --start string      start time for alerts (default "-24h")
      --status string     filter alerts by status (Open, Closed)
      --type string       filter alerts by type

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

---

## lacework alert open

```
Open a specified alert in a web browser.

Usage:
  lacework alert open <alert_id> [flags]

Flags:
  -h, --help   help for open

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

---

## lacework alert show

```
Show details about a specific alert.

There are different types of alert details that can be shown to assist
with alert investigation. These types are referred to as alert detail scopes.

The following alert detail scopes are available:

  * Details (default)
  * Investigation
  * Events
  * RelatedAlerts
  * Integrations
  * Timeline

View an alert's timeline details:

  lacework alert show <alert_id> --scope Timeline

Usage:
  lacework alert show <alert_id> [flags]

Flags:
  -h, --help           help for show
      --scope string   type of alert details to show (default "Details")

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

---

## lacework api

```

```

---

## lacework api lacework

```
Use this command as a helper to call any available Lacework API v2 endpoint.

### API v2

To list all available Lacework schema types:

    lacework api get /v2/schemas

To receive a json response of all machines within the given time window:

    lacework api post /api/v2/Entities/Machines/search -d "{}"

To receive a json response of all agents within the given time window:

    lacework api post /api/v2/AgentInfo/search -d "{}"

For a complete list of available API v2 endpoints visit:

    https://<ACCOUNT>.lacework.net/api/v2/docs

Usage:
  lacework api <method> <path> [flags]

Flags:
  -d, --data string   data to send only for post and patch requests
  -h, --help          help for api

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

---

## lacework cloud-account

```
Manage cloud account integrations with Lacework

Usage:
  lacework cloud-account [command]

Aliases:
  cloud-account, cloud-accounts, cloud, ca

Available Commands:
  create       Create a new cloud account integration
  delete       Delete a cloud account integration
  list         List all available cloud account integrations
  migrate      Mark a GCPv1 (storage-based) cloud account integration for migration
  show         Show a single cloud account integration

Flags:
  -h, --help   help for cloud-account

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

Use "lacework cloud-account [command] --help" for more information about a command.
```

---

## lacework cloud-account cloud-account,

```
Manage cloud account integrations with Lacework

Usage:
  lacework cloud-account [command]

Aliases:
  cloud-account, cloud-accounts, cloud, ca

Available Commands:
  create       Create a new cloud account integration
  delete       Delete a cloud account integration
  list         List all available cloud account integrations
  migrate      Mark a GCPv1 (storage-based) cloud account integration for migration
  show         Show a single cloud account integration

Flags:
  -h, --help   help for cloud-account

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

Use "lacework cloud-account [command] --help" for more information about a command.
```

---

## lacework cloud-account create

```
Create a new cloud account integration

Usage:
  lacework cloud-account create [flags]

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

---

## lacework cloud-account delete

```
Delete a cloud account integration

Usage:
  lacework cloud-account delete [flags]

Aliases:
  delete, rm

Flags:
  -h, --help   help for delete

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

---

## lacework cloud-account lacework

```
Manage cloud account integrations with Lacework

Usage:
  lacework cloud-account [command]

Aliases:
  cloud-account, cloud-accounts, cloud, ca

Available Commands:
  create       Create a new cloud account integration
  delete       Delete a cloud account integration
  list         List all available cloud account integrations
  migrate      Mark a GCPv1 (storage-based) cloud account integration for migration
  show         Show a single cloud account integration

Flags:
  -h, --help   help for cloud-account

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

Use "lacework cloud-account [command] --help" for more information about a command.
```

---

## lacework cloud-account list

```
List all available cloud account integrations

Usage:
  lacework cloud-account list [flags]

Aliases:
  list, ls

Flags:
  -h, --help          help for list
  -t, --type string   list all cloud accounts of a specific type

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

---

## lacework cloud-account migrate

```
Mark a GCPv1 (storage-based) cloud account integration for migration

Usage:
  lacework cloud-account migrate [flags]

Flags:
  -h, --help   help for migrate

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

---

## lacework cloud-account show

```
Show a single cloud account integration

Usage:
  lacework cloud-account show [flags]

Aliases:
  show, get

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

---

## lacework completion

```
Generate the autocompletion script for lacework for the specified shell.
See each sub-command's help for details on how to use the generated script.

Usage:
  lacework completion [command]

Available Commands:
  bash        Generate the autocompletion script for bash
  fish        Generate the autocompletion script for fish
  powershell  Generate the autocompletion script for powershell
  zsh         Generate the autocompletion script for zsh

Flags:
  -h, --help   help for completion

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

Use "lacework completion [command] --help" for more information about a command.
```

---

## lacework completion bash

```
Generate the autocompletion script for the bash shell.

This script depends on the 'bash-completion' package.
If it is not installed already, you can install it via your OS's package manager.

To load completions in your current shell session:

	source <(lacework completion bash)

To load completions for every new session, execute once:

#### Linux:

	lacework completion bash > /etc/bash_completion.d/lacework

#### macOS:

	lacework completion bash > $(brew --prefix)/etc/bash_completion.d/lacework

You will need to start a new shell for this setup to take effect.

Usage:
  lacework completion bash

Flags:
  -h, --help              help for bash
      --no-descriptions   disable completion descriptions

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

---

## lacework completion fish

```
Generate the autocompletion script for the fish shell.

To load completions in your current shell session:

	lacework completion fish | source

To load completions for every new session, execute once:

	lacework completion fish > ~/.config/fish/completions/lacework.fish

You will need to start a new shell for this setup to take effect.

Usage:
  lacework completion fish [flags]

Flags:
  -h, --help              help for fish
      --no-descriptions   disable completion descriptions

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

---

## lacework completion lacework

```
Generate the autocompletion script for lacework for the specified shell.
See each sub-command's help for details on how to use the generated script.

Usage:
  lacework completion [command]

Available Commands:
  bash        Generate the autocompletion script for bash
  fish        Generate the autocompletion script for fish
  powershell  Generate the autocompletion script for powershell
  zsh         Generate the autocompletion script for zsh

Flags:
  -h, --help   help for completion

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

Use "lacework completion [command] --help" for more information about a command.
```

---

## lacework completion powershell

```
Generate the autocompletion script for powershell.

To load completions in your current shell session:

	lacework completion powershell | Out-String | Invoke-Expression

To load completions for every new session, add the output of the above command
to your powershell profile.

Usage:
  lacework completion powershell [flags]

Flags:
  -h, --help              help for powershell
      --no-descriptions   disable completion descriptions

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

---

## lacework completion zsh

```
Generate the autocompletion script for the zsh shell.

If shell completion is not already enabled in your environment you will need
to enable it.  You can execute the following once:

	echo "autoload -U compinit; compinit" >> ~/.zshrc

To load completions in your current shell session:

	source <(lacework completion zsh)

To load completions for every new session, execute once:

#### Linux:

	lacework completion zsh > "${fpath[1]}/_lacework"

#### macOS:

	lacework completion zsh > $(brew --prefix)/share/zsh/site-functions/_lacework

You will need to start a new shell for this setup to take effect.

Usage:
  lacework completion zsh [flags]

Flags:
  -h, --help              help for zsh
      --no-descriptions   disable completion descriptions

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

---

## lacework compliance

```

```

---

## lacework compliance aws

```
Manage compliance reports for Amazon Web Services (AWS).

To list all AWS accounts configured in your account:

    lacework compliance aws list-accounts

To get the latest AWS compliance assessment report:

    lacework compliance aws get-report <account_id>

These reports run on a regular schedule, typically once a day.

Usage:
  lacework compliance aws [command]

Available Commands:
  get-report     Get the latest AWS compliance report
  list-accounts  List all AWS accounts configured
  scan           Scan triggers a new resource inventory scan
  search         Search for all known violations of a given resource arn

Flags:
  -h, --help   help for aws

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

Use "lacework compliance aws [command] --help" for more information about a command.
```

---

## lacework compliance azure

```
Manage compliance reports for Azure Cloud.

To list all Azure tenants configured in your account:

    lacework compliance azure list-tenants

To list all Azure subscriptions from a tenant, use the command:

    lacework compliance azure list-subscriptions <tenant_id>

To get the latest Azure compliance assessment report, use the command:

    lacework compliance azure get-report <tenant_id> <subscription_id>

These reports run on a regular schedule, typically once a day.

Usage:
  lacework compliance azure [command]

Aliases:
  azure, az

Available Commands:
  get-report         Get the latest Azure compliance report
  list               List Azure tenants and subscriptions
  list-subscriptions List subscriptions `<tenant-id>`
  scan               Scan triggers a new resource inventory scan

Flags:
  -h, --help   help for azure

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

Use "lacework compliance azure [command] --help" for more information about a command.
```

---

## lacework compliance compliance,

```
Manage compliance reports for Google, Azure, or AWS cloud providers.

Lacework cloud security platform provides continuous Compliance monitoring against
cloud security best practices and compliance standards as CIS, PCI DSS, SoC II and
HIPAA benchmark standards.

Get started by integrating one or more cloud accounts using the command:

    lacework cloud-account create

If you prefer to configure the integration via the WebUI, log in to your account at:

    https://<ACCOUNT>.lacework.net

Then navigate to Settings > Integrations > Cloud Accounts.

Use the following command to list all available integrations in your account:

    lacework cloud-account list

Usage:
  lacework compliance [command]

Aliases:
  compliance, comp

Available Commands:
  aws         Compliance for AWS
  azure       Compliance for Azure Cloud
  google      Compliance for Google Cloud

Flags:
  -h, --help   help for compliance

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

Use "lacework compliance [command] --help" for more information about a command.
```

---

## lacework compliance google

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

---

## lacework compliance lacework

```
Manage compliance reports for Google, Azure, or AWS cloud providers.

Lacework cloud security platform provides continuous Compliance monitoring against
cloud security best practices and compliance standards as CIS, PCI DSS, SoC II and
HIPAA benchmark standards.

Get started by integrating one or more cloud accounts using the command:

    lacework cloud-account create

If you prefer to configure the integration via the WebUI, log in to your account at:

    https://<ACCOUNT>.lacework.net

Then navigate to Settings > Integrations > Cloud Accounts.

Use the following command to list all available integrations in your account:

    lacework cloud-account list

Usage:
  lacework compliance [command]

Aliases:
  compliance, comp

Available Commands:
  aws         Compliance for AWS
  azure       Compliance for Azure Cloud
  google      Compliance for Google Cloud

Flags:
  -h, --help   help for compliance

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

Use "lacework compliance [command] --help" for more information about a command.
```

---

## lacework component

```
Manage components to extend your experience with the Lacework platform

Usage:
  lacework component [command]

Aliases:
  component, components

Available Commands:
  install     Install a new component
  list        List all components
  show        Show details about a component
  uninstall   Uninstall an existing component
  update      Update an existing component

Flags:
  -h, --help   help for component

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

Use "lacework component [command] --help" for more information about a command.
```

---

## lacework component component,

```
Manage components to extend your experience with the Lacework platform

Usage:
  lacework component [command]

Aliases:
  component, components

Available Commands:
  install     Install a new component
  list        List all components
  show        Show details about a component
  uninstall   Uninstall an existing component
  update      Update an existing component

Flags:
  -h, --help   help for component

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

Use "lacework component [command] --help" for more information about a command.
```

---

## lacework component install

```
Install a new component

Usage:
  lacework component install <component> [flags]

Flags:
  -h, --help             help for install
      --version string   require a specific version to be installed (default is latest)

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

---

## lacework component lacework

```
Manage components to extend your experience with the Lacework platform

Usage:
  lacework component [command]

Aliases:
  component, components

Available Commands:
  install     Install a new component
  list        List all components
  show        Show details about a component
  uninstall   Uninstall an existing component
  update      Update an existing component

Flags:
  -h, --help   help for component

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

Use "lacework component [command] --help" for more information about a command.
```

---

## lacework component list

```
List all available components and their current state

Usage:
  lacework component list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework component show

```
Show details about a component

Usage:
  lacework component show <component> [flags]

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

---

## lacework component uninstall

```
Uninstall an existing component

Usage:
  lacework component uninstall <component> [flags]

Aliases:
  uninstall, delete, remove, rm

Flags:
  -h, --help   help for uninstall

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

---

## lacework component update

```
Update an existing component

Usage:
  lacework component update <component> [flags]

Aliases:
  update, upgrade

Flags:
  -h, --help             help for update
      --version string   update to a specific version (default is latest)

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

---

## lacework configure

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

---

## lacework configure lacework

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

---

## lacework configure list

```
List all profiles configured into the config file ~/.lacework.toml

To switch profiles permanently use the command.

    lacework configure switch-profile profile2

Usage:
  lacework configure list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework configure show

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

---

## lacework configure switch-profile

```
Switch between profiles configured into the config file ~/.lacework.toml

An alternative to temporarily switch to a different profile in your current terminal
is to export the environment variable:

    export LW_PROFILE="my-profile"

Usage:
  lacework configure switch-profile <profile> [flags]

Aliases:
  switch-profile, switch, use

Flags:
  -h, --help   help for switch-profile

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

---

## lacework container-registry

```
Manage container registry integrations with Lacework

Usage:
  lacework container-registry [command]

Aliases:
  container-registry, container-registries, cr

Available Commands:
  create      Create a new container registry integration
  delete      Delete a container registry integration
  list        List all available container registry integrations
  show        Show a single container registry integration

Flags:
  -h, --help   help for container-registry

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

Use "lacework container-registry [command] --help" for more information about a command.
```

---

## lacework container-registry container-registry,

```
Manage container registry integrations with Lacework

Usage:
  lacework container-registry [command]

Aliases:
  container-registry, container-registries, cr

Available Commands:
  create      Create a new container registry integration
  delete      Delete a container registry integration
  list        List all available container registry integrations
  show        Show a single container registry integration

Flags:
  -h, --help   help for container-registry

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

Use "lacework container-registry [command] --help" for more information about a command.
```

---

## lacework container-registry create

```
Create a new container registry integration

Usage:
  lacework container-registry create [flags]

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

---

## lacework container-registry delete

```
Delete a container registry integration

Usage:
  lacework container-registry delete [flags]

Aliases:
  delete, rm

Flags:
  -h, --help   help for delete

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

---

## lacework container-registry lacework

```
Manage container registry integrations with Lacework

Usage:
  lacework container-registry [command]

Aliases:
  container-registry, container-registries, cr

Available Commands:
  create      Create a new container registry integration
  delete      Delete a container registry integration
  list        List all available container registry integrations
  show        Show a single container registry integration

Flags:
  -h, --help   help for container-registry

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

Use "lacework container-registry [command] --help" for more information about a command.
```

---

## lacework container-registry list

```
List all available container registry integrations

Usage:
  lacework container-registry list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework container-registry show

```
Show a single container registry integration

Usage:
  lacework container-registry show [flags]

Aliases:
  show, get

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

---

## lacework generate

```
Generate code to onboard your account and deploy Lacework into various cloud environments.

This command creates Infrastructure as Code (IaC) in the form of Terraform HCL, with the option of running
Terraform and deploying Lacework into AWS, Azure, GCP or OCI.

Usage:
  lacework generate [command]

Aliases:
  generate, gen

Available Commands:
  cloud-account Generate cloud integration IaC
  k8s           Generate Kubernetes integration IaC

Flags:
      --apply           run terraform apply without executing plan or prompting
  -h, --help            help for generate
      --output string   location to write generated content

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

Use "lacework generate [command] --help" for more information about a command.
```

---

## lacework generate cloud-account

```
Generate cloud-account IaC to deploy Lacework into a cloud environment.

This command creates Infrastructure as Code (IaC) in the form of Terraform HCL, with the option of running
Terraform and deploying Lacework into AWS, Azure, GCP or OCI.

Usage:
  lacework generate cloud-account [command]

Aliases:
  cloud-account, cloud, ca

Available Commands:
  aws         Generate and/or execute Terraform code for AWS integration
  azure       Generate and/or execute Terraform code for Azure integration
  gcp         Generate and/or execute Terraform code for GCP integration
  oci         Generate and/or execute Terraform code for OCI integration

Flags:
  -h, --help   help for cloud-account

Global Flags:
  -a, --account string      account subdomain of URL (i.e. <ACCOUNT>.lacework.net)
  -k, --api_key string      access key id
  -s, --api_secret string   secret access key
      --api_token string    access token (replaces the use of api_key and api_secret)
      --apply               run terraform apply without executing plan or prompting
      --debug               turn on debug logging
      --json                switch commands output from human-readable to json format
      --nocache             turn off caching
      --nocolor             turn off colors
      --noninteractive      turn off interactive mode (disable spinners, prompts, etc.)
      --organization        access organization level data sets (org admins only)
      --output string       location to write generated content
  -p, --profile string      switch between profiles configured at ~/.lacework.toml
      --subaccount string   sub-account name inside your organization (org admins only)

Use "lacework generate cloud-account [command] --help" for more information about a command.
```

---

## lacework generate generate,

```
Generate code to onboard your account and deploy Lacework into various cloud environments.

This command creates Infrastructure as Code (IaC) in the form of Terraform HCL, with the option of running
Terraform and deploying Lacework into AWS, Azure, GCP or OCI.

Usage:
  lacework generate [command]

Aliases:
  generate, gen

Available Commands:
  cloud-account Generate cloud integration IaC
  k8s           Generate Kubernetes integration IaC

Flags:
      --apply           run terraform apply without executing plan or prompting
  -h, --help            help for generate
      --output string   location to write generated content

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

Use "lacework generate [command] --help" for more information about a command.
```

---

## lacework generate k8s

```
Generate IaC to deploy Lacework into a Kubernetes platform.

This command creates Infrastructure as Code (IaC) in the form of Terraform HCL, with the option of running
Terraform and deploying Lacework into GKE.

Usage:
  lacework generate k8s [command]

Available Commands:
  eks         Generate and/or execute Terraform code for EKS integration
  gke         Generate and/or execute Terraform code for GKE integration

Flags:
  -h, --help   help for k8s

Global Flags:
  -a, --account string      account subdomain of URL (i.e. <ACCOUNT>.lacework.net)
  -k, --api_key string      access key id
  -s, --api_secret string   secret access key
      --api_token string    access token (replaces the use of api_key and api_secret)
      --apply               run terraform apply without executing plan or prompting
      --debug               turn on debug logging
      --json                switch commands output from human-readable to json format
      --nocache             turn off caching
      --nocolor             turn off colors
      --noninteractive      turn off interactive mode (disable spinners, prompts, etc.)
      --organization        access organization level data sets (org admins only)
      --output string       location to write generated content
  -p, --profile string      switch between profiles configured at ~/.lacework.toml
      --subaccount string   sub-account name inside your organization (org admins only)

Use "lacework generate k8s [command] --help" for more information about a command.
```

---

## lacework generate lacework

```
Generate code to onboard your account and deploy Lacework into various cloud environments.

This command creates Infrastructure as Code (IaC) in the form of Terraform HCL, with the option of running
Terraform and deploying Lacework into AWS, Azure, GCP or OCI.

Usage:
  lacework generate [command]

Aliases:
  generate, gen

Available Commands:
  cloud-account Generate cloud integration IaC
  k8s           Generate Kubernetes integration IaC

Flags:
      --apply           run terraform apply without executing plan or prompting
  -h, --help            help for generate
      --output string   location to write generated content

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

Use "lacework generate [command] --help" for more information about a command.
```

---

## lacework help

```
Help provides help for any command in the application.
Simply type lacework help [path to command] for full details.

Usage:
  lacework help [command] [flags]

Flags:
  -h, --help   help for help

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

---

## lacework help lacework

```
Help provides help for any command in the application.
Simply type lacework help [path to command] for full details.

Usage:
  lacework help [command] [flags]

Flags:
  -h, --help   help for help

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

---

## lacework lacework

```

```

---

## lacework policy-exception

```
Manage policy exceptions in your Lacework account.

To view all the policies in your Lacework account.

    lacework policy list

Usage:
  lacework policy-exception [command]

Aliases:
  policy-exception, policy-exceptions, pe, px

Available Commands:
  create      Create a policy exception
  delete      Delete a policy exception
  list        List all exceptions from a single policy
  show        Show details about a policy exception

Flags:
  -h, --help   help for policy-exception

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

Use "lacework policy-exception [command] --help" for more information about a command.
```

---

## lacework policy-exception create

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

---

## lacework policy-exception delete

```
Delete a policy exception. 

To remove a policy exception, run the delete command with policy ID and exception ID arguments:

    lacework policy-exception delete <policy_id> <exception_id>

Usage:
  lacework policy-exception delete <policy_id> <exception_id> [flags]

Aliases:
  delete, rm

Flags:
  -h, --help   help for delete

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

---

## lacework policy-exception lacework

```
Manage policy exceptions in your Lacework account.

To view all the policies in your Lacework account.

    lacework policy list

Usage:
  lacework policy-exception [command]

Aliases:
  policy-exception, policy-exceptions, pe, px

Available Commands:
  create      Create a policy exception
  delete      Delete a policy exception
  list        List all exceptions from a single policy
  show        Show details about a policy exception

Flags:
  -h, --help   help for policy-exception

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

Use "lacework policy-exception [command] --help" for more information about a command.
```

---

## lacework policy-exception list

```
List all of the policy exceptions from the provided policy ID.

Usage:
  lacework policy-exception list <policy_id> [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework policy-exception policy-exception,

```
Manage policy exceptions in your Lacework account.

To view all the policies in your Lacework account.

    lacework policy list

Usage:
  lacework policy-exception [command]

Aliases:
  policy-exception, policy-exceptions, pe, px

Available Commands:
  create      Create a policy exception
  delete      Delete a policy exception
  list        List all exceptions from a single policy
  show        Show details about a policy exception

Flags:
  -h, --help   help for policy-exception

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

Use "lacework policy-exception [command] --help" for more information about a command.
```

---

## lacework policy-exception show

```
Show the details of a policy exception.

Usage:
  lacework policy-exception show <policy_id> <exception_id> [flags]

Aliases:
  show, get

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

---

## lacework policy

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

---

## lacework policy create

```
Create a policy.

A policy is represented in either JSON or YAML format.

The following attributes are minimally required:

    ---
    title: My Policy
    enabled: false
    policyType: Violation
    alertEnabled: false
    alertProfile: Alert_Profile_ID.Alert_Template_Name
    evalFrequency: Daily
    queryId: MyQuery
    severity: high
    description: My Policy Description
    remediation: My Policy Remediation

Usage:
  lacework policy create [flags]

Flags:
  -f, --file string   path to a policy to create
  -h, --help          help for create
  -u, --url string    url to a policy to create

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

---

## lacework policy delete

```
Delete a policy by providing the policy ID.

Use the command 'lacework policy list' to list the registered policies in
your Lacework account.

Usage:
  lacework policy delete <policy_id> [flags]

Flags:
      --cascade   delete policy and its associated query
  -h, --help      help for delete

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

---

## lacework policy disable

```
Disable policies by ID or all policies matching a tag.

To disable a single policy by its ID:

	lacework policy disable lacework-policy-id

To disable many policies by ID provide a list of policy ids:

	lacework policy disable lacework-policy-id-one lacework-policy-id-two

To disable all policies for AWS CIS 1.4.0:

	lacework policy disable --tag framework:cis-aws-1-4-0

To disable all policies for GCP CIS 1.3.0:

	lacework policy disable --tag framework:cis-gcp-1-3-0

Usage:
  lacework policy disable [policy_id...] [flags]

Flags:
  -h, --help         help for disable
      --tag string   disable all policies with the specified tag

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

---

## lacework policy enable

```
Enable policies by ID or all policies matching a tag.

To enter the policy enable prompt:

	lacework policy enable

To enable a single policy by its ID:

	lacework policy enable lacework-policy-id

To enable many policies by ID provide a list of policy ids:

	lacework policy enable lacework-policy-id-one lacework-policy-id-two

To enable all policies for AWS CIS 1.4.0:

	lacework policy enable --tag framework:cis-aws-1-4-0

To enable all policies for GCP CIS 1.3.0:

	lacework policy enable --tag framework:cis-gcp-1-3-0

Usage:
  lacework policy enable [policy_id...] [flags]

Flags:
  -h, --help         help for enable
      --tag string   enable all policies with the specified tag

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

---

## lacework policy lacework

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

---

## lacework policy list-tags

```
List all tags associated with policies in your Lacework account.

Usage:
  lacework policy list-tags [flags]

Aliases:
  list-tags, ls

Flags:
  -h, --help   help for list-tags

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

---

## lacework policy list

```
List all registered policies in your Lacework account.

Usage:
  lacework policy list [flags]

Aliases:
  list, ls

Flags:
      --alert_enabled     only show alert_enabled policies
      --enabled           only show enabled policies
  -h, --help              help for list
      --severity string   filter policies by severity threshold (critical, high, medium, low, info)
      --tag string        only show policies with the specified tag

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

---

## lacework policy policy,

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

---

## lacework policy show

```
Show details about the provided policy ID.

Usage:
  lacework policy show <policy_id> [flags]

Aliases:
  show, ls

Flags:
  -h, --help   help for show
      --yaml   output query in YAML format

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

---

## lacework policy update

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

---

## lacework query

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

---

## lacework query create

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

---

## lacework query delete

```
Delete a single LQL query by providing the query ID.

Use the command 'lacework query list' to list the available queries in
your Lacework account.

Usage:
  lacework query delete <query_id> [flags]

Flags:
  -h, --help   help for delete

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

---

## lacework query lacework

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

---

## lacework query list-sources

```
List Lacework query datasources.

Usage:
  lacework query list-sources [flags]

Aliases:
  list-sources, sources

Flags:
  -h, --help   help for list-sources

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

---

## lacework query list

```
List all LQL queries in your Lacework account.

Usage:
  lacework query list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework query preview-source

```
Preview Lacework query datasource.

Usage:
  lacework query preview-source <datasource_id> [flags]

Flags:
  -h, --help   help for preview-source

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

---

## lacework query query,

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

---

## lacework query run

```
Run an LQL query via editor:

    lacework query run --range today

Run a query via ID (uses active profile):

    lacework query run MyQuery --start "-1w@w" --end "@w"

Start and end times are required to run a query:

1.  Specify start and end times in one of the following formats:

    A. A relative time specifier
    B. RFC3339 date and time
    C. Epoch time in milliseconds

2. Specify start and end times in one of the following ways:

    A. As StartTimeRange and EndTimeRange in the ParamInfo block within the query
    B. As start_time_range and end_time_range if specifying JSON
    C. As --start and --end CLI flags

3. Start and End time precedence:

    A. CLI flags take precedence over JSON specifications

Usage:
  lacework query run [query_id] [flags]

Aliases:
  run, execute

Flags:
      --empty                  start $EDITOR with empty file
      --end string             end time for query (default "now")
      --fail_on_count string   fail if the results from a query match the provided expression (e.g. '>0')
  -f, --file string            path to a query to run
  -h, --help                   help for run
      --limit int              result limit for query (default 0)
      --range string           natural time range for query
      --start string           start time for query (default "-24h")
  -u, --url string             url to a query to run
      --validate_only          validate query only (do not run)

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

---

## lacework query show-source

```
Show Lacework query datasource.

Usage:
  lacework query show-source <datasource_id> [flags]

Aliases:
  show-source, describe

Flags:
  -h, --help   help for show-source

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

---

## lacework query show

```
Show a query in your Lacework account.

Usage:
  lacework query show <query_id> [flags]

Flags:
  -h, --help   help for show
      --yaml   output query in YAML format

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

---

## lacework query update

```
There are multiple ways you can update a query:

  * Typing the query into your default editor (via $EDITOR)
  * Passing a query ID to load it into your default editor
  * From a local file on disk using the flag '--file'
  * From a URL using the flag '--url'

There are also multiple formats you can use to define a query:

  * Javascript Object Notation (JSON)
  * YAML Ain't Markup Language (YAML)

To launch your default editor and update a query.

    lacework query update

Usage:
  lacework query update [query_id] [flags]

Flags:
  -f, --file string   path to a query to update
  -h, --help          help for update
  -u, --url string    url to a query to update

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

---

## lacework query validate

```
Use this command to validate a single LQL query before creating it.

There are multiple ways you can validate a query:

  * Typing the query into your default editor (via $EDITOR)
  * From a local file on disk using the flag '--file'
  * From a URL using the flag '--url'

There are also multiple formats you can use to define a query:

  * Javascript Object Notation (JSON)
  * YAML Ain't Markup Language (YAML)

To launch your default editor and validate a query.

    lacework query validate

Usage:
  lacework query validate [flags]

Flags:
  -f, --file string   path to a query to validate
  -h, --help          help for validate
  -u, --url string    url to a query to validate

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

---

## lacework report-rule

```
Manage report rules to route reports to one or more email alert channels.		

A report rule has four parts:

  1. Email alert channel(s) that should receive the report
  2. One or more severities to include
  3. Resource group(s) containing the subset of your environment to consider
  4. Notification types containing which report information to send

Usage:
  lacework report-rule [command]

Aliases:
  report-rule, report-rules, rr

Available Commands:
  create      Create a new report rule
  delete      Delete a report rule
  list        List all report rules
  show        Show a report rule by ID

Flags:
  -h, --help   help for report-rule

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

Use "lacework report-rule [command] --help" for more information about a command.
```

---

## lacework report-rule 1.

```
Manage report rules to route reports to one or more email alert channels.		

A report rule has four parts:

  1. Email alert channel(s) that should receive the report
  2. One or more severities to include
  3. Resource group(s) containing the subset of your environment to consider
  4. Notification types containing which report information to send

Usage:
  lacework report-rule [command]

Aliases:
  report-rule, report-rules, rr

Available Commands:
  create      Create a new report rule
  delete      Delete a report rule
  list        List all report rules
  show        Show a report rule by ID

Flags:
  -h, --help   help for report-rule

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

Use "lacework report-rule [command] --help" for more information about a command.
```

---

## lacework report-rule 2.

```
Manage report rules to route reports to one or more email alert channels.		

A report rule has four parts:

  1. Email alert channel(s) that should receive the report
  2. One or more severities to include
  3. Resource group(s) containing the subset of your environment to consider
  4. Notification types containing which report information to send

Usage:
  lacework report-rule [command]

Aliases:
  report-rule, report-rules, rr

Available Commands:
  create      Create a new report rule
  delete      Delete a report rule
  list        List all report rules
  show        Show a report rule by ID

Flags:
  -h, --help   help for report-rule

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

Use "lacework report-rule [command] --help" for more information about a command.
```

---

## lacework report-rule 3.

```
Manage report rules to route reports to one or more email alert channels.		

A report rule has four parts:

  1. Email alert channel(s) that should receive the report
  2. One or more severities to include
  3. Resource group(s) containing the subset of your environment to consider
  4. Notification types containing which report information to send

Usage:
  lacework report-rule [command]

Aliases:
  report-rule, report-rules, rr

Available Commands:
  create      Create a new report rule
  delete      Delete a report rule
  list        List all report rules
  show        Show a report rule by ID

Flags:
  -h, --help   help for report-rule

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

Use "lacework report-rule [command] --help" for more information about a command.
```

---

## lacework report-rule 4.

```
Manage report rules to route reports to one or more email alert channels.		

A report rule has four parts:

  1. Email alert channel(s) that should receive the report
  2. One or more severities to include
  3. Resource group(s) containing the subset of your environment to consider
  4. Notification types containing which report information to send

Usage:
  lacework report-rule [command]

Aliases:
  report-rule, report-rules, rr

Available Commands:
  create      Create a new report rule
  delete      Delete a report rule
  list        List all report rules
  show        Show a report rule by ID

Flags:
  -h, --help   help for report-rule

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

Use "lacework report-rule [command] --help" for more information about a command.
```

---

## lacework report-rule create

```
Create a new report rule

Usage:
  lacework report-rule create [flags]

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

---

## lacework report-rule delete

```
Delete a single report rule by it's ID.

Usage:
  lacework report-rule delete <report_rule_id> [flags]

Flags:
  -h, --help   help for delete

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

---

## lacework report-rule lacework

```
Manage report rules to route reports to one or more email alert channels.		

A report rule has four parts:

  1. Email alert channel(s) that should receive the report
  2. One or more severities to include
  3. Resource group(s) containing the subset of your environment to consider
  4. Notification types containing which report information to send

Usage:
  lacework report-rule [command]

Aliases:
  report-rule, report-rules, rr

Available Commands:
  create      Create a new report rule
  delete      Delete a report rule
  list        List all report rules
  show        Show a report rule by ID

Flags:
  -h, --help   help for report-rule

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

Use "lacework report-rule [command] --help" for more information about a command.
```

---

## lacework report-rule list

```
List all report rules configured in your Lacework account.

Usage:
  lacework report-rule list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework report-rule report-rule,

```
Manage report rules to route reports to one or more email alert channels.		

A report rule has four parts:

  1. Email alert channel(s) that should receive the report
  2. One or more severities to include
  3. Resource group(s) containing the subset of your environment to consider
  4. Notification types containing which report information to send

Usage:
  lacework report-rule [command]

Aliases:
  report-rule, report-rules, rr

Available Commands:
  create      Create a new report rule
  delete      Delete a report rule
  list        List all report rules
  show        Show a report rule by ID

Flags:
  -h, --help   help for report-rule

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

Use "lacework report-rule [command] --help" for more information about a command.
```

---

## lacework report-rule show

```
Show a single report rule by it's ID.

Usage:
  lacework report-rule show <report_rule_id> [flags]

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

---

## lacework resource-group

```
Manage Lacework-identifiable assets via the use of resource groups.

Usage:
  lacework resource-group [command]

Aliases:
  resource-group, resource-groups, rg

Available Commands:
  create      Create a new resource group
  delete      Delete a resource group
  list        List all resource groups
  show        Get resource group by ID

Flags:
  -h, --help   help for resource-group

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

Use "lacework resource-group [command] --help" for more information about a command.
```

---

## lacework resource-group create

```
Creates a new single resource group.

Usage:
  lacework resource-group create [flags]

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

---

## lacework resource-group delete

```
Delete a single resource group by it's resource group ID.

Usage:
  lacework resource-group delete <resource_group_id> [flags]

Flags:
  -h, --help   help for delete

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

---

## lacework resource-group lacework

```
Manage Lacework-identifiable assets via the use of resource groups.

Usage:
  lacework resource-group [command]

Aliases:
  resource-group, resource-groups, rg

Available Commands:
  create      Create a new resource group
  delete      Delete a resource group
  list        List all resource groups
  show        Get resource group by ID

Flags:
  -h, --help   help for resource-group

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

Use "lacework resource-group [command] --help" for more information about a command.
```

---

## lacework resource-group list

```
List all resource groups configured in your Lacework account.

Usage:
  lacework resource-group list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework resource-group resource-group,

```
Manage Lacework-identifiable assets via the use of resource groups.

Usage:
  lacework resource-group [command]

Aliases:
  resource-group, resource-groups, rg

Available Commands:
  create      Create a new resource group
  delete      Delete a resource group
  list        List all resource groups
  show        Get resource group by ID

Flags:
  -h, --help   help for resource-group

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

Use "lacework resource-group [command] --help" for more information about a command.
```

---

## lacework resource-group show

```
Get a single resource group by it's resource group ID.

Usage:
  lacework resource-group show <resource_group_id> [flags]

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

---

## lacework team-member

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

---

## lacework team-member create

```
Create a new team member

Usage:
  lacework team-member create [flags]

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

---

## lacework team-member delete

```
Delete a single team member by it's ID.

Usage:
  lacework team-member delete <team_member_id> [flags]

Flags:
  -h, --help   help for delete

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

---

## lacework team-member lacework

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

---

## lacework team-member list

```
List all team members configured in your Lacework account.

Usage:
  lacework team-member list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework team-member show

```
Show a single team member by it's id.

Usage:
  lacework team-member show <team_member_id> [flags]

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

---

## lacework team-member team-member,

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

---

## lacework version

```
Prints out the installed version of the Lacework CLI and checks for newer
versions available for update.

Set the environment variable 'LW_UPDATES_DISABLE=1' to avoid checking for updates.

Usage:
  lacework version [flags]

Flags:
  -h, --help   help for version

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

---

## lacework version lacework

```
Prints out the installed version of the Lacework CLI and checks for newer
versions available for update.

Set the environment variable 'LW_UPDATES_DISABLE=1' to avoid checking for updates.

Usage:
  lacework version [flags]

Flags:
  -h, --help   help for version

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

---

## lacework vulnerability-exception

```
Manage vulnerability exceptions to control and customize your alert profile for hosts and containers.

Usage:
  lacework vulnerability-exception [command]

Aliases:
  vulnerability-exception, vulnerability-exceptions, ve, vuln-exception, vuln-exceptions

Available Commands:
  create      Create a new vulnerability exception
  delete      Delete a vulnerability exception
  list        List all vulnerability exceptions
  show        Get vulnerability exception by ID

Flags:
  -h, --help   help for vulnerability-exception

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

Use "lacework vulnerability-exception [command] --help" for more information about a command.
```

---

## lacework vulnerability-exception create

```
Creates a new single vulnerability exception.

Usage:
  lacework vulnerability-exception create [flags]

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

---

## lacework vulnerability-exception delete

```
Delete a single vulnerability exception by it's vulnerability exception ID.

Usage:
  lacework vulnerability-exception delete <exception_id> [flags]

Flags:
  -h, --help   help for delete

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

---

## lacework vulnerability-exception lacework

```
Manage vulnerability exceptions to control and customize your alert profile for hosts and containers.

Usage:
  lacework vulnerability-exception [command]

Aliases:
  vulnerability-exception, vulnerability-exceptions, ve, vuln-exception, vuln-exceptions

Available Commands:
  create      Create a new vulnerability exception
  delete      Delete a vulnerability exception
  list        List all vulnerability exceptions
  show        Get vulnerability exception by ID

Flags:
  -h, --help   help for vulnerability-exception

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

Use "lacework vulnerability-exception [command] --help" for more information about a command.
```

---

## lacework vulnerability-exception list

```
List all vulnerability exceptions configured in your Lacework account.

Usage:
  lacework vulnerability-exception list [flags]

Aliases:
  list, ls

Flags:
  -h, --help   help for list

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

---

## lacework vulnerability-exception show

```
Get a single vulnerability exception by it's vulnerability exception ID.

Usage:
  lacework vulnerability-exception show <exception_id> [flags]

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

---

## lacework vulnerability-exception vulnerability-exception,

```
Manage vulnerability exceptions to control and customize your alert profile for hosts and containers.

Usage:
  lacework vulnerability-exception [command]

Aliases:
  vulnerability-exception, vulnerability-exceptions, ve, vuln-exception, vuln-exceptions

Available Commands:
  create      Create a new vulnerability exception
  delete      Delete a vulnerability exception
  list        List all vulnerability exceptions
  show        Get vulnerability exception by ID

Flags:
  -h, --help   help for vulnerability-exception

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

Use "lacework vulnerability-exception [command] --help" for more information about a command.
```

---

## lacework vulnerability

```
Container and host vulnerability assessments.

Usage:
  lacework vulnerability [command]

Aliases:
  vulnerability, vuln, vul

Available Commands:
  container   Vulnerability assessment for containers
  host        Vulnerability assessment for hosts

Flags:
  -h, --help   help for vulnerability

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

Use "lacework vulnerability [command] --help" for more information about a command.
```

---

## lacework vulnerability container

```
Request on-demand container vulnerability scans and show previous assessments
from published images.

**PREREQUISITE:** Your Lacework account should already be configured
with a Container Registry Integration of the container images you are
trying to scan or show.

To create a new integration use the following command:

    lacework container-registry create

If you prefer to configure the integration via the WebUI, log in to your account at:

    https://<ACCOUNT>.lacework.net

Then navigate to Settings > Integrations > Container Registry.

Usage:
  lacework vulnerability container [command]

Aliases:
  container, ctr

Available Commands:
  list-assessments List container vulnerability assessments (default last 24 hours)
  list-registries  List all container registries configured
  scan             Request an on-demand container vulnerability assessment
  show-assessment  Show results of a container vulnerability assessment

Flags:
  -h, --help   help for container

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

Use "lacework vulnerability container [command] --help" for more information about a command.
```

---

## lacework vulnerability host

```
Request on-demand host vulnerability scans and show previous assessments
from hosts with the Lacework datacollector agent installed.

Usage:
  lacework vulnerability host [command]

Available Commands:
  generate-pkg-manifest Generates a package-manifest from the local host
  list-cves             List the CVEs found in the hosts in your environment
  list-hosts            List the hosts that contain a specified CVE ID in your environment
  scan-pkg-manifest     Request an on-demand host vulnerability assessment from a package-manifest
  show-assessment       Show results of a host vulnerability assessment

Flags:
  -h, --help   help for host

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

Use "lacework vulnerability host [command] --help" for more information about a command.
```

---

## lacework vulnerability lacework

```
Container and host vulnerability assessments.

Usage:
  lacework vulnerability [command]

Aliases:
  vulnerability, vuln, vul

Available Commands:
  container   Vulnerability assessment for containers
  host        Vulnerability assessment for hosts

Flags:
  -h, --help   help for vulnerability

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

Use "lacework vulnerability [command] --help" for more information about a command.
```

---

## lacework vulnerability vulnerability,

```
Container and host vulnerability assessments.

Usage:
  lacework vulnerability [command]

Aliases:
  vulnerability, vuln, vul

Available Commands:
  container   Vulnerability assessment for containers
  host        Vulnerability assessment for hosts

Flags:
  -h, --help   help for vulnerability

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

Use "lacework vulnerability [command] --help" for more information about a command.
```

---

