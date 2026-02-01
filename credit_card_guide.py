#!/usr/bin/env python3
"""Generate a credit card rewards guide PDF."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def create_pdf():
    doc = SimpleDocTemplate(
        "/home/user/Claude-Code/Credit_Card_Rewards_Guide.pdf",
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1a365d')
    )

    category_style = ParagraphStyle(
        'Category',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=8,
        textColor=colors.HexColor('#2c5282'),
        borderPadding=5
    )

    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#4a5568'),
        spaceAfter=25
    )

    story = []

    # Title
    story.append(Paragraph("💳 Credit Card Rewards Guide", title_style))
    story.append(Paragraph("Top 3 Cards by Spending Category", subtitle_style))
    story.append(Spacer(1, 10))

    # Categories data: (Category Name, [(Card, Rate, Notes), ...])
    categories = [
        ("🍽️ DINING & RESTAURANTS", [
            ("Citi Prestige", "5x ThankYou Points", "All restaurants incl. takeout/delivery"),
            ("Gemini Card", "3% back in crypto", "All dining purchases"),
            ("Citi Strata Elite", "3x-6x Points", "6x Fri-Sat 6PM-6AM, 3x other times"),
        ]),
        ("✈️ FLIGHTS / AIRFARE", [
            ("Citi Strata Elite", "6x Points", "Via Citi Travel portal"),
            ("Citi Prestige", "5x ThankYou Points", "Direct or travel agency purchases"),
            ("Amex Platinum", "5x MR Points", "Direct with airlines or Amex Travel"),
        ]),
        ("🏨 HOTELS", [
            ("Citi Strata Elite", "12x Points", "Hotels booked via Citi Travel"),
            ("Chase World of Hyatt", "9x Points", "At Hyatt properties (4x card + 5x member)"),
            ("Cap One Venture", "5x Miles", "Via Capital One Travel portal"),
        ]),
        ("🛒 GROCERIES", [
            ("Prime Visa", "5% back", "Whole Foods Market"),
            ("Gemini Card", "2% back in crypto", "All grocery stores"),
            ("Citi AAdvantage MilesUp", "2x AA Miles", "All grocery purchases"),
        ]),
        ("⛽ GAS STATIONS", [
            ("Gemini Card", "4% back in crypto", "Up to $300/month spend, then 1%"),
            ("Citi AAdvantage Platinum Select", "2x AA Miles", "All gas station purchases"),
            ("Prime Visa", "2% back", "All gas stations"),
        ]),
        ("🚇 TRANSIT & RIDESHARE", [
            ("Gemini Card", "4% back in crypto", "Transit, taxis, rideshare (up to $300/mo)"),
            ("Chase World of Hyatt", "2x Hyatt Points", "Local transit and commuting"),
            ("Chase Sapphire Preferred", "2x UR Points", "All travel including transit"),
        ]),
        ("📦 AMAZON & WHOLE FOODS", [
            ("Prime Visa", "5% back", "Amazon.com, Fresh, Whole Foods"),
            ("—", "—", "No other cards have Amazon bonuses"),
            ("—", "—", "Use everyday spend card for 1-2%"),
        ]),
        ("📺 STREAMING SERVICES", [
            ("Chase Sapphire Preferred", "3x UR Points", "Select streaming services"),
            ("Cap One Venture", "2x Miles", "Flat rate on all purchases"),
            ("Citi Strata Elite", "1.5x Points", "Base rate on all purchases"),
        ]),
        ("💼 BUSINESS: Shipping/Ads/Internet/Phone", [
            ("Chase Ink Business Preferred", "3x UR Points", "Up to $150K/year combined"),
            ("Cap One Venture", "2x Miles", "Flat rate fallback"),
            ("Citi Strata Elite", "1.5x Points", "Best base rate"),
        ]),
        ("🌐 EVERYTHING ELSE (Daily Spend)", [
            ("Cap One Venture", "2x Miles", "Flat 2x on ALL purchases"),
            ("Citi Strata Elite", "1.5x Points", "Best premium card base rate"),
            ("Chase Sapphire Preferred", "1x UR Points", "Transfer partners add value"),
        ]),
    ]

    # Table styling
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#e6f2ff')),
        ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#f7fafc')),
        ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#e6f2ff')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])

    col_widths = [2.3*inch, 1.5*inch, 3.2*inch]

    for cat_name, cards in categories:
        story.append(Paragraph(cat_name, category_style))

        data = [['Card', 'Earning Rate', 'Notes']]
        for i, (card, rate, notes) in enumerate(cards, 1):
            rank = ['🥇', '🥈', '🥉'][i-1] if card != "—" else ""
            data.append([f"{rank} {card}", rate, notes])

        table = Table(data, colWidths=col_widths)
        table.setStyle(table_style)
        story.append(table)
        story.append(Spacer(1, 5))

    # Footer notes
    story.append(Spacer(1, 15))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor('#718096'),
        alignment=TA_CENTER
    )
    story.append(Paragraph("Notes: Rates current as of February 2026. Portal bookings may be required for maximum rates.", footer_style))
    story.append(Paragraph("Always check issuer websites for the most current earning rates and terms.", footer_style))

    doc.build(story)
    print("PDF created: /home/user/Claude-Code/Credit_Card_Rewards_Guide.pdf")

if __name__ == "__main__":
    create_pdf()
