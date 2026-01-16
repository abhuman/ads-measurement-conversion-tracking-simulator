def calculate_roi(revenue, spend):
    if spend == 0:
        return 0
    return round(((revenue - spend) / spend) * 100, 2)
