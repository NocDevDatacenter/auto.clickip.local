from setuptools import setup, find_packages


def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="auto_clickip",
    version="0.1.0",
    description="Aplicação Flask para automação de redes",
    author="Fábio Ewerton",
    author_email="fabioew89@gmail.com",
    url="https://github.com/fabioew89/auto.clickip.local",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),  # Pegando as dependências do requirements.txt
    entry_points={
        "console_scripts": [
            "auto-clickip=app.run:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
