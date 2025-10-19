from colorama import Fore

from src.models import LogColors


def test_log_colors_match_colorama_palette() -> None:
    assert LogColors.ERROR.value == Fore.LIGHTRED_EX
    assert LogColors.INFO.value == Fore.LIGHTBLUE_EX
    assert LogColors.SUCCESS.value == Fore.LIGHTGREEN_EX
    assert LogColors.WARNING.value == Fore.LIGHTYELLOW_EX
    assert LogColors.FATAL.value == Fore.LIGHTMAGENTA_EX
    assert LogColors.RESET.value == Fore.RESET
