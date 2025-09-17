import torch
import numpy as np
from PIL import Image
from typing import Tuple

# Allowed MiDaS models that can be loaded via torch.hub
VALID_MODELS = ["DPT_Large", "DPT_Hybrid", "MiDaS_small"]


def load_midas(model_type: str = "DPT_Hybrid") -> Tuple[torch.nn.Module, object]:
    """
    Load a MiDaS depth estimation model from torch.hub.

    Args:
        model_type (str):
            The model type to load. Must be one of:
            - "DPT_Large": highest accuracy, slower
            - "DPT_Hybrid": good balance between speed and quality
            - "MiDaS_small": fastest, less accurate

    Returns:
        Tuple[torch.nn.Module, object]:
            - The loaded MiDaS model in evaluation mode
            - The corresponding image transform function
    """
    if model_type not in VALID_MODELS:
        raise ValueError(
            f"Invalid model_type '{model_type}'. "
            f"Valid options: {', '.join(VALID_MODELS)}"
        )

    # Load model from torch.hub
    midas = torch.hub.load("intel-isl/MiDaS", model_type)
    midas.eval()  # set model to evaluation mode

    # Load the corresponding input transformation
    transform_module = torch.hub.load("intel-isl/MiDaS", "transforms")
    if "DPT" in model_type:
        transform = transform_module.dpt_transform
    else:
        transform = transform_module.small_transform

    return midas, transform


def image_to_depthmap(img_path: str, model_type: str = "DPT_Hybrid") -> Image.Image:
    """
    Convert an RGB image into a normalized depth map using MiDaS.

    Args:
        img_path (str):
            Path to the input image.
        model_type (str, optional):
            Which MiDaS model to use.
            Options: "DPT_Large", "DPT_Hybrid", "MiDaS_small".
            Default is "DPT_Hybrid".

    Returns:
        PIL.Image.Image:
            A grayscale depth map normalized to [0, 255].
            White = close, black = far.
    """
    # Load the MiDaS model and preprocessing transform
    midas, transform = load_midas(model_type)

    # Open and convert the input image to RGB
    img = Image.open(img_path).convert("RGB")

    # Apply preprocessing: resize, normalize, convert to tensor
    inp = transform(img).unsqueeze(0)  # shape: (1, C, H, W)

    # Run inference without gradients for efficiency
    with torch.no_grad():
        prediction = midas(inp)              # raw depth prediction
        depth = prediction.squeeze().cpu().numpy()  # convert to numpy array

    # Normalize depth values to 0–255 range
    depth_min, depth_max = depth.min(), depth.max()
    depth_norm = (255 * (depth - depth_min) / (depth_max - depth_min)).astype(np.uint8)

    # Convert numpy array back to PIL Image
    depth_img = Image.fromarray(depth_norm)
    return depth_img
