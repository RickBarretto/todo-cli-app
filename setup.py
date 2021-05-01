import setuptools
setuptools.setup(

    name='todo',
    version='0.0.6',

    author='Rick Barretto',
    author_email='pdant.mailme@protonmail.ch',
    url='https://github.com/RickBarretto/todo-cli-app',

    description='This is a TODO CLI App.',

    packages=['todo_cli_app',
    'todo_cli_app/commands',
    'todo_cli_app/commands/file'
    ],
    install_requires=[
        'setuptools'
    ],

    entry_points = {
        'console_scripts': ['todo=todo_cli_app.main:cli'],
    },

    python_requires='>=3.9',
)