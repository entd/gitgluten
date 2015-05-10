import os
import sys
import confparser
import server
import daemon
import daemon.pidfile as pidlockfile

DEFAULT_NAME="config.json"

pidfile = pidlockfile.TimeoutPIDLockFile("/var/run/gluten.pid")
with daemon.DaemonContext(pidfile=pidfile):
	main()

def main():
	configParser = confparser.ConfigParser(DEFAULT_NAME)
	config = configParser.main_config
	server.serve(config)

if __name__ == "__main__":
	main()
