BANK_PATTERNS = {
    "HDFC": {
        "last_4_digits": r"Card No.*?(\d{4})",
        "billing_cycle": r"Statement Period\s*:\s*(.*)",
        "due_date": r"Payment Due Date\s*:\s*(.*)",
        "total_due": r"Total Amount Due\s*Rs\.?\s*([\d,]+)"
    },
    "ICICI": {
        "last_4_digits": r"XXXX\s+XXXX\s+XXXX\s+(\d{4})",
        "billing_cycle": r"Statement Period\s*:\s*(.*)",
        "due_date": r"Payment Due Date\s*:\s*(.*)",
        "total_due": r"Total Amount Due\s*₹?\s*([\d,]+)"
    },
    "AXIS": {
        "last_4_digits": r"XX+(\d{4})",
        "billing_cycle": r"Statement Period\s*:\s*(.*)",
        "due_date": r"Payment Due Date\s*:\s*(.*)",
        "total_due": r"Total Amount Due\s*₹?\s*([\d,]+)"
    },
    "SBI": {
        "last_4_digits": r"Card No.*?(\d{4})",
        "billing_cycle": r"Statement Period\s*:\s*(.*)",
        "due_date": r"Payment Due Date\s*:\s*(.*)",
        "total_due": r"Total Amount Due\s*₹?\s*([\d,]+)"
    },
    "AMEX": {
        "last_4_digits": r"Account Ending\s+(\d{4})",
        "billing_cycle": r"Statement Period\s*:\s*(.*)",
        "due_date": r"Payment Due Date\s*:\s*(.*)",
        "total_due": r"Total Amount Due\s*₹?\s*([\d,]+\.\d{2})"
    }
}
