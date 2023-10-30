# 0x03. Unittests and Integration Tests
	**UnitTests...Back-end...Integration tests**

![Unit test vs.Integration test](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/f088970b450e82c881ea.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231030%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231030T183403Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b705feb041e1cbc1a81ab84ffb05de2f390aa45890c121310fc7fc8ea1bffd56)

Unit testing is the process of testing that a particular function returns expected results for different set of inputs.
A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mockded, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tsts aim to test a code path end-to-end. In general, only low level functinos that make external calls such as HTTP requests, file I/O, database I/O. etc. are mocked.
Integration tests will test interactions between every part of your code.
Execute your tests with:
```bash
$ python -m unittest path/to/test_file.py
```

## Resources
**Read or watch:**
  - [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
  - [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
  - [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
  - [parameterized](https://pypi.org/project/parameterized/)
  - [Memoization](https://en.wikipedia.org/wiki/Memoization)

Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of Google:__
  - The difference between unit and integration tests.
  - Common testing patterns such as mocking, parametrizations and fixtures

## Requirements
  - All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
  - All your files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/env python3`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Your code should use the `pycodestyle` style (version 2.5)
  - All your files must be executable
  - All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
  - All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  - All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
  - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
  - All your functions and coroutines must be type-annotated.

## Required Files

**`util.py`**
  [download](https://intranet-projects-files.s3.amazonaws.com/webstack/utils.py)
**`client.py`**
  [download](https://intranet-projects-files.s3.amazonaws.com/webstack/client.py)
**`fixtures.py`**
  [download](https://intranet-projects-files.s3.amazonaws.com/webstack/fixtures.py)
