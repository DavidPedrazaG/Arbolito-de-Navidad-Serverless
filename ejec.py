from firstNode import handler

handler.hello(None, None)

import PIL.Image

# Convert image to grayscale and resize
def image_to_ascii(image_path, width=100):
    img = PIL.Image.open(image_path).convert('L')  # Convert to grayscale
    img = img.resize((width, int(width * img.height / img.width)))  # Resize to fit

    # ASCII characters by brightness
    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
    
    pixels = img.getdata()
    ascii_str = ""
    
    # Convert pixels to ASCII characters
    for pixel in pixels:
        ascii_str += ascii_chars[pixel // 25]
    
    # Format to have line breaks
    ascii_art = [ascii_str[index: index + width] for index in range(0, len(ascii_str), width)]
    return "\n".join(ascii_art)

# Path to the uploaded image
img_path = "image.png"
ascii_art = image_to_ascii(img_path)
print(ascii_art)


from PIL import Image
import matplotlib.pyplot as plt

# Load the image
img_path = "image.png"
img = Image.open(img_path)

# Display the image
plt.imshow(img)
plt.axis('off') # Hide axis
plt.show()