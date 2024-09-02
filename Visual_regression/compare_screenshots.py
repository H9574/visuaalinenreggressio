from PIL import Image
import imagehash

def compare_screenshot(img1_path, img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    hash1 = imagehash.average_hash(img1)
    hash2 = imagehash.average_hash(img2)

    difference = hash1 - hash2

    if difference > 10:  # Tolerance level
        print('Images are different!')
        print(f'Difference: {difference}')
        return False
    else:
        return True

#compare_images('screenshots/testi3.png', 'screenshots/testi5.png')
