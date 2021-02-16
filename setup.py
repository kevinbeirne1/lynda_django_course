from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='lynda_django_course',
    version='0.1.0',
    author="Kevin Beirne",
    description='Lynda Django Tutorial',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['django_course'],
    url='https://github.com/kevinbeirne1/lynda_django_course',
    license='MIT',
    author_email='####@example.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
