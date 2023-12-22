from pathlib import Path


def path(image_name):
    return str(Path(__file__).parent.joinpath(f'image/{image_name}'))
