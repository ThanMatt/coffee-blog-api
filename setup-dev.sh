#!/bin/sh

set -e
set -x

D="docker"
DC="docker compose"
$DC down

# # :: Create network
# $D network create coffee-blog

# Spin up conatiners
$DC build --no-cache
$DC up -d

sleep 3

# Run migration and seeders
$DC exec api python manage.py migrate

# show logs
$DC logs -f
