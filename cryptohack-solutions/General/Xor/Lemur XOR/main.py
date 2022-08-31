from PIL import Image
import numpy as np

lemur = Image.open('lemur.png').getdata()
flag = Image.open('flag.png').getdata()

width, height = lemur.size

answer = []

for i in range(height):
    answer.append([])

    for j in range(width):
        l = lemur[i * width + j]
        f = flag[i * width + j]
        answer[i].append((
            l[0] ^ f[0],
            l[1] ^ f[1],
            l[2] ^ f[2],
        ))

array = np.array(answer, dtype=np.uint8)

result = Image.fromarray(array)
result.save('answer.png')
