import imageio.v3 as iio

filenames = ['20171213_214811.jpg', '20171214_224904.jpg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("snowman.gif", images, duration = 1500, loop = 0)