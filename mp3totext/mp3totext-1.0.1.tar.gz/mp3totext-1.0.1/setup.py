from setuptools import setup, find_packages


setup(
    name='mp3totext',
    version='1.0.1',
    description='A simple extractor of text from mp3 (converts it to wav).',
    long_description='''
    This is a simple tool for converting MP3 audio files to text. It makes use of the SpeechRecognition, pydub, colorlog and argparse packages. The tool first converts the MP3 file to a WAV file and then uses the SpeechRecognition package to perform the speech-to-text conversion.
    
    To use the module you need to have a mp3 directory with .mp3 file/-s in it wherever you want to use the module.
    
    The source code is available on GitLab at https://gitlab.com/python3-projects/speechrecognition/mp3totext.
    ''',
    author='Kamil Dębski',
    author_email='kamil_debski@pm.me',
    packages=find_packages(),
    install_requires=[
        'SpeechRecognition',
        'pydub',
        'colorlog',
        'argparse',
    ],
    url='https://gitlab.com/python3-projects/speechrecognition/mp3totext',
)
