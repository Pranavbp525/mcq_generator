from setuptools import find_packages, setup

setup(
    name="mce_generator",
    version='0.0.1',
    author="Pranav Tandra",
    author_email="pranav.bp525@gmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)