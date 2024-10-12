import setuptools

from tgbotfilestream import __version__

try:
    long_desc = open("README.md").read()
except IOError:
    long_desc = "Failed to read README.md"

setuptools.setup(
    name="tgbotfilestream",
    version=__version__,

    description="A Telegram bot that can stream Telegram files to users over HTTP.",
    long_description=long_desc,
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages(),

    install_requires=[
        "aiohttp>=3",
        "telethon>=1.10",
        "yarl>=1",
    ],
    extras_require={
        "fast": ["cryptg>=0.2"],
    },
    python_requires="~=3.7",

    entry_points="""
        [console_scripts]
        tgbotfilestream=tgbotfilestream.__main__:main
    """,
)
