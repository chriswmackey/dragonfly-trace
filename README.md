# dragonfly-trace
[![Build Status](https://github.com/ladybug-tools/dragonfly-trace/workflows/CI/badge.svg)](https://github.com/ladybug-tools/dragonfly-trace/actions)
[![Python 3.10](https://img.shields.io/badge/python-3.10-orange.svg)](https://www.python.org/downloads/release/python-3100/)
[![IronPython](https://img.shields.io/badge/ironpython-2.7-red.svg)](https://github.com/IronLanguages/ironpython2/releases/tag/ipy-2.7.8/)

![Dragonfly](https://www.ladybug.tools/assets/img/dragonfly.png) <img src="https://global.discourse-cdn.com/sketchup/optimized/3X/9/9/99fa74426b043e577069fadc8ef493f3a399c1ff_2_500x500.jpeg" width="200" height="200">

Dragonfly extension for translation to Trane TRACE.

## Installation

`pip install -U dragonfly-trace`

## QuickStart

```console
import dragonfly_trace
```

## [API Documentation](http://ladybug-tools.github.io/dragonfly-trace/docs)

## Local Development

1. Clone this repo locally
```console
git clone git@github.com:ladybug-tools/dragonfly-trace

# or

git clone https://github.com/ladybug-tools/dragonfly-trace
```
2. Install dependencies:
```
cd dragonfly-trace
pip install -r dev-requirements.txt
pip install -r requirements.txt
```

3. Run Tests:
```console
python -m pytest tests/
```

4. Generate Documentation:
```console
sphinx-apidoc -f -e -d 4 -o ./docs ./dragonfly_trace
sphinx-build -b html ./docs ./docs/_build/docs
```