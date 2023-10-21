#!/bin/bash

PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/sbin

/usr/bin/apt-get update --quiet
/usr/bin/apt-get upgrade --simulate
