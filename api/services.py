
def average_weight(entries):
    if not entries:
        return None
    return sum(entry.weight for entry in entries) / len(entries)

