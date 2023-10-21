#!/bin/bash

set -u
set -e

/usr/bin/certbot renew

# Reload all services which rely on TLS, otherwise they will not pick up any
# new certificates
/usr/sbin/service apache2 reload
/usr/sbin/service dovecot reload
/usr/sbin/service postfix reload
