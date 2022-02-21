# Trii

![python]

<details>
<summary>Index</summary>

## Content table

- [Requirements](#Requirements)
  - [Dependencies](#Dependencies)
  - [Envs](#Envs)
    - [Local](#Envs---Local)
- [Run](#Run)
  - [Local](#Run---Local)

</details>

<br/>

## Requirements

> Python >= 3.9 

<br/>

### Dependencies

<details>
<summary> Modules </summary>

> [fastapi==0.74.1][fastapi] <br/>
> [pydantic==1.9.0][pydantic] <br/>

<br/>

</details><br/>

### Envs

### Envs - Local

<details>
<summary> envs </summary>

Envs for _Django_ - **./.envs/.django.local.env**

```bash
# General
# ------------------------------------------------------------------------------
USE_DOCKER # If runs with containers [ yes ]
IPYTHONDIR # Folder to save autofiles of IPython [ /app/.ipython ]
```

<br/>

Envs for _PostgreSQL_ - **./.envs/postgres.local.env**

```bash
POSTGRES_PASSWORD # Database password [ postgres_password ]
```

</details>

<br/>

## Run

### Run - Local

```bash
docker-compose -p project_name -f containers/local.yml up -d
```
<!-- badges -->
[python]: https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white

<!-- links -->
[fastapi]: https://fastapi.tiangolo.com/
[pydantic]: https://pydantic-docs.helpmanual.io/
