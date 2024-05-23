from utils.encode_image import encode_image

def process_receipt(image_path):
    # Encode the image
    base64_image = encode_image(image_path)
    
    # Console log the image path
    print(f"Processing: {image_path}")
    return