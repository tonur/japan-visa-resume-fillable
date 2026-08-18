from . import load_font
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# Register Japanese font for header and Japanese title
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

def create_outline_activities(filename="Outline_of_Intended_Activities_Fillable.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4  # 595.27 x 841.89 pt
    margin = 54.0       # Left margin (54 pt)
    right_margin = width - margin # Right edge alignment (541.27 pt)
    
    table_width = right_margin - margin # Total width 487.27 pt
    
    form = c.acroForm

    def draw_underline(x1, y, x2):
        c.setLineWidth(0.75)
        c.setStrokeColor(colors.black)
        c.line(x1, y, x2, y)

    # 1. Top Right Document Marker
    c.setFont("HeiseiKakuGo-W5", 10)
    c.setFillColor(colors.black)
    c.drawRightString(right_margin, height - 38, "別添２")

    # 2. Application Date Header
    c.setFont("Arial", 10)
    c.setFillColor(colors.black)
    c.drawString(right_margin - 170, height - 60, "Date")
    draw_underline(right_margin - 145, height - 62, right_margin)
    
    form.textfield(
        name='date',
        tooltip='Date',
        x=right_margin - 145,
        y=height - 62,
        width=145,
        height=18,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    # 3. Document Title
    c.setFont("Arial", 13)
    c.setFillColor(colors.black)
    c.drawCentredString(width / 2.0, height - 90, "Outline of intended activities")
    c.setFont("HeiseiKakuGo-W5", 10)
    c.drawCentredString(width / 2.0, height - 105, "（活動予定概要）")

    # 4. Applicant Info Header Box (Name, Sex, Age)
    box_top_y = height - 120
    box_height = 65
    box_bottom_y = box_top_y - box_height
    
    c.setLineWidth(0.8)
    c.setStrokeColor(colors.black)
    c.rect(margin, box_bottom_y, table_width, box_height, stroke=1, fill=0)

    # Header Box Labels
    y_labels = box_top_y - 18
    c.setFont("Arial", 10)
    c.drawString(margin + 10, y_labels, "Name of visa applicant")
    
    sex_label_x = margin + 310
    age_label_x = margin + 390
    c.drawString(sex_label_x, y_labels, "Sex")
    c.drawString(age_label_x, y_labels, "Age")

    y_inputs = box_top_y - 42
    
    # Name underlines & input fields
    surname_line_w = 95
    given_line_w = 175
    
    draw_underline(margin + 10, y_inputs, margin + 10 + surname_line_w)
    draw_underline(margin + 115, y_inputs, margin + 115 + given_line_w)

    form.textfield(
        name='surname',
        tooltip='Surname',
        x=margin + 12,
        y=y_inputs + 2,
        width=surname_line_w - 4,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    form.textfield(
        name='given_names',
        tooltip='Given and Middle name',
        x=margin + 117,
        y=y_inputs + 2,
        width=given_line_w - 4,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    c.setFont("Arial", 8)
    c.setFillColor(colors.HexColor('#374151'))
    c.drawString(margin + 25, y_inputs - 12, "(Surname)")
    c.drawString(margin + 140, y_inputs - 12, "(Given and Middle name)")

    # Sex & Age underlines & input fields
    sex_box_w = 55
    age_box_w = 55
    
    draw_underline(sex_label_x, y_inputs, sex_label_x + sex_box_w)
    draw_underline(age_label_x, y_inputs, age_label_x + age_box_w)

    form.textfield(
        name='sex',
        tooltip='Sex',
        x=sex_label_x,
        y=y_inputs + 2,
        width=sex_box_w,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    form.textfield(
        name='age',
        tooltip='Age',
        x=age_label_x,
        y=y_inputs + 2,
        width=age_box_w,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    # 5. Main Schedule Table
    table_top_y = box_bottom_y
    col1_w = 85
    col2_w = 145
    col3_w = table_width - col1_w - col2_w # 257.27 pt
    
    col1_x = margin
    col2_x = col1_x + col1_w
    col3_x = col2_x + col2_w

    # Table Header Row
    header_h = 42
    header_bottom_y = table_top_y - header_h

    c.rect(margin, header_bottom_y, table_width, header_h, stroke=1, fill=0)
    c.line(col2_x, table_top_y, col2_x, header_bottom_y)
    c.line(col3_x, table_top_y, col3_x, header_bottom_y)

    c.setFont("Arial", 9)
    c.setFillColor(colors.black)
    c.drawString(col1_x + 8, header_bottom_y + 18, "period")

    # Column 2 Header
    text_obj2 = c.beginText(col2_x + 6, header_bottom_y + 26)
    text_obj2.setFont("Arial", 8.5)
    text_obj2.setLeading(11)
    text_obj2.textLine("In which city or prefecture do")
    text_obj2.textLine("you intend to stay?")
    c.drawText(text_obj2)

    # Column 3 Header
    text_obj3 = c.beginText(col3_x + 6, header_bottom_y + 28)
    text_obj3.setFont("Arial", 8.5)
    text_obj3.setLeading(11)
    text_obj3.textLine("Please give an outline of activities you wish to")
    text_obj3.textLine("engage in Japan. (ex. Travel, work, study)")
    c.drawText(text_obj3)

    # 7 Activity Rows
    num_rows = 7
    row_h = 80
    
    for i in range(num_rows):
        r_top_y = header_bottom_y - (i * row_h)
        r_bottom_y = r_top_y - row_h

        # Outer row box & vertical column lines
        c.rect(margin, r_bottom_y, table_width, row_h, stroke=1, fill=0)
        c.line(col2_x, r_top_y, col2_x, r_bottom_y)
        c.line(col3_x, r_top_y, col3_x, r_bottom_y)

        # Col 1 Labels: from (date) / to (date)
        c.setFont("Arial", 8)
        c.setFillColor(colors.HexColor('#1F2937'))
        c.drawString(col1_x + 5, r_top_y - 14, "from")
        c.drawString(col1_x + 5, r_top_y - 25, "(date)")
        c.drawString(col1_x + 5, r_top_y - 50, "to")
        c.drawString(col1_x + 5, r_top_y - 61, "(date)")

        # Col 1 Fillable Dates
        form.textfield(
            name=f'period_from_{i+1}',
            tooltip=f'Period from date row {i+1}',
            x=col1_x + 32,
            y=r_top_y - 28,
            width=col1_w - 36,
            height=18,
            borderStyle='solid',
            borderWidth=0,
            fillColor=colors.HexColor('#F8FAFC'),
            borderColor=colors.HexColor('#CBD5E1'),
            fontSize=8,
            textColor=colors.black
        )

        form.textfield(
            name=f'period_to_{i+1}',
            tooltip=f'Period to date row {i+1}',
            x=col1_x + 32,
            y=r_top_y - 64,
            width=col1_w - 36,
            height=18,
            borderStyle='solid',
            borderWidth=0,
            fillColor=colors.HexColor('#F8FAFC'),
            borderColor=colors.HexColor('#CBD5E1'),
            fontSize=8,
            textColor=colors.black
        )

        # Col 2 Multi-line Input Field: City / Prefecture
        form.textfield(
            name=f'location_{i+1}',
            tooltip=f'Location row {i+1}',
            x=col2_x + 4,
            y=r_bottom_y + 4,
            width=col2_w - 8,
            height=row_h - 8,
            fieldFlags='multiline',
            borderStyle='solid',
            borderWidth=0,
            fillColor=colors.HexColor('#F8FAFC'),
            borderColor=colors.HexColor('#F8FAFC'),
            fontSize=9,
            textColor=colors.black
        )

        # Col 3 Multi-line Input Field: Outline of Activities
        form.textfield(
            name=f'activities_{i+1}',
            tooltip=f'Outline of activities row {i+1}',
            x=col3_x + 4,
            y=r_bottom_y + 4,
            width=col3_w - 8,
            height=row_h - 8,
            fieldFlags='multiline',
            borderStyle='solid',
            borderWidth=0,
            fillColor=colors.HexColor('#F8FAFC'),
            borderColor=colors.HexColor('#F8FAFC'),
            fontSize=9,
            textColor=colors.black
        )

    c.save()

if __name__ == '__main__':
    create_outline_activities()