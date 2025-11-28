# Lightweight no-LLM stub for Colab / low-RAM setups.
# We do NOT import llama_cpp or xllamacpp here.

from typing import Any, List

# public API expected by the rest of RuinedFooocus
llama_names: List[str] = []

def run_llama(prompt: str, *args: Any, **kwargs: Any) -> str:
    """
    Stub implementation that just returns the original prompt.

    All call sites that expect a rewritten prompt from a local LLM will
    simply get the original text back. This keeps the rest of the app
    working without any heavy LLM dependencies.
    """
    return prompt
