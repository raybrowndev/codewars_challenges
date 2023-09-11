#DESCRIPTION

# The open/closed principle states that code should be closed for modification, yet open for extension. That means you should be able to add new functionality to an object or method without altering it.

# One way to achieve this is by using a lambda, which by nature is lazily bound to the lexical context. Until you call a lambda, it is just a piece of data you can pass around.

# Task at hand
# Implement 3 lambdas that alter a message based on emotion:

# spoken    = lambda greeting: ... # "hello WORLD" --> "Hello world."
# shouted   = lambda greeting: ... # "Hello world" --> "HELLO WORLD!"
# whispered = lambda greeting: ... # "HELLO WORLD" --> "hello world."
# Then create a fourth lambda, this one will take one of the above lambdas and a message, and the last lambda will delegate the emotion and the message up the chain.

# greet = lambda style, msg: ...

spoken    = lambda greeting: f"{greeting.capitalize()}."
shouted   = lambda greeting: f"{greeting.upper()}!"
whispered = lambda greeting: f"{greeting.lower()}."

greet = lambda style, msg: style(msg)

