from setuptools import setup
setup(
    name='torch_mr',
    version='0.1.0',
    description='A Python Package for PyTorch Monitoring',
    url='https://github.com/ian-coccimiglio/torch_mr',
    author='Ian Coccimiglio',
    author_email='icoccimi@gmail.com',
    license='MIT',
    python_requires='>3.5.0',
    packages=['torch_mr'],
    install_requires=['torch'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
