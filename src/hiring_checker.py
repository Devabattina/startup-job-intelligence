TARGET_ROLES = [
    "Data Analyst",
    "Business Analyst",
    "MIS Executive",
    "Operations Executive",
    "Customer Support",
    "Customer Success",
    "Process Associate",
    "Voice Process",
    "Non Voice Process"
]

def role_matches(title):
    title = title.lower()

    for role in TARGET_ROLES:
        if role.lower() in title:
            return True

    return False