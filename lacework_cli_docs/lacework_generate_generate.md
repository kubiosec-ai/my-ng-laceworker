# `lacework generate generate`

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
