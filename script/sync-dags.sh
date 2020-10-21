#!/usr/bin/env bash

set -e

echo "running dags sync"

if [ ! -d /eyk/dags_repo ]; then
  git clone $DAGS_GIT_URL /eyk/dags_repo
fi


cd /eyk/dags_repo
git checkout master
git pull origin master
mkdir -p "$AIRFLOW_HOME/dags"
rsync -avu --delete --force "$1" "$AIRFLOW_HOME/dags"
echo "dags sync complete"
