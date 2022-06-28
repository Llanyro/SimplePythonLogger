# SimplePythonLogger

# Use exmaple
```
logger = Logger("./logs")
# 1st parameter is log filename (Only in custom_log)
# All remaining parameters will be used as string separated by space between them.
# Example 1:
logger.custom_log("arguments.log", "Log this", "Log that", "\n\t", "Log everything")
# Example 2:
logger.log("Log this", "Log that", "Log all")
# Example 3:
logger.custom_log_time("custom_log_time_name.log", "Log this", "Log that", "\n\t", "Log everything")
```
