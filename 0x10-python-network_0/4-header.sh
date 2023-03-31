#!/bin/bash
URL="$1"
HEADER="X-HolbertonSchool-User-Id: 98"
curl -sH "$HEADER" "$URL"
