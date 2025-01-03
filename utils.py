import cv2
def read_image(image_path, flag=cv2.IMREAD_UNCHANGED):
    '''
    Read image from image_path and return it as numpy array.
    :param image_path: str, path to image file.
    :param flag: int, flag to read image. Default is cv2.IMREAD_UNCHANGED.
    :return: numpy array, image.
    '''
    image = cv2.imread(image_path, flag)
    
    cvt_color_code = cv2.COLOR_BGR2RGB
    if len(image.shape) == 4:
        cvt_color_code = cv2.COLOR_BGRA2RGBA

    # Converting the image from BGR to RGB
    image = cv2.cvtColor(image, cvt_color_code)

    return image

def write_image(image, image_path):
    '''
    Write image to image_path.
    :param image: numpy array, image.
    :param image_path: str, path to save image.
    '''
    written = cv2.imwrite(image_path, image)
    if not written:
        raise Exception(f'Failed to write image to {image_path}')
    return True

def draw_line(image, point1, point2, color=(0, 0, 255), thickness=2, line_type=cv2.LINE_AA):
    '''
    Draw line on image.
    :param image: numpy array, image.
    :param point1: tuple, (x, y) coordinate of start point.
    :param point2: tuple, (x, y) coordinate of end point.
    :param color: tuple, (r, g, b) color of line. Default is (0, 0, 255).
    :param thickness: int, thickness of line. Default is 2.
    '''
    cv2.line(image, point1, point2, color, thickness, lineType=line_type)
    return image

def draw_rectangle(image, point1, point2, color=(256, 256, 255), thickness=2, line_type=cv2.LINE_AA):
    '''
    Draw rectangle on image.
    :param image: numpy array, image.
    :param point1: tuple, (x, y) coordinate of top-left point.
    :param point2: tuple, (x, y) coordinate of bottom-right point.
    :param color: tuple, (r, g, b) color of rectangle. Default is (0, 0, 255).
    :param thickness: int, thickness of rectangle. Default is 2.
    '''
    cv2.rectangle(image, point1, point2, color, thickness, lineType=line_type)
    return image

def draw_circle(image, center, radius, color=(256, 256, 255), thickness=2, line_type=cv2.LINE_AA):
    '''
    Draw circle on image.
    :param image: numpy array, image.
    :param center: tuple, (x, y) coordinate of center of circle.
    :param radius: int, radius of circle.
    :param color: tuple, (r, g, b) color of circle. Default is (0, 0, 255).
    :param thickness: int, thickness of circle. Default is 2.
    '''
    cv2.circle(image, center, radius, color, thickness, lineType=line_type)
    return image

def write_text(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, size=2, color=(256, 256, 255), thickness=2, line_type=cv2.LINE_AA):
    '''
    Draw text on image.
    :param image: numpy array, image.
    :param text: str, text to draw.
    :param position: tuple, (x, y) coordinate of text this should be the bottom-left corner of the text string in the image.
    :param font: int, font of text. Default is cv2.FONT_HERSHEY_SIMPLEX.
    :param font_scale: int, font scale of text. Default is 1.
    :param color: tuple, (r, g, b) color of text. Default is (0, 0, 255).
    :param thickness: int, thickness of text. Default is 2.
    '''
    cv2.putText(image, text, position, font, size, color, thickness, lineType=line_type)
    return image

