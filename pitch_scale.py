from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def draw_scale(c :canvas, height:float, base_x :float):
    leading = 1 * cm
    scale=2*cm
    for i in range(20):
        t = 1*cm
        x = i*scale
        z = height-leading-x
        c.line(base_x-t, z, base_x+t, z)
        

def main():
    # Paper size (A4)
    width = 21.0 * cm
    height = 29.7 * cm

    c = canvas.Canvas("./pitch_scale.pdf")
    c.saveState()

    c.setAuthor("Kimikazu Kato")
    c.setTitle("Test")

    for w in [width / 4, width / 2, width * 3 / 4]:
        c.line(w, 0, w, height)
    draw_scale(c, height, width / 4)
    draw_scale(c, height, width * 3 / 4)
    c.showPage()
    c.save()

if __name__ == "__main__":
    main()
