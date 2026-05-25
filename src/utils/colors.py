def generate_hex_gradient(count: int) -> list[str]:
    """Generates a list of hex colors progressing from dark to light."""
    if count <= 0:
        return []
    if count == 1:
        return ["#111111"]

    colors = []
    # Start dark, go towards light
    start_val = 0x11
    end_val = 0xDD

    step = (end_val - start_val) / (count - 1)

    for i in range(count):
        val = int(start_val + (step * i))
        # Use grayscale for simplicity, or we can use a single hue like blue
        # Let's use a nice blue progression: Dark Blue to Light Blue
        r = val
        g = val
        b = min(0xFF, val + 0x22)  # slight blue tint
        colors.append(f"#{r:02x}{g:02x}{b:02x}")

    return colors
