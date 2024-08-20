

0x01. Python - Async
====================

PythonBack-end

*   Weight: 1
*   Project will start Aug 19, 2024 6:00 AM, must end by Aug 20, 2024 6:00 AM
*   Checker was released at Aug 19, 2024 12:00 PM
*   An auto review will be launched at the deadline

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/4aeaa9c3cb1f316c05c4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240819T151548Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6c0f851d273084cb4d9c2f64f5a81c9dc2bbefa53c8c5dfe7255f02cf052279c)

Resources
---------

**Read or watch**:

*   [Async IO in Python: A Complete Walkthrough](/rltoken/zYkXScziW1D5rNdNEvObjQ "Async IO in Python: A Complete Walkthrough")
*   [asyncio - Asynchronous I/O](/rltoken/aZUO4GiWHbPIrVBIwptFAw "asyncio - Asynchronous I/O")
*   [random.uniform](/rltoken/72mVf1s8rx2ih_U2WjBmaA "random.uniform")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/RzzuxS2J7-SysSxP0Hu3cA "explain to anyone"), **without the help of Google**:

*   `async` and `await` syntax
*   How to execute an async program with `asyncio`
*   How to run concurrent coroutines
*   How to create `asyncio` tasks
*   How to use the `random` module

Requirements
------------

### General

*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
*   All your files should end with a new line
*   All your files must be executable
*   The length of your files will be tested using `wc`
*   The first line of all your files should be exactly `#!/usr/bin/env python3`
*   Your code should use the `pycodestyle` style (version 2.5.x)
*   All your functions and coroutines must be type-annotated.
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Tasks
-----

### 0\. The basics of async

mandatory

Write an asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it.

Use the `random` module.

    bob@dylan:~$ cat 0-main.py
    #!/usr/bin/env python3
    
    import asyncio
    
    wait_random = __import__('0-basic_async_syntax').wait_random
    
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
    
    bob@dylan:~$ ./0-main.py
    9.034261504534394
    1.6216525464615306
    10.634589756751769
    

**Repo:**

*   GitHub repository: `alx-backend-python`
*   Directory: `0x01-python_async_function`
*   File: `0-basic_async_syntax.py`

Done?! Check your code

×

#### Correction of "0. The basics of async"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 1\. Let's execute multiple coroutines at the same time with async

mandatory

Import `wait_random` from the previous python file that you’ve written and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified `max_delay`.

`wait_n` should return the list of all the delays (float values). The list of the delays should be in ascending order without using `sort()` because of concurrency.

    bob@dylan:~$ cat 1-main.py
    #!/usr/bin/env python3
    '''
    Test file for printing the correct output of the wait_n coroutine
    '''
    import asyncio
    
    wait_n = __import__('1-concurrent_coroutines').wait_n
    
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
    
    bob@dylan:~$ ./1-main.py
    [0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
    [0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    

The output for your answers might look a little different and that’s okay.

**Repo:**

*   GitHub repository: `alx-backend-python`
*   Directory: `0x01-python_async_function`
*   File: `1-concurrent_coroutines.py`

Done?! Check your code

×

#### Correction of "1. Let's execute multiple coroutines at the same time with async"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 2\. Measure the runtime

mandatory

From the previous file, import `wait_n` into `2-measure_runtime.py`.

Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. Your function should return a float.

Use the `time` module to measure an approximate elapsed time.

    bob@dylan:~$ cat 2-main.py
    #!/usr/bin/env python3
    
    measure_time = __import__('2-measure_runtime').measure_time
    
    n = 5
    max_delay = 9
    
    print(measure_time(n, max_delay))
    
    bob@dylan:~$ ./2-main.py
    1.759705400466919
    

**Repo:**

*   GitHub repository: `alx-backend-python`
*   Directory: `0x01-python_async_function`
*   File: `2-measure_runtime.py`

Done?! Check your code

×

#### Correction of "2. Measure the runtime"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 3\. Tasks

mandatory

Import `wait_random` from `0-basic_async_syntax`.

Write a function (do not create an async function, use the regular function syntax to do this) `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task`.

    bob@dylan:~$ cat 3-main.py
    #!/usr/bin/env python3
    
    import asyncio
    
    task_wait_random = __import__('3-tasks').task_wait_random
    
    
    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)
    
    asyncio.run(test(5))
    
    bob@dylan:~$ ./3-main.py
    <class '_asyncio.Task'>
    

**Repo:**

*   GitHub repository: `alx-backend-python`
*   Directory: `0x01-python_async_function`
*   File: `3-tasks.py`

Done?! Check your code

×

#### Correction of "3. Tasks"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 4\. Tasks

mandatory

Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.

    bob@dylan:~$ cat 4-main.py
    #!/usr/bin/env python3
    
    import asyncio
    
    task_wait_n = __import__('4-tasks').task_wait_n
    
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
    
    bob@dylan:~$ ./4-main.py
    [0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
    

**Repo:**

*   GitHub repository: `alx-backend-python`
*   Directory: `0x01-python_async_function`
*   File: `4-tasks.py`

Done?! Check your code

×

#### Correction of "4. Tasks"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

×

#### Recommended Sandbox

Running only

### 1 image(1/2 Sandboxes spawned)

### Ubuntu 18.04 - Python 3.7

Ubuntu 18.04 with Python 3.7

SSH

SFTP

[Webterm](/user_containers/695952/webterm)

RestartDestroy

#### Credentials

**Host**037ca4a30544.5dabdd76.alx-cod.online

**Username**037ca4a30544

**Password**e495a801affd2dbc8aab

#### Web access

[HTTP](http://037ca4a30544.5dabdd76.alx-cod.online)[3000](http://037ca4a30544.5dabdd76.alx-cod.online:3000)[4000](http://037ca4a30544.5dabdd76.alx-cod.online:4000)[5000](http://037ca4a30544.5dabdd76.alx-cod.online:5000)[5001](http://037ca4a30544.5dabdd76.alx-cod.online:5001)[8000](http://037ca4a30544.5dabdd76.alx-cod.online:8000)[8080](http://037ca4a30544.5dabdd76.alx-cod.online:8080)

#### Port mapping

**SSH**32983

**HTTP**32982

**3000**32981

**4000**32980

**5000**32979

**5001**32978

**8000**32977

**8080**32976

Copyright © 2024 ALX, All rights reserved.

×

#### Markdown Guide

#### Emphasis

\*\***bold**\*\*
\*_italics_\*
~~strikethrough~~

#### Headers

\# Big header
## Medium header
### Small header
#### Tiny header

#### Lists

\* Generic list item
\* Generic list item
\* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item

#### Links

\[Text to display\](http://www.example.com)

#### Quotes

\> This is a quote.
> It can span multiple lines!

#### Images

CSS style available: `width, height, opacity`

!\[\](http://www.example.com/image.jpg)
!\[\](http://www.example.com/image.jpg | width: 200px)
!\[\](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)

#### Tables

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

_Or without aligning the columns..._

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |

#### Displaying code

\`var example = "hello!";\`

_Or spanning multiple lines..._

\`\`\`
var example = "hello!";
alert(example);
\`\`\`
