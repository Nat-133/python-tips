# Readme
This repository is an odd collection of examples.
Treat it as a reference, the actual examples aren't that realistic, but should be decent proof of concepts.

Many of the examples are of anti-patterns. They should be clearly labeled.


A lot of the examples use Jupyter Notebooks to interleave markdown and code, and allow the running of individual code segments.

To use these in intellij, you will need the Jupyter extension, alternatives are available for most other IDEs.


## How to setup a python project
### Overview
An example project structure:
```
git_root_folder
|- requirements.txt
|- test_requirements.txt    # first line should be: -r requirements.txt
|- dockerfile
|- .venv/
`- python_package/
    |- __init__.py
    |- __main__.py          # the entrypoint, contains a single function call
    |- src/                 # or main, etc... personal choice
    |   |- __init__.py
    |   `- sourcecode
    `- test/
        |- __init__.py
        `- tests
```
You would run this with `python -m python_package`, ensuring `python_package` is in the `PYTHONPATH` (probably by having `git_root_folder` as the working directory).

This is only one way of doing things, there are a few others. However, if you are unsure what to setup, just follow the above. I have never had any issues with it.


### Steps
I will reference the above example project, replace specific names with your project's terms.
1. create a new python project in intellij
2. create your python package as a subdirectory (`python_package/`)
3. create at least `src/` and `test/` packages in `python_package/`
   - a python package is a directory with `__init__.py` in it
   - if there is no `__init__.py` in a directory, imports may still work, but if the same namespace appears anywhere else in `PYTHONPATH`, then you may not be referencing what you intend. You are defining a namespace package if there is no `__init__.py`, don't do this unless it's intentional.
4. create `__main__.py` in `python_package/` this is the entrypoint into your module
5. create requirements.txt in `git_root_folder/`
6. create test_requirements.txt in `git_root_folder`. The first line should be `-r requirements.txt`
   - this recursively references all the requirements in `requirements.txt`
7. Configure project sdk. In intellij, go to `project settings > project > SDK > edit` create new virtual environment for this project.
   - a venv (python virtual environment) is a copy of the python binaries and a location to put all the dependencies of the project so it doesn't affect the main python install
   - it can be created manually with `python -m venv desired/path/to/.venv`
8. run your project with `python -m python_package`

#### Note. Unless you know what you're doing, all imports should be absolute from the top level package, e.g.
`from python_package.src.dolphin import paddy`
