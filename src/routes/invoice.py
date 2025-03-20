from fastapi import APIRouter, BackgroundTasks
import smtplib
from email.message import EmailMessage
import ssl
import os

from src.schemas import OrderCreate
from src.utils import create_invoice

route = APIRouter()


def send_email_with_invoice(to_email: str, pdf_bytes: bytes):
    """Send email with invoice PDF as an attachment."""
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASS")
    subject = "Your JungleSmart Invoice"
    body = "Dear Customer,\n\nPlease find your invoice attached.\n\nThank you for your business!"

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    msg.add_attachment(
        pdf_bytes, maintype="application", subtype="pdf", filename="invoice.pdf"
    )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)


@route.post("/generate-invoice/")
def send_invoice(order: OrderCreate, background_tasks: BackgroundTasks):
    """Generate invoice PDF and send it via email."""
    pdf_bytes = create_invoice(order)
    background_tasks.add_task(send_email_with_invoice, order.customer_email, pdf_bytes)
    return {"message": "Invoice generated and sent to email."}
