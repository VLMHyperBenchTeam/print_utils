"""Пакет `print_utils`.

В инициализаторе пакета экспортируем высокоуровневые функции из
модуля :pymod:`.print_utils` для удобства внешних импортов::

    from print_utils import print_info, print_success
"""

# Перенаправляем импорты на внутренний модуль
from .print_utils import (  # noqa: F401
    print_error,
    print_header,
    print_info,
    print_result,
    print_section,
    print_success,
)

__all__ = [
    "print_header",
    "print_section",
    "print_success",
    "print_error",
    "print_info",
    "print_result",
] 