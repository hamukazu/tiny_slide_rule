from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
import numpy as np


def font_height(face, fontsize):
    ascent = (face.ascent * fontsize) / 1000.0
    descent = (face.descent * fontsize) / 1000.0
    return ascent - descent


def tick_label(c: canvas, x: float, y: float, offset: float, label: str):
    c.saveState()
    c.translate(x, y)
    c.rotate(-90)
    c.drawCentredString(0, offset, label)
    c.restoreState()


def tick(
    c: canvas,
    text_height: float,
    x: float,
    y: float,
    tick_size: float,
    tick_dir: int,
    label: str,
):
    c.line(x, y, x + tick_size * tick_dir, y)
    if tick_dir > 0:
        offset = 0.2 * cm
    else:
        offset = -text_height - 0.2 * cm
    if label:
        tick_label(c, x + tick_size * tick_dir, y, offset, label)


def draw_scale(c: canvas, height: float, base_x: float, flip: bool):
    fontname = "Helvetica"
    face = pdfmetrics.getFont(fontname).face
    fontsize = 10
    c.setFont(fontname, fontsize)
    text_height = font_height(face, fontsize)
    leading = 1 * cm
    scale = 14 * cm
    for i in range(3):
        t = 1 * cm
        x = i * scale
        y = leading + x
        z = height - leading - x
        if not flip:
            y = z
        label = str(10 ** i)
        tick(c, text_height, base_x, y, t, 1, label)
        tick(c, text_height, base_x, z, t, -1, label)
    fontsize = 9
    c.setFont(fontname, fontsize)
    text_height = font_height(face, fontsize)
    for i in range(2, 10):
        t = 0.7 * cm
        x = np.log10(i) * scale
        y = leading + x
        z = height - leading - x
        if not flip:
            y = z
        label = str(i)
        tick(c, text_height, base_x, y, t, 1, label)
        tick(c, text_height, base_x, z, t, -1, label)
        x = np.log10(i * 10) * scale
        y = leading + x
        z = height - leading - x
        if not flip:
            y = z
        label = str(i * 10)
        tick(c, text_height, base_x, y, t, 1, label)
        tick(c, text_height, base_x, z, t, -1, label)
    fontsize = 7
    c.setFont(fontname, fontsize)
    text_height = font_height(face, fontsize)
    for i in range(11, 100):
        if i % 10 != 0:
            if i % 5 == 0:
                t = 0.4 * cm
                label = str(i)
            else:
                t = 0.3 * cm
                label = None
            x = np.log10(i) * scale
            y = leading + x
            z = height - leading - x
            if not flip:
                y = z
            tick(c, text_height, base_x, y, t, 1, label)
            tick(c, text_height, base_x, z, t, -1, label)
            if i % 5 == 0:
                t = 0.4 * cm
                label = str(i * 0.1)
            else:
                t = 0.3 * cm
                label = None
            x = np.log10(i * 0.1) * scale
            y = leading + x
            z = height - leading - x
            if not flip:
                y = z
            tick(c, text_height, base_x, y, t, 1, label)
            tick(c, text_height, base_x, z, t, -1, label)


def main():
    # Paper size (A4)
    width = 21.0 * cm
    height = 29.7 * cm

    c = canvas.Canvas("./tiny_slide_scale.pdf")
    c.saveState()

    c.setAuthor("Kimikazu Kato")
    c.setTitle("Test")

    for w in [width / 4, width / 2, width * 3 / 4]:
        c.line(w, 0, w, height)
    draw_scale(c, height, width / 4, False)
    draw_scale(c, height, width * 3 / 4, False)
    c.showPage()
    c.save()


if __name__ == "__main__":
    main()
