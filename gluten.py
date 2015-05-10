import os
import sys
import confparser
import server

DEFAULT_NAME="config.json"


if __name__ == "__main__":
    configParser = confparser.ConfigParser(DEFAULT_NAME)
    config = configParser.main_config
    server.serve(config)
