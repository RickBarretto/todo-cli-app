import setuptools
setuptools.setup(
    name='todo',
    version='0.0.1',
    scripts=['./scripts/myscript'],
    author='Me',
    description='This runs my script which is great.',
    packages=['lib.myscript']
    install_requires=[
        'setuptools'
    ],
    entry_points = {
        'console_scripts': ['todo=todo_cli_app.main:cli'],
    },
    python_requires='>=3.9'
)