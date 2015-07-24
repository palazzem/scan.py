import os
import subprocess


SCANNER_DEVICE = "epkowa:interpreter:001:008"
OUTPUT_FORMAT = "tiff"
RESOLUTION = 300
QUALITY = 50


def scan_to_file(filename):
    device = "--device {}".format(SCANNER_DEVICE)
    output_format = "--format={}".format(OUTPUT_FORMAT)
    resolution = "--resolution {}".format(RESOLUTION)
    subprocess.call("scanimage {} {} {} > {}".format(device, output_format, resolution, filename), shell=True)


def compress_images(images):
    jpeg_images = []
    files_list = " ".join(images)
    subprocess.call("mogrify -format jpg -quality {} {}".format(QUALITY, files_list), shell=True)

    # removing old images
    for image in images:
        os.remove(image)
        jpeg_images.append(image.replace(OUTPUT_FORMAT, "jpg"))

    return jpeg_images


def merge_images(images):
    files_list = " ".join(images)
    subprocess.call("convert {} output.pdf".format(files_list), shell=True)

    # removing old images
    for image in images:
        os.remove(image)

    return ["output.pdf"]


if __name__ == "__main__":
    another_page = True
    current_page = 0
    images_list = []

    # papers scan
    while another_page:
        current_page += 1
        filename = "file_{}.{}".format(current_page, OUTPUT_FORMAT)
        scan_to_file(filename)
        images_list.append(filename)
        another_page = input("Do you have another page? [y/N] ") in ["y", "Y"]

    # compressing to jpeg
    compression = input("Do you want to apply jpeg compression? [y/N] ") in ["y", "Y"]
    if compression:
        images_list = compress_images(images_list)

    # merging to PDF
    merging = input("Do you want to merge all images in a single PDF? [y/N] ") in ["y", "Y"]
    if merging:
        images_list = merge_images(images_list)

    print("Done!")
