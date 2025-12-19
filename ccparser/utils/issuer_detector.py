# utils/issuer_detector.py
def detect_issuer(text):
    text = text.lower()

    if "hdfc bank" in text:
        return "HDFC"
    elif "icici bank" in text:
        return "ICICI"
    elif "axis bank" in text:
        return "AXIS"
    elif "sbi card" in text:
        return "SBI"
    elif "american express" in text:
        return "AMEX"
    else:
        return None
