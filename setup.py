import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requires = f.read().splitlines()

setuptools.setup(
    name="ondewo-nlu-client-python",
    version="1.0.1",
    author="Ondewo GbmH",
    author_email="info@ondewo.com",
    description="This library facilitates the interaction between a user and his/her CAI server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ondewo/ondewo-nlu-client-python",
    packages=[
        np
        for np in filter(
            lambda n: n.startswith('ondewo.') or n == 'ondewo',
            setuptools.find_namespace_packages()
        )
    ],
    package_data={
        'ondewo.nlu': ['py.typed']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.0.1',
    install_requires=requires,
)
