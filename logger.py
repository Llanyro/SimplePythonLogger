import os


class Logger:
    __logger_folder: str
    __logger_file_error: str = "errors.log"
    __logger_file_info: str = "info.log"
    __logger_file_log: str = "log.log"

    def __init__(self, logger_folder: str = "."):
        self.__logger_folder = logger_folder
        if os.path.exists(logger_folder) is False:
            os.mkdir(logger_folder)

    def custom_log(self, logger_file, *args, **kwargs) -> bool:
        resultado = True
        try:
            with open(logger_file, "a") as f:
                for i in args:
                    f.write(f"{i} ")
                f.write("\n")
                f.close()
        except FileNotFoundError:
            resultado = False
        return resultado

    def log(self, *args, **kwargs) -> bool:
        return self.custom_log(self.__logger_file_log, *args, **kwargs)

    def error(self, *args, **kwargs) -> bool:
        return self.custom_log(self.__logger_file_error, *args, **kwargs)

    def info(self, *args, **kwargs) -> bool:
        return self.custom_log(self.__logger_file_info, *args, **kwargs)

