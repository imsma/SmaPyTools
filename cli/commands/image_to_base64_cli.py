from ..base_cli import BaseCLI
from image_converter.image_converter.converter import ImageConverter


class ImageToBase64CLI(BaseCLI):
    def __init__(self, image_path, output=None):
        self.image_path = image_path
        self.output = output

    def execute(self):
        converter = ImageConverter(self.image_path)
        base64_string = converter.get_base64()
        if self.output:
            with open(self.output, 'w') as file:
                file.write(base64_string)
            print(f"Base64 string saved to {self.output}")
        else:
            print(base64_string)
