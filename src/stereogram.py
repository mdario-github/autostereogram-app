import numpy as np
from PIL import Image
from typing import Union


def generate_autostereogram(
    depth_map: Union[Image.Image, np.ndarray],
    eye_separation: int = 15
) -> Image.Image:
    """
    Generate an autostereogram from a depth map.

    Args:
        depth_map (Union[Image.Image, np.ndarray]):
            The input depth map in grayscale (0 = far, 255 = close).
            Can be a PIL.Image or a numpy array.
        eye_separation (int, optional):
            Maximum horizontal pixel shift to create the 3D effect.
            Default is 15.

    Returns:
        Image.Image: The generated autostereogram as a grayscale image.
    """
    # Convert depth map to numpy array if it's a PIL image
    if isinstance(depth_map, Image.Image):
        depth_map = np.array(depth_map.convert("L"))

    # Basic input validation
    if depth_map.ndim != 2:
        raise ValueError("Depth map must be a 2D grayscale image.")
    if eye_separation <= 0:
        raise ValueError("eye_separation must be a positive integer.")

    h, w = depth_map.shape

    # Start with random noise pattern for the stereogram
    stereogram = np.random.randint(0, 255, (h, w), dtype=np.uint8)

    # Shift pixels horizontally based on depth map values
    for y in range(h):
        for x in range(eye_separation, w):
            shift = int((depth_map[y, x] / 255) * eye_separation)
            stereogram[y, x] = stereogram[y, x - shift]

    return Image.fromarray(stereogram)
