class Digital:
    def __init__(self, file_format, file_size):
        self._file_format = file_format
        self._file_size = file_size

    @property
    def file_format(self):
        return self._file_format

    @file_format.setter
    def file_format(self, value):
        allowed_formats = ["PDF", "EPUB", "MOBI", "AZW3"]
        if value.upper() not in allowed_formats:
            raise ValueError(
                f"Невірний формат файлу. Дозволені: {allowed_formats}")
        self._file_format = value.upper()

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        if value <= 0:
            raise ValueError("Розмір файлу повинен бути більший за 0 МБ")
        self._file_size = value

    def display_info(self):
        return f"Цифровий формат: {self._file_format}, Розмір файлу: {self._file_size} МБ"
