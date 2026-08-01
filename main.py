import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

def create_cv(filename="Working_Holiday_Visa_Resume_Fillable.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4 # 595.27 x 841.89 pt
    margin = 54.0 # Left margin (base)
    right_margin = width - margin # Right edge alignment
    
    input_x = margin + 16
    input_width = right_margin - input_x # 471.27 pt width
    
    form = c.acroForm

    def draw_circle(x, y):
        c.setLineWidth(0.8)
        c.setStrokeColor(colors.black)
        c.setFillColor(colors.white)
        c.circle(x, y + 3.5, 3.2, stroke=1, fill=0)

    def draw_underline(x1, y, x2):
        c.setLineWidth(0.75)
        c.setStrokeColor(colors.black)
        c.line(x1, y, x2, y)

    # 1. Top Right: 別添１
    c.setFont("HeiseiKakuGo-W5", 10)
    c.setFillColor(colors.black)
    c.drawRightString(right_margin, height - 38, "別添１")

    # 2. Date
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

    # 3. Document Title: R E S U M E (Regular font, not bold)
    c.setFont("Arial", 14)
    c.setFillColor(colors.black)
    title_text = "R E S U M E"
    c.drawCentredString(width / 2.0, height - 88, title_text)
    
    # Draw title underline
    title_w = c.stringWidth(title_text, "Arial", 14)
    draw_underline((width - title_w) / 2.0 - 2, height - 91, (width + title_w) / 2.0 + 2)

    c.setFont("HeiseiKakuGo-W5", 10)
    c.drawCentredString(width / 2.0, height - 105, "（履 歴 書）")

    # 4. Section 1: Name of visa applicant
    y1 = height - 128
    draw_circle(margin + 4, y1)
    
    c.setFont("Arial", 10)
    c.setFillColor(colors.black)
    c.drawString(margin + 16, y1, "Name of visa applicant:")

    # Sex & Age labels on row 1
    c.drawString(margin + 330, y1, "Sex:")
    c.drawString(margin + 420, y1, "Age:")

    y_name_row = y1 - 24
    draw_underline(input_x, y_name_row, margin + 310)
    draw_underline(margin + 330, y_name_row, margin + 395)
    draw_underline(margin + 420, y_name_row, right_margin)

    form.textfield(
        name='surname',
        tooltip='Surname',
        x=input_x + 2,
        y=y_name_row + 2,
        width=90,
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
        tooltip='Given and middle name',
        x=input_x + 100,
        y=y_name_row + 2,
        width=200,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    form.textfield(
        name='sex',
        tooltip='Sex',
        x=margin + 330,
        y=y_name_row + 2,
        width=65,
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
        x=margin + 420,
        y=y_name_row + 2,
        width=right_margin - (margin + 420),
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
    c.drawString(input_x + 15, y_name_row - 12, "(Surname)")
    c.drawString(input_x + 140, y_name_row - 12, "(Given and middle name)")

    # Date of Birth / Place of Birth row
    y2 = y_name_row - 32
    c.setFont("Arial", 10)
    c.setFillColor(colors.black)
    c.drawString(input_x, y2, "Date of birth :")
    
    dob_box_x = input_x + 68
    dob_box_w = 110
    draw_underline(dob_box_x, y2 - 2, dob_box_x + dob_box_w)
    form.textfield(
        name='dob',
        tooltip='Date of birth',
        x=dob_box_x,
        y=y2 - 2,
        width=dob_box_w,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    pob_label_x = dob_box_x + dob_box_w + 15
    c.drawString(pob_label_x, y2, "Place of birth :")
    pob_box_x = pob_label_x + 75
    draw_underline(pob_box_x, y2 - 2, right_margin)
    form.textfield(
        name='pob',
        tooltip='Place of birth',
        x=pob_box_x,
        y=y2 - 2,
        width=right_margin - pob_box_x,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    # 5. Section 2: Educational and Employment history
    y3 = y2 - 28
    draw_circle(margin + 4, y3)
    c.setFont("Arial", 10)
    c.setFillColor(colors.black)
    c.drawString(margin + 16, y3, "Educational and Employment history :")

    y_lines3 = y3 - 22
    for i in range(7):
        line_y = y_lines3 - (i * 20)
        draw_underline(input_x, line_y - 2, right_margin)
        form.textfield(
            name=f'edu_emp_history_{i+1}',
            tooltip=f'Educational and Employment history line {i+1}',
            x=input_x,
            y=line_y - 2,
            width=input_width,
            height=17,
            borderStyle='solid',
            borderWidth=0,
            fillColor=colors.HexColor('#F8FAFC'),
            borderColor=colors.HexColor('#F8FAFC'),
            fontSize=9,
            textColor=colors.black
        )

    # 6. Section 3: Experience of stay in Japan
    y4 = y_lines3 - (7 * 20) - 16
    draw_circle(margin + 4, y4)
    c.setFont("Arial", 10)
    c.setFillColor(colors.black)
    c.drawString(margin + 16, y4, "Experience of stay in Japan (if any, please write the period, purpose, and place of each visit) :")

    y_lines4 = y4 - 22
    for i in range(5):
        line_y = y_lines4 - (i * 20)
        draw_underline(input_x, line_y - 2, right_margin)
        form.textfield(
            name=f'japan_exp_{i+1}',
            tooltip=f'Japan experience line {i+1}',
            x=input_x,
            y=line_y - 2,
            width=input_width,
            height=17,
            borderStyle='solid',
            borderWidth=0,
            fillColor=colors.HexColor('#F8FAFC'),
            borderColor=colors.HexColor('#F8FAFC'),
            fontSize=9,
            textColor=colors.black
        )

    # 7. Section 4: Skills and Hobbies
    y5 = y_lines4 - (5 * 20) - 16
    draw_circle(margin + 4, y5)
    c.setFont("Arial", 10)
    c.setFillColor(colors.black)
    c.drawString(margin + 16, y5, "Skills and Hobbies :")

    for i in range(2):
        line_y = y5 - 20 - (i * 20)
        draw_underline(input_x, line_y - 2, right_margin)
        form.textfield(
            name=f'skills_hobbies_{i+1}',
            tooltip=f'Skills and Hobbies line {i+1}',
            x=input_x,
            y=line_y - 2,
            width=input_width,
            height=17,
            borderStyle='solid',
            borderWidth=0,
            fillColor=colors.HexColor('#F8FAFC'),
            borderColor=colors.HexColor('#F8FAFC'),
            fontSize=9,
            textColor=colors.black
        )

    # 8. Section 5: If your employment in Japan has been arranged
    y6 = y5 - 64
    draw_circle(margin + 4, y6)
    c.setFont("Arial", 10)
    c.setFillColor(colors.black)
    c.drawString(margin + 16, y6, "If your employment in Japan has been arranged, please fill the following.")

    col1_x = input_x
    col1_w = 230
    col2_x = margin + 265
    col2_w = right_margin - col2_x

    # Row 1
    y_r1 = y6 - 18
    c.drawString(col1_x, y_r1, "Name of employer :")
    c.drawString(col2_x, y_r1, "Tel :")
    
    y_r1_box = y_r1 - 20
    draw_underline(col1_x, y_r1_box, col1_x + col1_w)
    form.textfield(
        name='employer_name',
        x=col1_x,
        y=y_r1_box,
        width=col1_w,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    draw_underline(col2_x, y_r1_box, col2_x + col2_w)
    form.textfield(
        name='employer_tel',
        x=col2_x,
        y=y_r1_box,
        width=col2_w,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    # Row 2
    y_r2 = y_r1_box - 22
    c.drawString(col1_x, y_r2, "Address :")
    c.drawString(col2_x, y_r2, "Type of business :")

    y_r2_box = y_r2 - 20
    draw_underline(col1_x, y_r2_box, col1_x + col1_w)
    form.textfield(
        name='employer_address',
        x=col1_x,
        y=y_r2_box,
        width=col1_w,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    draw_underline(col2_x, y_r2_box, col2_x + col2_w)
    form.textfield(
        name='business_type',
        x=col2_x,
        y=y_r2_box,
        width=col2_w,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    # Row 3
    y_r3 = y_r2_box - 22
    c.drawString(col1_x, y_r3, "Working hours per day :")
    c.drawString(col2_x, y_r3, "Period of employment :")

    y_r3_box = y_r3 - 20
    draw_underline(col1_x, y_r3_box, col1_x + col1_w)
    form.textfield(
        name='working_hours',
        x=col1_x,
        y=y_r3_box,
        width=col1_w,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    draw_underline(col2_x, y_r3_box, col2_x + col2_w)
    form.textfield(
        name='employment_period',
        x=col2_x,
        y=y_r3_box,
        width=col2_w,
        height=17,
        borderStyle='solid',
        borderWidth=0,
        fillColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#F8FAFC'),
        fontSize=9,
        textColor=colors.black
    )

    c.save()


if __name__ == "__main__":
    create_cv()
