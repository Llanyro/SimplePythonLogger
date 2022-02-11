import os
from time import strftime


class Logger:
    __logger_folder: str
    __logger_file_error: str = "errors.log"
    __logger_file_info: str = "info.log"
    __logger_file_log: str = "log.log"

    def __init__(self, logger_folder: str = "."):
        self.__logger_folder = logger_folder + "/{0}"
        if os.path.exists(logger_folder) is False:
            os.mkdir(logger_folder)

    # region Simple Logs
    def custom_log(self, logger_file, *args, **kwargs) -> bool:
        resultado = True
        try:
            with open(self.__logger_folder.format(logger_file), "a") as f:
                for i in args:
                    f.write(i)
                    f.write(' ')
                f.write("\n")
                f.close()
        except FileNotFoundError:
            resultado = False
        return resultado

    def log(self, *args, **kwargs) -> bool:
        return self.custom_log(self.__logger_file_log, *args, *kwargs)

    def error(self, *args, **kwargs) -> bool:
        return self.custom_log(self.__logger_file_error, *args, *kwargs)

    def info(self, *args, **kwargs) -> bool:
        return self.custom_log(self.__logger_file_info, *args, *kwargs)

    # endregion
    # region Time Logs
    def custom_log_time(self, logger_file, *args, **kwargs) -> bool:
        resultado = True
        try:
            timestamp = strftime('[%Y-%b-%d %H:%M]')
            with open(self.__logger_folder.format(logger_file), "a") as f:
                f.write(f"{timestamp} ")
                for i in args:
                    f.write(i)
                    f.write(' ')
                f.write("\n")
                f.close()
        except FileNotFoundError:
            resultado = False
        return resultado

    def log_time(self, *args, **kwargs) -> bool:
        return self.custom_log_time(self.__logger_file_log, *args, *kwargs)

    def error_time(self, *args, **kwargs) -> bool:
        return self.custom_log_time(self.__logger_file_error, *args, *kwargs)

    def info_time(self, *args, **kwargs) -> bool:
        return self.custom_log_time(self.__logger_file_info, *args, *kwargs)
    # endregion
