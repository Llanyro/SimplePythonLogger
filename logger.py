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
    def custom_log(self, logger_file: str, *args, **kwargs) -> int:
        """
            Returns:
                0: All ok
                1: args.__len__() == 0 (No args)
                2: FileNotFoundError
        """
        resultado: int = 0
        if args.__len__() > 0:
            try:
                with open(self.__logger_folder.format(logger_file), "a") as f:
                    f.write(args[0])
                    for argument in args[1:]:
                        f.write(' ')
                        f.write(argument)
                    f.write("\n")
                    f.close()
            except FileNotFoundError:
                resultado = 2
        else:
            resultado = 1
        return resultado

    def log(self, *args, **kwargs) -> int:
        return self.custom_log(self.__logger_file_log, *args, *kwargs)

    def error(self, *args, **kwargs) -> int:
        return self.custom_log(self.__logger_file_error, *args, *kwargs)

    def info(self, *args, **kwargs) -> int:
        return self.custom_log(self.__logger_file_info, *args, *kwargs)

    # endregion
    # region Time Logs
    def custom_log_time(self, logger_file: str, *args, **kwargs) -> int:
        """
            Returns:
                0: All ok
                1: args.__len__() == 0 (No args)
                2: FileNotFoundError
        """
        resultado: int = 0
        if args.__len__() > 0:
            try:
                timestamp = strftime('[%Y-%b-%d %H:%M]')
                with open(self.__logger_folder.format(logger_file), "a") as f:
                    f.write(f"{timestamp} ")
                    f.write(args[0])
                    for argument in args[1:]:
                        f.write(' ')
                        f.write(argument)
                    f.write("\n")
                    f.close()
            except FileNotFoundError:
                resultado = 2
        else:
            resultado = 1
        return resultado

    def log_time(self, *args, **kwargs) -> int:
        return self.custom_log_time(self.__logger_file_log, *args, *kwargs)

    def error_time(self, *args, **kwargs) -> int:
        return self.custom_log_time(self.__logger_file_error, *args, *kwargs)

    def info_time(self, *args, **kwargs) -> int:
        return self.custom_log_time(self.__logger_file_info, *args, *kwargs)
    # endregion
