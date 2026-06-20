"""
Generate moody black & white placeholder frames (grain + vignette + soft gradients)
so the gallery renders like a real film portfolio before real scans are added.
"""
import numpy as np
from PIL import Image, ImageFilter
import os

OUT = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(OUT, exist_ok=True)

rng = np.random.default_rng(7)

# (filename, width, height, base_low, base_high, direction)
# direction: 'v' vertical, 'h' horizontal, 'd' diagonal, 'r' radial-light
frames = [
    ("frame-01.jpg", 1500, 1000, 18, 120, "d"),
    ("frame-02.jpg", 1000, 1500, 30, 200, "v"),
    ("frame-03.jpg", 1200, 1200, 10, 90, "r"),
    ("frame-04.jpg", 1500, 1000, 40, 175, "h"),
    ("frame-05.jpg", 1000, 1500, 12, 110, "d"),
    ("frame-06.jpg", 1500, 1000, 60, 210, "v"),
    ("frame-07.jpg", 1200, 1200, 22, 140, "r"),
    ("frame-08.jpg", 1000, 1500, 8, 95, "h"),
    ("frame-09.jpg", 1500, 1000, 35, 160, "d"),
    ("frame-10.jpg", 1200, 1200, 50, 190, "v"),
    ("frame-11.jpg", 1000, 1500, 14, 130, "r"),
    ("frame-12.jpg", 1500, 1000, 28, 150, "h"),
]

def gradient(w, h, lo, hi, direction):
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    if direction == "v":
        g = yy / max(h - 1, 1)
    elif direction == "h":
        g = xx / max(w - 1, 1)
    elif direction == "d":
        g = (xx / max(w - 1, 1) + yy / max(h - 1, 1)) / 2.0
    else:  # radial light pool
        cx, cy = w * (0.4 + 0.2 * rng.random()), h * (0.35 + 0.2 * rng.random())
        d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
        g = 1.0 - (d / d.max())
    return lo + (hi - lo) * g

def vignette(w, h, strength=0.55):
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    cx, cy = w / 2.0, h / 2.0
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    d = d / d.max()
    return 1.0 - strength * (d ** 2.2)

for name, w, h, lo, hi, direction in frames:
    base = gradient(w, h, lo, hi, direction)
    # add a couple of soft tonal blobs for depth
    for _ in range(3):
        bx, by = rng.integers(0, w), rng.integers(0, h)
        br = rng.integers(min(w, h) // 4, min(w, h) // 2)
        amp = rng.uniform(-35, 45)
        yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
        dd = np.sqrt((xx - bx) ** 2 + (yy - by) ** 2)
        base += amp * np.clip(1 - dd / br, 0, 1) ** 2
    base *= vignette(w, h, strength=rng.uniform(0.45, 0.65))
    # film grain
    grain = rng.normal(0, 11, size=(h, w)).astype(np.float32)
    img = np.clip(base + grain, 0, 255).astype(np.uint8)
    im = Image.fromarray(img, mode="L").convert("RGB")
    # tiny blur so grain reads as film, not digital salt
    im = im.filter(ImageFilter.GaussianBlur(0.4))
    im.save(os.path.join(OUT, name), quality=84, optimize=True)
    print("wrote", name, f"{w}x{h}")

print("done")
