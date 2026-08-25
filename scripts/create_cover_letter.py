from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer


OUTPUT = Path(__file__).resolve().parents[1] / "output" / "pdf" / "yash-srivastava-cover-letter.pdf"


def paragraph(text, style):
    return Paragraph(text, style)


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=17 * mm,
        bottomMargin=18 * mm,
        title="Yash Srivastava - Cover Letter",
        author="Yash Srivastava",
    )

    styles = getSampleStyleSheet()
    ink = colors.HexColor("#303030")
    muted = colors.HexColor("#707070")
    rule = colors.HexColor("#9A9A9A")

    name = ParagraphStyle(
        "Name",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=25,
        leading=28,
        textColor=ink,
        alignment=TA_CENTER,
        spaceAfter=3,
    )
    contact = ParagraphStyle(
        "Contact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=12,
        textColor=muted,
        alignment=TA_CENTER,
    )
    salutation = ParagraphStyle(
        "Salutation",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10.8,
        leading=15.2,
        textColor=ink,
        alignment=TA_LEFT,
        spaceAfter=8,
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10.7,
        leading=15.6,
        textColor=ink,
        alignment=TA_LEFT,
        spaceAfter=10,
    )
    closing = ParagraphStyle(
        "Closing",
        parent=body,
        spaceBefore=3,
        spaceAfter=0,
    )

    story = [
        paragraph("Yash Srivastava", name),
        paragraph(
            'officialyash2616@gmail.com&nbsp;&nbsp; | &nbsp;&nbsp;+91 8604802120&nbsp;&nbsp; | &nbsp;&nbsp;<link href="https://www.linkedin.com/in/yash-srivastava-04802a15b/" color="#707070">LinkedIn</link>',
            contact,
        ),
        Spacer(1, 5 * mm),
        HRFlowable(width="100%", thickness=0.6, color=rule, spaceBefore=0, spaceAfter=7 * mm),
        paragraph("Dear Hiring Manager,", salutation),
        paragraph(
            "I’m a Senior Software Engineer and mobile product leader with 6+ years of experience building Flutter-based products across fintech, OTT, and AI. I’m excited to bring a blend of hands-on engineering, product ownership, experimentation, and team leadership to your organization.",
            body,
        ),
        paragraph(
            "In my current role as Team Lead at Made Card, I own mobile architecture and product delivery for conversion-focused fintech experiences. I increased average monthly Subscription Card spend from approximately $90 to $120 per active user through iterative A/B testing, doubled user activation from 10% to approximately 20%, and helped generate 25-30 qualified mortgage leads per month. I also built scalable interaction analytics and engagement heatmaps that gave leadership stronger data for third-party aggregator negotiations.",
            body,
        ),
        paragraph(
            "Previously at STAGE, I led mobile initiatives for a product serving a 40M+ user base. My work improved DAU by 7%, increased average monthly watch time from 5.5 to 6 hours, improved Month 1-to-Month 2 retention by 5%, and reduced boot-time requests by 50% while lowering costs by 22%. I also shipped the STAGE TV app from scratch to production in under two weeks and built attribution backfilling to preserve ad-set-level AppsFlyer data for late-signup users.",
            body,
        ),
        paragraph(
            "What I bring is more than Flutter implementation: I enjoy turning ambiguous customer or business problems into measurable product outcomes. I’m comfortable owning user journeys, funnels, A/B experiments, analytics instrumentation, performance improvements, and delivery with cross-functional teams. I also use AI-assisted engineering workflows thoughtfully to accelerate execution without compromising product quality.",
            body,
        ),
        paragraph(
            "I would welcome the opportunity to discuss how my experience in mobile product engineering and growth-focused delivery could contribute to your company’s goals.",
            body,
        ),
        paragraph("Sincerely,<br/>Yash Srivastava", closing),
    ]
    doc.build(story)


if __name__ == "__main__":
    main()
