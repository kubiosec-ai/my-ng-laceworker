# `lacework generate k8s`

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
