import os
import re
import sys

body = os.environ['body']
body = body.split('\n')

jira = body[0]
jira=jira[:-1]


match = bool(re.match(r"^\[.*\]\(.*\)$", jira))

if not match:
  print("Jira ID format no right!")
  sys.exit(1)
