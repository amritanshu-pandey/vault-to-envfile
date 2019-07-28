Drone Plugin - vault-to-env
===========================

Create a `vault.env` file from the secrets exported from Vault.
The generated file contain the secrets as key=value pairs.

for example:

```bash
DOCKER_USER=amritanshu
DOCKER_PASSWORD=blah
```


# How to use this plugin

In the `drone.yml` file add the following job as the first step in pipeline:

```yaml
- name: <job_name>
  image: amritanshu16/vault-to-env
  settings:
    vault_addr: <vault_http_or_https_address>
    vault_token:
    from_secret: <vault_token>
    vault_secret_path: <vault secret path e.g. 'drone/data/ci'>
```

At the end of this job, a file named `vault.env` will be created at the root
of the workspace. The file will contain the secrets exported from the given
vault path. The vault token used must have `list` and `read` permissions
for the path.

If `env` file is to be created at a different location, it could be specified
using the follwogin setting: `vault_env_file: /path/to/dot.env`

# How to use the output `env` file
This file can be used in follwogin ways:

1. Given as input to the docker build command:
    
    ```bash
    docker run --env-file=vault.env <image> <command>
    ```

    Similar command exist for using the `env` file in `docker-compose` file.

2. Use in *nix shell:

    ```bash
    . ./vault.env && echo ${DOCKER_USER}
    ```
