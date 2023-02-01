# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onnx_clip']

package_data = \
{'': ['*'],
 'onnx_clip': ['data/.gitattributes',
               'data/.gitattributes',
               'data/.gitattributes',
               'data/.gitattributes',
               'data/.gitattributes',
               'data/CLIP.png',
               'data/CLIP.png',
               'data/CLIP.png',
               'data/CLIP.png',
               'data/CLIP.png',
               'data/bpe_simple_vocab_16e6.txt.gz',
               'data/bpe_simple_vocab_16e6.txt.gz',
               'data/bpe_simple_vocab_16e6.txt.gz',
               'data/bpe_simple_vocab_16e6.txt.gz',
               'data/bpe_simple_vocab_16e6.txt.gz',
               'data/expected_preprocessed_image.npy',
               'data/expected_preprocessed_image.npy',
               'data/expected_preprocessed_image.npy',
               'data/expected_preprocessed_image.npy',
               'data/expected_preprocessed_image.npy',
               'data/franz-kafka.jpg',
               'data/franz-kafka.jpg',
               'data/franz-kafka.jpg',
               'data/franz-kafka.jpg',
               'data/franz-kafka.jpg']}

install_requires = \
['boto3>=1.23.10,<2.0.0',
 'ftfy>=6.0.3,<7.0.0',
 'numpy>=1.18.0,<2.0.0',
 'onnxruntime>=1.4.0',
 'opencv-python-headless>=4.0.1,<5.0.0',
 'pillow>=8.4.0,<9.0.0',
 'regex']

setup_kwargs = {
    'name': 'onnx-clip',
    'version': '2.0.1',
    'description': 'CLIP with ONNX Runtime and without PyTorch dependencies.',
    'long_description': '# onnx_clip\n\nAn [ONNX](https://onnx.ai/)-based implementation of [CLIP](https://github.com/openai/CLIP) that doesn\'t\ndepend on `torch` or `torchvision`.\n\nThis works by\n- running the text and vision encoders (the ViT-B/32 variant) in [ONNX Runtime](https://onnxruntime.ai/)\n- using a pure NumPy version of the tokenizer\n- using a pure NumPy+PIL version of the [preprocess function](https://github.com/openai/CLIP/blob/3702849800aa56e2223035bccd1c6ef91c704ca8/clip/clip.py#L79).\n  The PIL dependency could also be removed with minimal code changes - see `preprocessor.py`.\n\n## git lfs\nThis repository uses Git LFS for the `.onnx` files of the image and text models.\nMake sure to do `git lfs install` before cloning.\n\nIn case you use the `onnx_clip` project not as a repo, but as a package,\nthe models will be downloaded from the public S3 bucket:\n[image model](https://lakera-clip.s3.eu-west-1.amazonaws.com/clip_image_model_vitb32.onnx),\n[text model](https://lakera-clip.s3.eu-west-1.amazonaws.com/clip_text_model_vitb32.onnx).\n\n## Installation\nTo install, run the following in the root of the repository:\n```bash\npip install .\n```\n\n## Usage\n\nAll you need to do is call the `OnnxClip` model class. An example:\n\n```python\nfrom onnx_clip import OnnxClip, softmax, get_similarity_scores\nfrom PIL import Image\n\nimages = [Image.open("onnx_clip/data/franz-kafka.jpg").convert("RGB")]\ntexts = ["a photo of a man", "a photo of a woman"]\n\nonnx_model = OnnxClip()\n\n# Unlike the original CLIP, there is no need to run tokenization/preprocessing\n# separately - simply run get_image_embeddings directly on PIL images/NumPy\n# arrays, and run get_text_embeddings directly on strings.\nimage_embeddings = onnx_model.get_image_embeddings(images)\ntext_embeddings = onnx_model.get_text_embeddings(texts)\n\n# To use the embeddings for zero-shot classification, you can use these two\n# functions. Here we run on a single image, but any number is supported.\nlogits = get_similarity_scores(image_embeddings, text_embeddings)\nprobabilities = softmax(logits)\n\nprint("Logits:", logits)\n\nfor text, p in zip(texts, probabilities[0]):\n    print(f"Probability that the image is \'{text}\': {p:.3f}")\n```\n\n## Building & developing from source\n\n**Note**: The following may give timeout errors due to the filesizes. If so, this can be fixed with poetry version 1.1.13 - see [this related issue.](https://github.com/python-poetry/poetry/issues/6009)\n\n### Install, run, build and publish with Poetry\n\nInstall [Poetry](https://python-poetry.org/docs/)\n```\ncurl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -\n```\n\nTo setup the project and create a virtual environment run the following command from the project\'s root directory.\n```\npoetry install\n```\n\nTo build a source and wheel distribution of the library run the following command from the project\'s root directory.\n```\npoetry build\n```\n\n#### Instructions to publish the build artifacts for project maintainers\n\nFirst, configure the upload API endpoint in Poetry:\n```shell\npoetry config repositories.onnx_clip https://gitlab.com/api/v4/projects/41150990/packages/pypi\n```\n\nWith this setup you can now publish a package like so\n```\npoetry publish --repository onnx_clip -u <access_token_name> -p <access_token_key>\n```\nWARNING: Do not publish to the public pypi registry, e.g. always use the --repository option.\nNOTE1: You must generate [an access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)\nwith scope set to api.  \nNOTE2: The push will fail if there is already a package with the same version. You can increment the version using [poetry](https://python-poetry.org/docs/cli/#version)\n```\npoetry version\n```\nor by manually changing the version number in pyproject.toml.\n\n## Help\n\nPlease let us know how we can support you: [earlyaccess@lakera.ai](mailto:earlyaccess@lakera.ai).\n\n## LICENSE\nSee the [LICENSE](./LICENSE) file in this repository.\n\nThe `franz-kafka.jpg` is taken from [here](https://www.knesebeck-verlag.de/franz_kafka/p-1/270).',
    'author': 'Lakera AI',
    'author_email': 'dev@lakera.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
