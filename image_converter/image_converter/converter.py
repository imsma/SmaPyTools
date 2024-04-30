import base64
from PIL import Image
import io

class ImageConverter:
    """A class to convert images to Base64 encoded strings."""
    
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = self._load_image()

    def _load_image(self):
        """Private method to load an image from the specified path."""
        try:
            return Image.open(self.image_path)
        except IOError:
            raise FileNotFoundError(f"Cannot load image from {self.image_path}")

    def get_base64(self):
        """Convert the loaded image to a Base64 encoded string."""
        buffered = io.BytesIO()
        self.image.save(buffered, format=self.image.format)
        img_str = base64.b64encode(buffered.getvalue())
        return img_str.decode('utf-8')