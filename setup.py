from setuptools import setup, find_packages

with open("README.md", "utf-8") as fh:
    long_description = fh.read()
setup(
    name="cli-todo-app",
    version="0.1.0",
    author="Afnan Sukri Anwar Abdullah",
    author_email="afnan.sukri_anwar_abdullah.ay3@g.ext.naist.jp",
    description="CLI Todo Application for SSD 6th Assignment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Afnanaz/cli-todo-app",
    py_modules=["todo"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "todo=todo:main",
        ],
    }
)