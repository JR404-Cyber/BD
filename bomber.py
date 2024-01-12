import os, sys
try:
    __import__("bomber").banner()
except Exception as e:
    exit(str(e))
