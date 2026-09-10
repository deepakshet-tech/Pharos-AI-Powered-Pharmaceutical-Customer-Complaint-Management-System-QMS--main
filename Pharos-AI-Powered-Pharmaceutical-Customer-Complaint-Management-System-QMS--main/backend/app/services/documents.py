import email
import io
from email import policy

from pypdf import PdfReader


def parse_upload(filename: str, content: bytes) -> str:
    """Lightweight document parsing (production OCR intentionally out of scope)."""
    lower = (filename or "").lower()
    
    if lower.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(content))
        text = "\n".join((p.extract_text() or "") for p in reader.pages)
        
    elif lower.endswith(".docx"):
        import docx
        doc = docx.Document(io.BytesIO(content))
        text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
        
    elif lower.endswith(".doc"):
        raise ValueError("Legacy .doc files are not supported. Please save the document as .docx and re-upload.")
        
    elif lower.endswith(".eml"):
        msg = email.message_from_bytes(content, policy=policy.default)
        parts = []
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and not part.get_filename():
                try:
                    payload = part.get_content()
                except (LookupError, TypeError):
                    payload = part.get_payload(decode=True)
                    if isinstance(payload, bytes):
                        payload = payload.decode(part.get_content_charset() or "utf-8", errors="ignore")
                if payload:
                    parts.append(str(payload))
        text = "\n".join(parts)
        
    elif lower.endswith((".txt", ".md", ".csv")):
        text = content.decode("utf-8", errors="ignore")
        
    else:
        raise ValueError("Unsupported file type. Please upload PDF, DOCX, EML, or TXT — or paste the text directly.")
        
    if not text.strip():
        raise ValueError(
            "No readable text found. The file may be empty or an image-only PDF; "
            "try a text-based PDF, DOCX, EML, or TXT file."
        )
        
    return text
