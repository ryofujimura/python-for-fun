from PIL import Image
from collections import Counter
color_categories = {
    'red': (200,0,0),
    'green': (0,200,0),
    'blue': (0,0,200),
    'yellow': (255,255,0),
    'white': (255, 255, 255),
    'black': (0,0,0),
}

def categorizeColor(rgb):
    # print('runnning...2')
    r, g, b = rgb
    min_distance = float('inf')
    category = 'Unknown'
    for name, (cr, cg, cb) in color_categories.items():
        distance = (r - cr) ** 2 + (g - cg) ** (b- cb) ** 2
        if distance < min_distance:
            min_distance = distance
            category = name
    return category

def detectMajorityColor(image_path):
    print('runnning...1')
    image = Image.open(image_path)
    image = image.resize((100,100))
    pixels = list(image.getdata())
    color_count = Counter(pixels)
    majority_color = color_count.most_common(1)[0][0]
    color_mapping = {color: categorizeColor(color) for color in color_count}
    return majority_color, color_mapping

image_path = './image.jpg'
print('image detected')
print('runnning...0')
majoriy_color, color_mapping = detectMajorityColor(image_path)
print(f'Majority Color: {majoriy_color}')
# print(f'Print Mapping: {color_mapping}')