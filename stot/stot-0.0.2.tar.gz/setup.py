from setuptools import setup, find_packages

setup(
    name='stot',
    url='https://github.com/dsymbol/stot',
    version='0.0.2',
    author='dsymbol',
    description="real-time transcription of speech to text using whisper",
    include_package_data=True,
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        'pyaudio',
        'SpeechRecognition',
        'requests',
        'tqdm',
        'torch',
        'torchvision',
        'torchaudio',
        'openai-whisper'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'stot = stot.__main__:main'
        ]
    }
)
