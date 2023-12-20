from PIL import Image

# image location on your personal system
image_location = Image.open(r'image-location')

image_one = image_location.convert('RGB')

# where you want to save the new image
image_one.save(r'image-saved-location')