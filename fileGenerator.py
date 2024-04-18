from pathlib import Path

directory = "/Users/adithyaviswanathan/gitx/test"

for i in range(1800):
    file_path = directory + str(i) + ".yaml"
    print (file_path)
    Path(file_path).touch()