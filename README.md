# SimplePythonLogger

logger = Logger("./logs")
# 1st parameter is log filename (Only in custom_log)
# All remaining parameters will be used as string separated by space between them.
# Example:
logger.custom_log("arguments.l", timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status, "\n\t", f"Args:{request.args}")
# Or
logger.log("Log this", "Log that", "Log all")
