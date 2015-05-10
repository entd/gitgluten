import sys
import os
import json


class ConfigParser(object):
	def __init__(self, name="config.json"):
		print("Loading config {}".format(name))
		self._name = name
		self.main_config = ConfigParser.generate_config(self._name)

	@classmethod
	def generate_config(cls, filename):
		with open(filename) as f:
			text = f.read()
			#Save our souls from parsing error
			raw_config = json.loads(text)
			port = raw_config["port"]
			module = raw_config["module"]
			raw_repos = raw_config["repos"]
			repos = []
			for raw_repo in raw_repos:
				branch = raw_repo["branch"]
				address = raw_repo["address"]
				hook = raw_repo["hook"]
				repo = RepoConfig(branch, address, hook)
				repos.append(repo)
			return Config(port, repos, module)


class Config(object):
	def __init__(self, port, repos, module):
		self._port = port
		self._repos = repos
		self._module = module

	def get_repo(self):
		for repo in repos:
			yield repo

class RepoConfig(object):
	def __init__(self, branch, address, hook):
		self._branch = branch
		self._address = address
		self._hook = hook
