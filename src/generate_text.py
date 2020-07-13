#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont


def generate_text():
    print("Generating Image")

    text = "Hello World"
    page_size = (800, 600)

    image = create_image(page_size)
    font = create_font(text)
    origin = find_centered_origin(text, font, page_size)
    draw_text(text, image, font, origin)
    image.save("output.png")


def create_image(page_size: (int, int)):
    image_mode = "RGB"
    image_size = page_size
    image_color = (255, 255, 255)
    return Image.new(image_mode, image_size, image_color)


def create_font(text: str):
    font_size = 128
    font = ImageFont.truetype("Sophia.ttf", font_size)
    return font


def draw_text(text: str, image: Image, font: ImageFont, origin: (int, int)):
    draw = ImageDraw.Draw(image)
    text_color = (0, 0, 0)
    draw.text(origin, text, fill=text_color, font=font)


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
