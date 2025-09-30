"""
Monkey patch for integrating ADetailer into RuinedFooocus. This module patches the process function from modules.sdxl_pipeline so that after the original image generation, ADetailer can optionally refine the results if the `use_adetailer` flag is enabled in settings or in the gen_data dictionary. This patch is loaded by importing modules.adetailer_patch in settings.py.
"""
from modules import settings
from modules import sdxl_pipeline
import numpy as np

try:
    import adetailer
except Exception:
    adetailer = None

# Save reference to original process
_original_process = sdxl_pipeline.process


def patched_process(*args, **kwargs):
    """Wrapper for sdxl_pipeline.process that applies ADetailer if enabled."""
    # Call original sdxl pipeline process to generate images (list of numpy arrays)
    images = _original_process(*args, **kwargs)
    # Determine whether to use ADetailer
    use_flag = False
    gen_data = None
    if args:
        gen_data = args[0]
    # Check if gen_data is a dict or object with use_adetailer flag
    try:
        if isinstance(gen_data, dict) and gen_data.get("use_adetailer") is not None:
            use_flag = bool(gen_data.get("use_adetailer"))
        elif hasattr(gen_data, "use_adetailer"):
            use_flag = bool(getattr(gen_data, "use_adetailer"))
    except Exception:
        pass
    # Fall back to global settings
    if not use_flag:
        try:
            use_flag = settings.get_setting("use_adetailer")
        except Exception:
            use_flag = False
    # If enabled and adetailer available, process each image
    if use_flag and adetailer is not None:
        processed = []
        for img in images:
            try:
                from PIL import Image
                pil_img = Image.fromarray(img)
                result = pil_img
                # Attempt various functions to run adetailer
                try:
                    if hasattr(adetailer, "run"):
                        result = adetailer.run(pil_img)
                    elif hasattr(adetailer, "process"):
                        result = adetailer.process(pil_img)
                    else:
                        from adetailer import scripts  # type: ignore
                        if hasattr(scripts, "ladetailer"):
                            result = scripts.ladetailer.process(pil_img)  # type: ignore
                except Exception:
                    result = pil_img
                processed.append(np.array(result))
            except Exception as e:
                print("ADetailer processing error:", e)
                processed.append(img)
        images = processed
    return images

# Apply patch
sdxl_pipeline.process = patched_process
print("ADetailer patch loaded: sdxl_pipeline.process has been patched.")
