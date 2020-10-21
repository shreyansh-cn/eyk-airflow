from subprocess import call
from time import sleep
from os import environ, path

dags_git_path = environ.get("DAGS_GIT_PATH", ".")
if not dags_git_path.startswith("."):
  dags_git_path = "." + dags_git_path

dags_git_path = path.abspath(path.join("/eyk/dags_repo", dags_git_path)) + "/"

while True:
  if "DAGS_GIT_URL" not in environ:
    break
  call(["/bin/bash", "/eyk/sync-dags.sh", dags_git_path])
  sleep(60)
