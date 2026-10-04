#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/../apps/api"
poetry run alembic upgrade head
