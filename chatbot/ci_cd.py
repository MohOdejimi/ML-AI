cicd = [
    (
        r"(?:what is|explain) ci[?.! ]*", 
            "Continuous integration automatically checks changes, often with linting and tests, when code is merged or pushed."
    ),
    (
        r"(?:what is|explain) cd[?.! ]*", 
            "Continuous delivery keeps software ready to release; continuous deployment automatically releases passing changes."
    ),
    (
        r"(?:what is|explain) ci[/ -]?cd[?.! ]*", 
            "CI/CD automates verification and the path from a code change to a releasable or deployed build."
    ),
    ( 
        r"(?:what is|explain) (?:a )?pipeline[?.! ]*", 
            "A pipeline is an automated sequence of checks, builds, and release steps."
    ),
    (
        r"(?:what is|explain) (?:a )?runner[?.! ]*", 
            "A runner is the machine or service that executes pipeline jobs."
    ),
    (
        r"(?:what is|explain) (?:a )?job[?.! ]*", 
            "A job is a group of pipeline steps executed in a runner environment."
    ),
    (
        r"(?:what is|explain) (?:a )?workflow[?.! ]*", 
            "A workflow defines when automation runs and which jobs it performs."
    ),
    (
        r"(?:what is|explain) (?:an )?artifact[?.! ]*", 
            "An artifact is an output of a build or job, such as a test report or compiled package."
    ),
]