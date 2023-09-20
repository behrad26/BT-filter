def grayscale(img: list) -> None:
    height, width = len(img), len(img[0])
    for i in range(height):
        for j in range(width):
            img[i][j][0] = img[i][j][1] = img[i][j][2] = sum(img[i][j]) // 3


def sepia(img: list) -> None:
    height, width = len(img), len(img[0])
    for i in range(height):
        for j in range(width):
            red = round(
                0.393 * img[i][j][0] + 0.769 * img[i][j][1] + 0.189 * img[i][j][2]
            )
            green = round(
                0.349 * img[i][j][0] + 0.686 * img[i][j][1] + 0.168 * img[i][j][2]
            )
            blue = round(
                0.272 * img[i][j][0] + 0.534 * img[i][j][1] + 0.131 * img[i][j][2]
            )
            img[i][j][0] = red if red < 255 else 255
            img[i][j][1] = green if green < 255 else 255
            img[i][j][2] = blue if blue < 255 else 255


def reflect_horizontally(img: list) -> None:
    height, width = len(img), len(img[0])
    for i in range(height):
        for j in range(width // 2):
            img[i][j][0], img[i][width - j - 1][0] = (
                img[i][width - j - 1][0],
                img[i][j][0],
            )
            img[i][j][1], img[i][width - j - 1][1] = (
                img[i][width - j - 1][1],
                img[i][j][1],
            )
            img[i][j][2], img[i][width - j - 1][2] = (
                img[i][width - j - 1][2],
                img[i][j][2],
            )


def reflect_vertically(img: list) -> None:
    height, width = len(img), len(img[0])
    for i in range(height // 2):
        for j in range(width):
            for k in range(3):
                img[i][j][k], img[height - i - 1][j][k] = img[height - i - 1][j][k], img[i][j][k]


def blur1(img: list) -> None:
    height, width = len(img), len(img[0])
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            for k in range(3):
                img[i][j][k] = (
                    sum(
                        [
                            img[i - 1][j - 1][k],
                            img[i - 1][j][k],
                            img[i - 1][j + 1][k],
                            img[i][j - 1][k],
                            img[i][j][k],
                            img[i][j + 1][k],
                            img[i + 1][j - 1][k],
                            img[i + 1][j][k],
                            img[i + 1][j + 1][k],
                        ]
                    )
                    // 9
                )


def blur2(img: list) -> None:
    height, width = len(img), len(img[0])
    for i in range(2, height - 2):
        for j in range(2, width - 2):
            for k in range(3):
                img[i][j][k] = (
                    sum(
                        [
                            img[i - 2][j - 2][k],
                            img[i - 2][j - 1][k],
                            img[i - 2][j][k],
                            img[i - 2][j + 1][k],
                            img[i - 2][j + 2][k],
                            img[i - 1][j - 2][k],
                            img[i - 1][j - 1][k],
                            img[i - 1][j][k],
                            img[i - 1][j + 1][k],
                            img[i - 1][j + 2][k],
                            img[i][j - 2][k],
                            img[i][j - 1][k],
                            img[i][j][k],
                            img[i][j + 1][k],
                            img[i][j + 2][k],
                            img[i + 1][j - 2][k],
                            img[i + 1][j - 1][k],
                            img[i + 1][j][k],
                            img[i + 1][j + 1][k],
                            img[i + 1][j + 2][k],
                            img[i + 2][j - 2][k],
                            img[i + 2][j - 1][k],
                            img[i + 2][j][k],
                            img[i + 2][j + 1][k],
                            img[i + 2][j + 2][k],
                        ]
                    )
                    // 25
                )

def blur3(img: list) -> None:
    height, width = len(img), len(img[0])
    for i in range(3, height - 3):
        for j in range(3, width - 3):
            for k in range(3):
                img[i][j][k] = (
                    sum(
                        [
                            img[i - 3][j - 3][k],
                            img[i - 3][j - 2][k],
                            img[i - 3][j - 1][k],
                            img[i - 3][j][k],
                            img[i - 3][j + 1][k],
                            img[i - 3][j + 2][k],
                            img[i - 3][j + 3][k],
                            img[i - 2][j - 3][k],
                            img[i - 2][j - 2][k],
                            img[i - 2][j - 1][k],
                            img[i - 2][j][k],
                            img[i - 2][j + 1][k],
                            img[i - 2][j + 2][k],
                            img[i - 2][j + 3][k],
                            img[i - 1][j - 3][k],
                            img[i - 1][j - 2][k],
                            img[i - 1][j - 1][k],
                            img[i - 1][j][k],
                            img[i - 1][j + 1][k],
                            img[i - 1][j + 2][k],
                            img[i - 1][j + 3][k],
                            img[i][j - 3][k],
                            img[i][j - 2][k],
                            img[i][j - 1][k],
                            img[i][j][k],
                            img[i][j + 1][k],
                            img[i][j + 2][k],
                            img[i][j + 3][k],
                            img[i + 1][j - 3][k],
                            img[i + 1][j - 2][k],
                            img[i + 1][j - 1][k],
                            img[i + 1][j][k],
                            img[i + 1][j + 1][k],
                            img[i + 1][j + 2][k],
                            img[i + 1][j + 3][k],
                            img[i + 2][j - 3][k],
                            img[i + 2][j - 2][k],
                            img[i + 2][j - 1][k],
                            img[i + 2][j][k],
                            img[i + 2][j + 1][k],
                            img[i + 2][j + 2][k],
                            img[i + 2][j + 3][k],
                            img[i + 3][j - 3][k],
                            img[i + 3][j - 2][k],
                            img[i + 3][j - 1][k],
                            img[i + 3][j][k],
                            img[i + 3][j + 1][k],
                            img[i + 3][j + 2][k],
                            img[i + 3][j + 3][k],
                        ]
                    )
                    // 49
                )