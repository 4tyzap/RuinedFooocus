import random
from typing import Any, Tuple

# ===== Основная генерация промпта (One Button / OBP) =====

def build_dynamic_prompt(*args: Any, **kwargs: Any) -> str:
    """
    Лёгкая заглушка One Button Prompt.

    Все сложные штуки (superprompter, transformers, LLM) выключены.
    Строим простой промпт из доступных полей kwargs.
    """
    parts = []

    preset_prefix = kwargs.get("preset_prefix") or ""
    prefixprompt = kwargs.get("prefixprompt") or ""
    givensubject = (kwargs.get("givensubject") or "").strip()
    forcesubject = (kwargs.get("forcesubject") or "").strip()
    giventypeofimage = kwargs.get("giventypeofimage") or ""
    preset_suffix = kwargs.get("preset_suffix") or ""
    suffixprompt = kwargs.get("suffixprompt") or ""

    if preset_prefix:
        parts.append(preset_prefix)

    if prefixprompt:
        parts.append(prefixprompt)

    subject = givensubject or forcesubject
    if subject and subject.lower() != "all":
        parts.append(subject)

    if giventypeofimage:
        parts.append(giventypeofimage)

    if preset_suffix:
        parts.append(preset_suffix)

    if suffixprompt:
        parts.append(suffixprompt)

    text = ", ".join([p for p in parts if p])
    if not text:
        text = "beautiful detailed illustration"
    return text


# ===== Варианты под SDXL / base (тот же stub, но отдельные функции) =====

def build_dynamic_prompt_sdxl(*args: Any, **kwargs: Any) -> str:
    """
    Облегчённая версия для SDXL – та же логика, что и build_dynamic_prompt.
    """
    return build_dynamic_prompt(*args, **kwargs)


def build_dynamic_prompt_sdxl_base(*args: Any, **kwargs: Any) -> str:
    """
    Облегчённая версия для SDXL base – тоже просто прокси.
    """
    return build_dynamic_prompt(*args, **kwargs)


# ===== Негативный промпт =====

def build_dynamic_negative(*args: Any, **kwargs: Any) -> str:
    """
    Stub негативного промпта – возвращаем какой-то базовый набор.
    Можно при желании поправить под себя.
    """
    base_negative = kwargs.get("base_negative") or ""
    extra_negative = kwargs.get("extra_negative") or ""

    parts = []
    if base_negative:
        parts.append(base_negative)
    if extra_negative:
        parts.append(extra_negative)

    if not parts:
        parts = [
            "low quality, bad anatomy, blurry, distorted, extra limbs, text, watermark"
        ]

    return ", ".join(parts)


# ===== Уровень безумия (insanity) – просто возвращаем число =====

def get_insanity(*args: Any, **kwargs: Any) -> int:
    """
    Stub функции get_insanity – возвращаем санкционированный уровень безумия.
    Если в kwargs передали insanitylevel – используем его, иначе 5.
    """
    level = kwargs.get("insanitylevel", 5)
    try:
        return int(level)
    except Exception:
        return 5


# ===== Вариант промпта для вкладки Evolve =====

def createpromptvariant(prompt: str, *args: Any, **kwargs: Any) -> str:
    """
    Простая "вариация" промпта для вкладки Evolve:
    слегка перемешиваем слова, без моделей.
    """
    words = prompt.split()
    if len(words) > 4:
        random.shuffle(words)
    return " ".join(words)
