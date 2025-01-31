import colorgram

colours = colorgram.extract("art2.jpg", 10)
rgb_list = []
for colour in colours:
    t = (colour.rgb.r, colour.rgb.g, colour.rgb.b)
    rgb_list.append(t)
print(rgb_list)
