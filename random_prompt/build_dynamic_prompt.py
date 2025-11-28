import random
from typing import Any

def build_dynamic_prompt(
    insanitylevel: int = 5,
    forcesubject: str = "all",
    artists: str = "all",
    imagetype: str = "all",
    onlyartists: bool = False,
    antivalues: str = "",
    prefixprompt: str = "",
    suffixprompt: str = "",
    promptcompounderlevel: str = "1",
    seperator: str = "comma",
    givensubject: str = "",
    smartsubject: bool = True,
    giventypeofimage: str = "",
    imagemodechance: int = 20,
    gender: str = "all",
    subtypeobject: str = "all",
    subtypehumanoid: str = "all",
    subtypeconcept: str = "all",
    advancedprompting: bool = True,
    hardturnoffemojis: bool = False,
    seed: int = -1,
    overrideoutfit: str = "",
    prompt_g_and_l: bool = False,
    base_model: str = "SD1.5",
    OBP_preset: str = "",
    prompt_enhancer: str = "none",
    subtypeanimal: str = "all",
    subtypelocation: str = "all",
    preset_prefix: str = "",
    preset_suffix: str = "",
) -> str:
    """
    Лёгкая заглушка OneButton random prompt.

    Никаких superprompter / transformers / T5.
    Просто собираем текст из доступных полей.
    """
    parts = []

    if preset_prefix:
        parts.append(preset_prefix)

    if prefixprompt:
        parts.append(prefixprompt)

    # берём либо заданный subject, либо forcesubject (если он не 'all')
    subject = (givensubject or "").strip() or (forcesubject or "").strip()
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
        # запасной вариант – какой-то базовый осмысленный промпт
        text = "beautiful detailed illustration"

    return text


def createpromptvariant(prompt: str, *args: Any, **kwargs: Any) -> str:
    """
    Простая "вариация" промпта для вкладки Evolve:
    чуть-чуть перемешиваем слова, без моделей.
    """
    words = prompt.split()
    if len(words) > 4:
        random.shuffle(words)
    return " ".join(words)
