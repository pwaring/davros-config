# Davros

## TLS certificates

First, ensure that you have removed any old certificate entries and private keys
from `dehydrated/certs`, otherwise you may experience problems when
switching between the LetsEncrypt staging and production servers (this is a
known issue with dehydrated).

```
# Change into dehydrated git repository
./dehydrated --cron --config ./path/to/server-config/dehydrated/config.sh
```
