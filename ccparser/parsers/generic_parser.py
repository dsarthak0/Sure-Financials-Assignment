import re
from parsers.bank_patterns import BANK_PATTERNS

class GenericCardParser:
    def parse(self, text: str, issuer: str):
        patterns = BANK_PATTERNS.get(issuer)
        if not patterns:
            raise ValueError("Unsupported issuer")

        data = {"issuer": issuer}

        for field, regex in patterns.items():
            data[field] = self._extract(regex, text)

        return data

    def _extract(self, pattern, text):
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1).strip() if match else None
