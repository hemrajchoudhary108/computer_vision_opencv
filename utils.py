import cv2
def read_image(image_path, flag=cv2.IMREAD_UNCHANGED):

    '''
    :param image_path: str, path to image file.
    :param flag: int, flag to read image. Default is cv2.IMREAD_UNCHANGED.
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
    :param point1: tuple, (x, y) coordinate of start point.
    :param point2: tuple, (x, y) coordinate of end point.
    '''

    cv2.line(image, point1, point2, color, thickness, lineType=line_type)
    return image

def draw_rectangle(image, point1, point2, color=(256, 256, 255), thickness=2, line_type=cv2.LINE_AA):

    '''
    :param point1: tuple, (x, y) coordinate of top-left point.
    :param point2: tuple, (x, y) coordinate of bottom-right point.
    '''
    
    cv2.rectangle(image, point1, point2, color, thickness, lineType=line_type)
    return image

def draw_circle(image, center, radius, color=(256, 256, 255), thickness=2, line_type=cv2.LINE_AA):
    
    '''
    :param center: tuple, (x, y) coordinate of center of circle.
    :param radius: int, radius of circle.
    '''
    
    cv2.circle(image, center, radius, color, thickness, lineType=line_type)
    return image

def write_text(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, size=2, color=(256, 256, 255), thickness=2, line_type=cv2.LINE_AA):
    
    '''
    :param position: tuple, (x, y) coordinate of text this should be the bottom-left corner of the text string in the image.
    :param font: int, font of text. Default is cv2.FONT_HERSHEY_SIMPLEX.
    :param size: int, font scale of text. Default is 1.
    '''
    
    cv2.putText(image, text, position, font, size, color, thickness, lineType=line_type)
    return image

