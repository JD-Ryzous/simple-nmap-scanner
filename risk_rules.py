HIGH_RISK = [
    "telnet",
    "ftp",
    "rsh",
    "rexec"
]

MEDIUM_RISK = [
    "smtp",
    "snmp"
]


def get_risk(service):

    service = service.lower()

    if service in HIGH_RISK:
        return "HIGH"

    elif service in MEDIUM_RISK:
        return "MEDIUM"

    return "LOW"
