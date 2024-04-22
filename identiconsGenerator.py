import hashlib
from PIL import Image
from io import BytesIO


def getImage(matrix, color, image_size):

    height = width = image_size
    pixel_size = image_size//6
    shift = (image_size - 5*pixel_size)//2

    img = Image.new('RGB', (width, height), color='white')

    for y in range(5):
        for x in range(5):

            if matrix[y][x]:
                img.paste(color, ((x * pixel_size+shift),
                                  (y * pixel_size + shift),
                                  ((x + 1) * pixel_size + shift),
                                  ((y + 1) * pixel_size) + shift)
                          )

    img_byte_array = BytesIO()
    img.save(img_byte_array, format="PNG")
    img_byte_array = img_byte_array.getvalue()
    return img_byte_array


def identicons(string: str, image_size: int = 100):

    hash = hashlib.sha256(string.encode()).hexdigest()

    nums = [[0]*3 for _ in range(5)]
    color = ""

    for i in range(16):
        num = ""
        for j in range(4):
            num += hash[i+j*16]
        if i == 15:
            color = num
        else:
            nums[i//3][i % 3] = int(num, 16) % 2

    for r in nums:
        r.append(r[1])
        r.append(r[0])

    color = hash[:2]+color

    color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    return getImage(nums, color, image_size)
