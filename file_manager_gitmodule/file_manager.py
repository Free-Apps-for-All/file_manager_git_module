import os
from typing import Literal

ReadingMode = Literal['r', 'rb']  # no rb+
WritingMode = Literal['w', 'wb']  # no wb+
AppendingMode = Literal['a', 'ab']
Encoding = Literal['utf-8', None]  # adjust according to your needs


class FileManager:
    """ Utility to standard manage file operations with ease. """

    @staticmethod
    def read_file(fp: str, mode: ReadingMode) -> bytes | str | None:
        """
        Reads a file according to mode.

        Usage example:
            if file_content := read_file(fp, mode) is not None: ...

        Returns bytes, string, or None (if the file wasn't found).
        """
        if os.path.isfile(fp):
            with open(fp, mode) as file:
                return file.read()
        else:
            return None

    @staticmethod
    def write_file(fp: str, data: bytes | str, mode: WritingMode, encoding: Encoding = None) -> None:
        """
        Writes data to a file.
        Remember, in binary mode encoding should be None.

        Returns None, as anyways a new file will be created.
        """
        with open(fp, mode, encoding) as encrypted_file:
            encrypted_file.write(data)

    @staticmethod
    def delete_file(fp: str) -> bool:
        """
        Deletes the file
        Returns bool depending on if the file was found or not.
        """
        if os.path.isfile(fp):
            os.remove(fp)
            return True
        return False

    @classmethod
    def append_to_file(cls, fp: str, content: bytes | str, mode: AppendingMode) -> bool:
        """
        Appends content to file
        Returns bool depending on if the file was found or not.
        """
        if os.path.isfile(fp):
            with open(fp, mode) as file:
                file.write(content)
                return True
        return False
