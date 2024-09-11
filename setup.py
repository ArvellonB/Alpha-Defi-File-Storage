from setuptools import setup, find_packages

setup(
    name='defi-file-storage',
    version='0.1',
    description='A blockchain-based file storage solution',
    long_description=open('README.md').read(),  # Ensure you have a README.md file for this
    long_description_content_type='text/markdown',
    author='Arvellon Ballard',
    author_email='your.email@example.com',  # Replace with your email
    url='https://github.com/ArvellonB/Defi-File-Storage',  # Replace with your project's URL
    packages=find_packages(),
    install_requires=[
        'certifi==2024.8.30',
        'charset-normalizer==2.1.1',
        'click==8.1.7',
        'Flask==2.2.2',
        'idna==3.8',
        'itsdangerous==2.2.0',
        'Jinja2==3.1.4',
        'MarkupSafe==2.1.5',
        'numpy==1.25.2',
        'requests==2.28.1',
        'urllib3==1.26.20',
        'Werkzeug==3.0.4',
    ],
    python_requires='>=3.7',  # Adjust according to your Python version compatibility
)
