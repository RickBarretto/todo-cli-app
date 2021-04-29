import setuptools
setuptools.setup(
    name='todo',
    version='0.0.1',
    author='Me',
    description='This runs my script which is great.',
    packages=['todo_cli_app'],
    install_requires=[
        'setuptools'
    ],
    entry_points = {
        'console_scripts': ['todo=todo_cli_app.main:cli'],
    },
    python_requires='>=3.9'
)