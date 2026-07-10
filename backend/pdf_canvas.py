from reportlab.pdfgen import canvas
from reportlab.lib.colors import white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


_registered_fonts = {}


def register_font(font_name, font_path):

    if font_name not in _registered_fonts:

        pdfmetrics.registerFont(

            TTFont(

                font_name,

                font_path

            )

        )

        _registered_fonts[font_name] = True


def create_canvas(output_path, width, height):

    return canvas.Canvas(

        output_path,

        pagesize=(width, height)

    )