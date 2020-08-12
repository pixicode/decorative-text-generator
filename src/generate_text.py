#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import sys


def generate_text():

    if len(sys.argv) != 2:
        print("Requires exactly one argument for the text to generate.")
        exit(1)

    text = sys.argv[1]

    if len(text) < 2:
        print("Text length must be at least 2 characters.")
        exit(1)

    print("Generating Image")
    page_size = (800, 240)
    font_size = 128

    image = create_image(page_size)
    font = ImageFont.truetype("Sophia.ttf", font_size)
    left_font = ImageFont.truetype("SophiaLeft.ttf", font_size)
    right_font = ImageFont.truetype("SophiaRight.ttf", font_size)

    x, y = find_centered_origin(text, font, page_size)

    first_letter = text[0]
    middle_text = text[1:-1]
    last_letter = text[-1]

    middle_text_x = x + font.getsize(first_letter)[0]
    last_letter_x = middle_text_x + font.getsize(middle_text)[0]

    draw_text(first_letter, image, left_font, x, y)
    draw_text(middle_text, image, font, middle_text_x, y)
    draw_text(last_letter, image, right_font, last_letter_x, y)

    image.save("output.png")


def create_image(page_size: (int, int)):
    image_mode = "RGB"
    image_size = page_size
    image_color = (255, 255, 255)
    return Image.new(image_mode, image_size, image_color)

def draw_text(text: str, image: Image, font: ImageFont, x: int, y: int):
    draw = ImageDraw.Draw(image)
    text_color = (0, 0, 0)
    draw.text((x, y), text, fill=text_color, font=font)


def find_centered_origin(text: str, font: ImageFont, page_size: (int, int)):
    text_width, text_height = font.getsize(text)
    page_width, page_height = page_size

    width_delta = page_width - text_width
    height_delta = page_height - text_height

    origin_x = width_delta // 2
    origin_y = height_delta // 2

    return (origin_x, origin_y)


if __name__ == "__main__":
    generate_text()
