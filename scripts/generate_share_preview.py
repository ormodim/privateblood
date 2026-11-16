#!/usr/bin/env python3
"""Generate the Private Blood social-sharing image.

Install the dependency with:
    python3 -m pip install -r scripts/requirements.txt

Run from the repository root or any other directory with:
    python3 scripts/generate_share_preview.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "share-preview.jpg"
SCALE = 2
WIDTH = 1200
HEIGHT = 630
GEORGIA = "/System/Library/Fonts/Supplemental/Georgia.ttf"
AVENIR_NEXT = "/System/Library/Fonts/Avenir Next.ttc"


def scaled_box(values: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return tuple(round(value * SCALE) for value in values)


def load_font(path: str, size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size * SCALE, index=index)


def draw_tube(
    image: Image.Image,
    cap: str,
    sample: str,
    angle: int,
    center: tuple[int, int],
) -> None:
    tube_image = Image.new("RGBA", (100 * SCALE, 320 * SCALE), (0, 0, 0, 0))
    tube_draw = ImageDraw.Draw(tube_image)
    body = scaled_box((18, 48, 82, 311))
    body_radius = 30 * SCALE

    tube_draw.rounded_rectangle(
        body, radius=body_radius, fill="#fffefa"
    )
    tube_draw.rectangle(scaled_box((21, 228, 79, 284)), fill=sample)
    tube_draw.ellipse(scaled_box((21, 270, 79, 307)), fill=sample)
    tube_draw.rounded_rectangle(
        scaled_box((10, 12, 90, 58)), radius=7 * SCALE, fill=cap
    )
    tube_draw.line(
        (22 * SCALE, 24 * SCALE, 78 * SCALE, 24 * SCALE),
        fill="#ffffff",
        width=2 * SCALE,
    )
    tube_draw.line(
        (31 * SCALE, 82 * SCALE, 31 * SCALE, 207 * SCALE),
        fill="#ffffff",
        width=3 * SCALE,
    )
    tube_draw.rounded_rectangle(
        scaled_box((25, 144, 75, 178)),
        radius=3 * SCALE,
        fill="#f3f1ec",
    )
    tube_draw.line(
        (33 * SCALE, 155 * SCALE, 66 * SCALE, 155 * SCALE),
        fill="#b9c1bc",
        width=2 * SCALE,
    )
    tube_draw.rounded_rectangle(
        body,
        radius=body_radius,
        outline="#97a5a1",
        width=2 * SCALE,
    )

    rotated = tube_image.rotate(
        angle, resample=Image.Resampling.BICUBIC, expand=False
    )
    position = (
        round(center[0] * SCALE - rotated.width / 2),
        round(center[1] * SCALE - rotated.height / 2),
    )
    image.paste(rotated, position, rotated)


def draw_brand(draw: ImageDraw.ImageDraw) -> None:
    draw.ellipse(
        scaled_box((76, 57, 124, 105)),
        outline="#c9a9ad",
        width=2 * SCALE,
    )
    draw.polygon(
        [
            (100 * SCALE, 65 * SCALE),
            (91 * SCALE, 82 * SCALE),
            (91 * SCALE, 89 * SCALE),
            (96 * SCALE, 97 * SCALE),
            (104 * SCALE, 99 * SCALE),
            (111 * SCALE, 93 * SCALE),
            (111 * SCALE, 85 * SCALE),
        ],
        outline="#773c4a",
    )
    draw.line(
        (96 * SCALE, 88 * SCALE, 100 * SCALE, 93 * SCALE),
        fill="#773c4a",
        width=2 * SCALE,
    )
    draw.text(
        (140 * SCALE, 57 * SCALE),
        "PRIVATE BLOOD",
        font=load_font(AVENIR_NEXT, 23, index=2),
        fill="#24313a",
    )
    draw.text(
        (141 * SCALE, 88 * SCALE),
        "PHLEBOTOMY TRAINING",
        font=load_font(AVENIR_NEXT, 12, index=7),
        fill="#647078",
    )


def draw_illustration(draw: ImageDraw.ImageDraw, image: Image.Image) -> None:
    draw.rounded_rectangle(
        scaled_box((742, 38, 1150, 612)),
        radius=190 * SCALE,
        fill="#e9e7df",
    )
    draw.ellipse(
        scaled_box((780, 124, 1112, 456)),
        outline="#c9a9ad",
        width=2 * SCALE,
    )
    draw.ellipse(
        scaled_box((814, 158, 1078, 422)),
        fill="#ead9d8",
    )

    draw_tube(image, "#d9b5b7", "#773c4a", 9, (838, 326))
    draw_tube(image, "#758a82", "#a76b53", 0, (946, 306))
    draw_tube(image, "#c7a86f", "#c5a96f", -9, (1054, 326))


def draw_copy(draw: ImageDraw.ImageDraw) -> None:
    draw.line(
        (78 * SCALE, 160 * SCALE, 105 * SCALE, 160 * SCALE),
        fill="#773c4a",
        width=2 * SCALE,
    )
    draw.text(
        (118 * SCALE, 148 * SCALE),
        "PRACTICAL PHLEBOTOMY TRAINING",
        font=load_font(AVENIR_NEXT, 14, index=5),
        fill="#773c4a",
    )

    headline = load_font(GEORGIA, 61)
    draw.text((77 * SCALE, 190 * SCALE), "Hands-on", font=headline, fill="#24313a")
    draw.text(
        (77 * SCALE, 259 * SCALE),
        "phlebotomy",
        font=headline,
        fill="#773c4a",
    )
    draw.text(
        (77 * SCALE, 328 * SCALE),
        "practice.",
        font=headline,
        fill="#24313a",
    )

    body = load_font(AVENIR_NEXT, 20, index=7)
    draw.text(
        (80 * SCALE, 428 * SCALE),
        "Finished your theory course?",
        font=body,
        fill="#536069",
    )
    draw.text(
        (80 * SCALE, 464 * SCALE),
        "Help shape a hands-on workshop for your first role.",
        font=load_font(AVENIR_NEXT, 17, index=7),
        fill="#536069",
    )

    draw.rounded_rectangle(
        scaled_box((80, 532, 88, 573)),
        radius=3 * SCALE,
        fill="#773c4a",
    )
    draw.text(
        (105 * SCALE, 541 * SCALE),
        "WORKSHOP IN DEVELOPMENT",
        font=load_font(AVENIR_NEXT, 14, index=5),
        fill="#5d2f3b",
    )


def create_preview() -> None:
    image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), "#f7f4ef")
    draw = ImageDraw.Draw(image)

    draw_illustration(draw, image)
    draw_brand(draw)
    draw_copy(draw)

    image = image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    image.save(OUTPUT, format="JPEG", quality=92, optimize=True, progressive=True)
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    create_preview()
