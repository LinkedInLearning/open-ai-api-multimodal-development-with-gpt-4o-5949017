import base64

def encode_image(image_path):
    """
    Encode an image file as a base64 string.

    Parameters:
    image_path (str): The path to the image file to be encoded.

    Returns:
    str: The base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")