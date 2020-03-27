import os
import random
from git import Repo
from datetime import datetime, timedelta, timezone

emoji = ["☀️", "❄️", "☁️", "⚡️", "☔️"]

path = os.getcwd()
repo = Repo(path)

add = repo.index.add("README.md")
jst = timezone(timedelta(hours=+9), "JST")
today = datetime.now(jst).strftime("%Y-%m-%d")
num = random.randint(0, 4)
msg = "{} {} {}".format(emoji[num], today, emoji[num])
commit = repo.index.commit(msg)
repo.git.push("origin", "master")

