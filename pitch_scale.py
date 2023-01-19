from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import argparse


def draw_scale(c: canvas, height: float, base_x: float, scale: float):
    leading = 1 * cm
    # circle mark on the upper scale
    c.circle(base_x + 4 * cm, height - leading, 0.1 * cm)
    i = 0
    while i * scale < height:
        t = 1 * cm
        x = i * scale
        z = height - leading - x
        c.line(base_x - t, z, base_x + t, z)
        i += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pitch", type=int)
    args = parser.parse_args()
    # Paper size (A4)
    width = 21.0 * cm
    height = 29.7 * cm

    c = canvas.Canvas("./pitch_scale.pdf")
    c.saveState()

    c.setAuthor("Kimikazu Kato")
    c.setTitle("Scale")

    for w in [width / 4, width / 2, width * 3 / 4]:
        c.line(w, 0, w, height)
    draw_scale(c, height, width / 4, args.pitch * cm)
    draw_scale(c, height, width * 3 / 4, args.pitch * cm)
    c.showPage()
    c.save()


if __name__ == "__main__":
    main()
