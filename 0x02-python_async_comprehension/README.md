
0x02. Python - Async Comprehension
==================================

PythonBack-end

*   Weight: 1
*   Project will start Aug 20, 2024 6:00 AM, must end by Aug 21, 2024 6:00 AM
*   Checker was released at Aug 20, 2024 12:00 PM
*   An auto review will be launched at the deadline

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/ee85b9f67c384e29525b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240820T234834Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=71a06e95fcb95c04d062e498361f28228e3fc506c672fc64e427ed0f103ef9aa)

Resources
---------

**Read or watch**:

*   [PEP 530 – Asynchronous Comprehensions](/rltoken/hlwtED-iLsdORSgly8DsyQ "PEP 530 -- Asynchronous Comprehensions")
*   [What’s New in Python: Asynchronous Comprehensions / Generators](/rltoken/0OkbObYzCKtO7ZUAxfKvkw "What’s New in Python: Asynchronous Comprehensions / Generators")
*   [Type-hints for generators](/rltoken/l4Fnno568VbVIn9GvrFVtQ "Type-hints for generators")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/_jK22HqiCeh5NjKJ4ZHBww "explain to anyone"), **without the help of Google**:

*   How to write an asynchronous generator
*   How to use async comprehensions
*   How to type-annotate generators

Requirements
------------

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/env python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `pycodestyle` style (version 2.5.x)
*   The length of your files will be tested using `wc`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   All your functions and coroutines must be type-annotated.

Tasks
-----

### 0\. Async Generator

mandatory

Write a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the `random` module.

    bob@dylan:~$ cat 0-main.py
    #!/usr/bin/env python3
    
    import asyncio
    
    async_generator = __import__('0-async_generator').async_generator
    
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)
    
    asyncio.run(print_yielded_values())
    
    bob@dylan:~$ ./0-main.py
    [4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
    

**Repo:**

*   GitHub repository: `alx-backend-python`
*   Directory: `0x02-python_async_comprehension`
*   File: `0-async_generator.py`

Done?! Check your code

×

#### Correction of "0. Async Generator"

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

### 1\. Async Comprehensions

mandatory

Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

    bob@dylan:~$ cat 1-main.py
    #!/usr/bin/env python3
    
    import asyncio
    
    async_comprehension = __import__('1-async_comprehension').async_comprehension
    
    
    async def main():
        print(await async_comprehension())
    
    asyncio.run(main())
    
    bob@dylan:~$ ./1-main.py
    [9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]
    
    

**Repo:**

*   GitHub repository: `alx-backend-python`
*   Directory: `0x02-python_async_comprehension`
*   File: `1-async_comprehension.py`

Done?! Check your code

×

#### Correction of "1. Async Comprehensions"

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

### 2\. Run time for four parallel comprehensions

mandatory

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.

`measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

    bob@dylan:~$ cat 2-main.py
    #!/usr/bin/env python3
    
    import asyncio
    
    
    measure_runtime = __import__('2-measure_runtime').measure_runtime
    
    
    async def main():
        return await(measure_runtime())
    
    print(
        asyncio.run(main())
    )
    
    bob@dylan:~$ ./2-main.py
    10.021936893463135
    
    

**Repo:**

*   GitHub repository: `alx-backend-python`
*   Directory: `0x02-python_async_comprehension`
*   File: `2-measure_runtime.py`

Done?! Check your code

×

#### Correction of "2. Run time for four parallel comprehensions"

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
