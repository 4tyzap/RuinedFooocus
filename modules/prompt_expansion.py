from typing import Any, Dict, Tuple

class PromptExpansion:
    """
    Лёгкая заглушка Prompt Expansion для Colab.

    Оригинальный модуль использует transformers + ComfyUI ModelPatcher,
    что тянет за собой кучу тяжёлых зависимостей и ломается в Colab.
    В этой версии мы НИЧЕГО не генерируем, просто возвращаем исходный текст.
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        # Сохраняем интерфейс, похожий на ComfyUI-узел, чтобы
        # любые обращения к INPUT_TYPES не падали.
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFF}),
                "log_prompt": (["No", "Yes"], {"default": "No"}),
            },
        }

    # Эти поля могут использоваться где-то в коде, оставляем их.
    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("final_prompt", "seed")
    FUNCTION = "expand_prompt"
    CATEGORY = "utils"

    @staticmethod
    def expand_prompt(
        text: str,
        seed: int,
        log_prompt: str = "No",
    ) -> Tuple[str, int]:
        """
        Stub: просто возвращаем текст как есть и seed без изменений.
        """
        try:
            seed = int(seed)
        except Exception:
            seed = 0

        # Можно при желании сделать сюда принт, но лучше молча.
        return text, seed

    # На всякий случай, если кто-то будет вызывать экземпляр как функцию.
    def __call__(self, text: str, seed: int, log_prompt: str = "No"):
        return self.expand_prompt(text, seed, log_prompt)
