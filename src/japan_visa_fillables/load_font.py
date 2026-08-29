from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def setup_fonts():
    """Registers Liberation Sans under the name 'Arial' for ReportLab."""
    font_path = Path(__file__).parent / "fonts" / "LiberationSans-Regular.ttf"
    
    # Avoid re-registering if the font is already registered
    if 'Arial' not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont('Arial', font_path))

setup_fonts()