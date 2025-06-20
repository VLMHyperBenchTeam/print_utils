"""print_utils.print_utils
~~~~~~~~~~~~~~~~~~~~~~~~~

Реализация вспомогательных функций для форматированного вывода
сообщений в консоль. Выделено в отдельный модуль, чтобы облегчить
поддержку и избежать избыточных импортов при инициализации пакета.
"""

__all__ = [
    "print_header",
    "print_section",
    "print_success",
    "print_error",
    "print_info",
    "print_result",
]


def _print_with_emoji(prefix: str, message: str) -> None:
    """Базовая функция вывода сообщения с префиксом-эмодзи."""
    print(f"{prefix} {message}")


def print_header() -> None:
    """Выводит красивый заголовок тестирования модели."""
    print("\n" + "=" * 70)
    print("🚀 ТЕСТИРОВАНИЕ МОДЕЛИ QWEN2.5-VL")
    print("=" * 70)


def print_section(title: str) -> None:
    """Выводит заголовок секции."""
    print(f"\n📋 {title}")
    print("-" * 50)


def print_success(message: str) -> None:
    """Выводит сообщение об успехе."""
    _print_with_emoji("✅", message)


def print_error(message: str) -> None:
    """Выводит сообщение об ошибке."""
    _print_with_emoji("❌", message)


def print_info(message: str) -> None:
    """Выводит информационное сообщение."""
    _print_with_emoji("ℹ️", message)


def print_result(answer: str) -> None:
    """Выводит результат работы модели."""
    print("\n📝 РЕЗУЛЬТАТ РАБОТЫ МОДЕЛИ:")
    print("=" * 60)
    print(answer)
    print("=" * 60) 