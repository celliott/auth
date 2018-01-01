# auth
Basic auth http endpoint backed by vault

## Requirements
* [Docker for Mac](https://www.docker.com/docker-mac)

## Usage
Build and run container

```
$ make push
```

Get auth

#### plaintext

```bash
$ curl https://${SERVICE}.${DOMAIN}
{
  "authenticated": true,
  "user": "<username>"
}
```

### Helm chart
NOTE depends on [nginx-ingress](https://github.com/kubernetes/charts/tree/master/stable/nginx-ingress), [external-dns](https://github.com/kubernetes/charts/tree/master/stable/external-dns), and [kube-lego](https://github.com/kubernetes/charts/tree/master/stable/kube-lego)

#### Deploy

```bash
$ make deploy
```

#### Delete

```bash
$ make delete
```
#### Vault setup
NOTE uses vault userpass for auth

```bash
$ vault auth-enable userpass
$ vault write auth/userpass/users/${VAULT_USER} \
  password=${VAULT_PASS} \
  policies=default
```
