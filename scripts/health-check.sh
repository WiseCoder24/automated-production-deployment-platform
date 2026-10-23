#!/usr/bin/env bash

set -u

URL="http://localhost:8081/health"

if curl --fail --silent --show-error --max-time 5 "$URL"; then
    echo
    echo "HEALTH CHECK PASSED"
    exit 0
else
    echo
    echo "HEALTH CHECK FAILED: $URL"
    exit 1
fi
