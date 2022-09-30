import sys
import cv2
import re
import os


def cutSkinHead(skinPath, headPath, size=(64, 64)):
    img = cv2.imread(skinPath)
    img = img[8:16, 8:16]
    img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    cv2.imwrite(headPath, img)


if __name__ == '__main__':
    skinPath = sys.argv[1] if len(sys.argv) > 1 else None
    headPath = sys.argv[2] if len(sys.argv) > 2 else None
    size = sys.argv[3] if len(sys.argv) > 3 else None

    if skinPath is None:
        print("No skin path specified")
        sys.exit(1)

    if not os.path.exists(skinPath):
        print("Skin path does not exist")
        sys.exit(1)

    if not os.path.isfile(skinPath):
        print("Skin path is not a file")
        sys.exit(1)

    if not skinPath.endswith(".png"):
        print("Skin path should be .png")
        sys.exit(1)

    if headPath is None:
        print("No head path specified, using default.")
        headPath = os.path.basename(skinPath).replace(".png", ".") + "head.png"

    if not headPath.endswith(".png"):
        print("Head path should be .png, using default.")
        headPath = os.path.basename(skinPath).replace(".png", ".") + "head.png"

    if size is None:
        print("No size specified, using default 64x64px")
        size = "64x64"

    if not len(re.findall(r'^\d+x\d+$', size)) > 0:
        print("Size must be in format like 64x64")
        print("Using default 64x64px")
        size = (64, 64)
    else:
        size = tuple(map(int, size.split('x')))

    try:
        cutSkinHead(skinPath, headPath, size)
        print("Done")
    except Exception as e:
        print(f'Unexpected error: {e}')
