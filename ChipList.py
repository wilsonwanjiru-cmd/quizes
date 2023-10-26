def create_chip_list(chips, maxChipsDisplayed, maxTextLength):
    if not chips or len(chips) == 0:
        return []

    if maxChipsDisplayed <= 0:
        # Only the "+n more items" label will be displayed
        return ["+" + str(len(chips) - 1) + " more items"]

    visible_chips = chips[:maxChipsDisplayed]
    exceeding_chips = chips[maxChipsDisplayed:]

    result = []

    for index, chip in enumerate(visible_chips):
        label = chip["label"]
        if len(label) <= maxTextLength:
            result.append(label)
        else:
            result.append(label[:maxTextLength] + "...")
            
    if exceeding_chips:
        result.append("+" + str(len(exceeding_chips)) + " more items")

    return result

# Example usage:
sample_chips = [
    {"label": "123456"},
    {"label": "1234567"},
    {"label": "12345678"},
    {"label": "12345"},
    {"label": "123456789"}
]

max_chips_displayed = 3
max_text_length = 6

result = create_chip_list(sample_chips, max_chips_displayed, max_text_length)
for item in result:
    print(item)

