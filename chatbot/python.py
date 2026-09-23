
python = [
    (
        r"(?:what is|explain) python[?.! ]*", 
            "Python is a general-purpose programming language widely used in automation, web services, data work, and ML."
    ),
    (
        r"(?:what is|explain) (?:a )?list[?.! ]*", 
            "A list is a mutable, ordered sequence written with square brackets."
    ),
    (
        r"(?:what is|explain) (?:a )?tuple[?.! ]*", 
            "A tuple is an immutable, ordered sequence."
    ),
    (
        r"(?:what is|explain) (?:a )?dictionary[?.! ]*", 
            "A dictionary maps hashable keys to values."
    ),
    (
        r"(?:what is|explain) (?:a )?set[?.! ]*", 
            "A set stores unique hashable values and supports fast average-case membership checks."
    ),
    (
        r"(?:what is|explain) (?:a )?generator[?.! ]*", 
            "A generator yields values as needed instead of building the full result in memory."
    ),
    (
        r"(?:what is|explain) (?:an )?iterator[?.! ]*", 
            "An iterator provides items one at a time through its next operation."
    ),
    (
        r"(?:what is|explain) (?:a )?decorator[?.! ]*", 
            "A decorator wraps a function or class to extend behavior without editing its body."
    ),
    (
        r"(?:what is|explain) (?:a )?context manager[?.! ]*", 
            "A context manager sets up and cleans up resources around a with block."
    ),
    (
        r"(?:what is|explain) (?:a )?virtual environment[?.! ]*", 
            "A virtual environment isolates a project's Python packages from other projects."
    ),
    (
        r"(?:what is|explain) pip[?.! ]*", 
            "pip installs Python packages into an environment."
    ),
    (
        r"(?:what is|explain) (?:a )?type hint[?.! ]*", 
            "A type hint describes an expected type for tools and readers; Python does not enforce most hints at runtime."
    ),
    (
        r"(?:what is|explain) (?:an )?exception[?.! ]*", 
            "An exception signals an error or unusual condition that code can handle with try and except."
    ),
    (
        r"(?:what is|explain) (?:a )?comprehension[?.! ]*", 
            "A comprehension builds a collection from an iterable using concise expression syntax."
    ),
    (
        r"(?:what is|explain) (?:a )?lambda[?.! ]*", 
            "A lambda is a small anonymous function defined as an expression."
    ),
    (
        r"(?:what is|explain) (?:a )?dataclass[?.! ]*", 
            "A dataclass creates common data-object methods such as an initializer from declared fields."
    ),
    (
        r"(?:what is|explain) (?:a )?module[?.! ]*", 
            "A module is a Python file whose definitions can be imported elsewhere."
    ),
    (
        r"(?:what is|explain) (?:a )?package[?.! ]*", 
            "A package organizes importable Python modules under a namespace."
    ),
    (
        r"(?:what is|explain) (?:a )?unit test[?.! ]*", 
            "A unit test checks a small piece of behavior under controlled inputs."
    ),
    (
        r"(?:what is|explain) pytest[?.! ]*", 
            "pytest is a Python testing framework that discovers tests and provides assertions and fixtures."
    ),
    (
        r"(?:what is|explain) (?:a )?fixture[?.! ]*", 
            "A pytest fixture provides reusable setup or test data to tests."
    ),
    (
        r"(?:what is|explain) async(?:io)?[?.! ]*", 
            "Async code allows tasks to yield while waiting for operations such as network I/O."
    ),
    (
        r"(?:what is|explain) (?:the )?gil[?.! ]*", 
            "In typical CPython builds, the Global Interpreter Lock limits simultaneous execution of Python bytecode by threads."
    ),
    (
        r"(?:what is|explain) (?:the )?difference between (?:a )?list and (?:a )?tuple[?.! ]*", 
            "Lists are mutable; tuples are immutable. Both preserve order."
    ),
]

