Python program does not need to be compiled before execution.

'''
In Python, programs don’t need to be manually compiled before execution in the way that languages like C or Java require. 
Instead, Python uses an interpreter that compiles code behind the scenes, making Python a "just-in-time" (JIT) compiled language.

Here's how it works in Python:

1. Source Code to Bytecode: When you run a Python script, the Python interpreter first compiles the source code (.py file) into bytecode. 
This bytecode is a lower-level, platform-independent representation of your code, which Python can execute more efficiently.

2. Bytecode Execution: The Python interpreter then runs this bytecode on the Python Virtual Machine (PVM), executing the instructions line-by-line. 
This step is where your program actually runs and produces output.

3. Caching in .pyc Files: To speed up future executions, Python often saves the compiled bytecode as .pyc files in a __pycache__ directory. 
The next time you run the same program, Python can use the cached bytecode instead of recompiling.

So while Python does compile code to bytecode before execution, this process is handled automatically by the interpreter, 
and you typically don’t need to explicitly compile Python code like in statically compiled languages.
'''
