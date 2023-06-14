from PIL import Image

image_name = input("Input the image name(add .png extension): ")
new_image = input("Input the new image name for the resized image: ")

def resize_image(size1, size2):
    image = Image.open(image_name)

    print(f"Current size: {image.size}")

    resized_image = Image.resize((size1, size2))

    resized_image.save(new_image)

size1 = int(input("Enter width: "))
size2 = int(input("Enter length: "))
resize_image(size1, size2)