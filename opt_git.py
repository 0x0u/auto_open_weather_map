import os
from git import Repo
from datetime import datetime, timedelta, timezone

path = os.getcwd()
repo = Repo(path)

add = repo.index.add("README.md")
jst = timezone(timedelta(hours=+9), "JST")
today = datetime.now(jst).strftime("%Y-%m-%d")
msg = "☀️ {}".format(today)
commit = repo.index.commit(msg)
repo.git.push("origin", "master")
