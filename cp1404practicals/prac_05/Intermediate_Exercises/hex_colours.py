COLOR_TO_HEX_CODE = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "AliceBlue": "#f0f8ff",
                     "AlizarinCrimson": "#e32636",
                     "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
                     "Apricot": "#fbceb1", "Aqua": "#00ffff"}

color_name = input("Enter a color name: ")
while color_name != "":
    if color_name in COLOR_TO_HEX_CODE:
        print(f"Hex code for {color_name} is: {COLOR_TO_HEX_CODE[color_name]}")
    else:
        print("Invalid color name, try again!")
    color_name = input("Enter a color name: ")
