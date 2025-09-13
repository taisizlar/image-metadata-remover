from PIL import Image

input_name = input("Enter input image name (with extension): ")
output_name = input("Enter output image name (without extension): ")

image = Image.open(input_name)
image.save(output_name + ".jpg", "JPEG")

print("Metadata removed. New image created:", output_name + ".jpg")