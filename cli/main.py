import click

from .commands.image_to_base64_cli import ImageToBase64CLI

@click.group()
def cli():
    """CLI tool for various utilities in SmaPyTools."""
    pass

@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.option('--output', type=click.Path(), help='Output file path to save the Base64 string.')
def image_to_base64(image_path, output):
    command = ImageToBase64CLI(image_path, output)
    command.execute()

if __name__ == '__main__':
    cli()

