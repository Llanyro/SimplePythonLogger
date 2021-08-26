# SimplePythonLogger

# Use exmaple
```
logger = Logger("./logs")
# 1st parameter is log filename (Only in custom_log)
# All remaining parameters will be used as string separated by space between them.
# Example 1:
logger.custom_log("arguments.l", timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status, "\n\t", f"Args:{request.args}")
# Example 2:
logger.log("Log this", "Log that", "Log all")
```
