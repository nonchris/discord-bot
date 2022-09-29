import re

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')
with open(here / "requirements.txt", "r") as f:
    dependencies = f.readlines()

with open('src/discord_bot/version.py') as f:
    version = re.search(r'VERSION\s*=\s*\"((\w+\.?)+)', f.read(), re.MULTILINE).group(1)

setup(
    # TODO: Adjust your project information here
    name='discord_bot',
    version=version,
    description='A discord bot template',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nonchris/discord-bot',
    author='nonchris',
    author_email='info@nonchris.eu',

    project_urls={
        'Bug Reports': 'https://github.com/nonchris/discord-bot/issues',
        'Source': 'https://github.com/https://github.com/nonchris/discord-bot',
    },

    keywords='discord-bot',

    python_requires='>=3.8, <4',

    install_requires=dependencies,

    classifiers=[

        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        'Intended Audience :: Other Audience',
        'Topic :: Communications :: Chat',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',

        'Typing :: Typed',
    ],

    package_dir={'': 'src'},

    packages=find_packages(where='src'),

    entry_points={
        'console_scripts': [
            'discord-bot=discord_bot:main',
        ],
    },
)
