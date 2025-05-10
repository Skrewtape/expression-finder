# Expresison Finder

A simple application to explore the space of mathemtical expressions constructed by composing
a number of "interesting" functions applied to a set of "interesting" numbers.

The algorithm will use each known operation and input value at most once per expression, which
limits the size of the search space and maximizes the "interestingness" of the resulting
expressions. Any expression that evaluates to a number in the designated range will be printed
to the console.

Due to the terribleness of the implementation, it can take a while to run, so be patient.

To run the application, execute `python find.py <min> <max>` where `<min>` and `<max>` define
the bounds of the target range.

For example, running `python find.py 1 100` will result in output like this:

```
(√(π))^(|(-4) + (e)|) = 2.0825863277465793                  
(√3)^(|(-4) + (ζ(−1))|) = 9.42155443552865               
(|(-5) + (Γ(2))|)^((ln(7)) / (11)) = 1.277923827820499      
```

I built this project to help come up with the design for a
(t-shirt)[https://www.teepublic.com/t-shirt/74788750-math].

# Additional Work

There's a lot of room for improvement here. Some ideas include:

- Performance optimization. Right now, I just sprinkled in some `lru_cache` decorators
  and called it a day. The runtime is completely CPU=bound, which makes using async pythong
  not particularly useful. There might be something to be done with multiprocessing, but
  it's probably not worth the effort.
- We could be a little smarter about where we put parentheses. The current implementation
  adds them everywhere to avoid all ambiguity, but the result could be a little bit nicer
  with some TLC.
- Better output for LaTeX or Wolfram Alpha.  Alpha is forgiving enough to (mostly) accept
  the current output (probably,) but it could stil be improved. LaTeX output should be
  fairly straightforward, but I don't feel like doing it right now.
- Some kind of branch triming logic to save time exploring branches that are doomed to
  fail. Some of the functions are too chatoic to predict, but others are fairly well-behaved
  and can probably give some opportunity for pruning.

Patches are always welcome, but keep in mind that I will definitely judge anyone who chooses
to contribute to this project. I mean, come on.
