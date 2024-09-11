from setuptools import setup, find_packages

setup(
    name='defi-file-storage',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==2.2.2',
        'Jinja2==3.1.4',
        'MarkupSafe==2.1.5',
        'Werkzeug==3.0.4',
        'certifi==2024.8.30',
        'charset-normalizer==2.1.1',
        'click==8.1.7',
        'idna==3.8',
        'itsdangerous==2.2.0',
        'requests==2.28.1',
        'urllib3==1.26.20',
        'numpy==1.25.2'
    ],
)
