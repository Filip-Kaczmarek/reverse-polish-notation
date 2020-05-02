# reverse-polish-notation
This is a simple program to read formula of predicate calculus in reverse polish notation (RPN)
and then print them in standard bracket notation, which is more natural to read by humans.
Examples of input and the expected output:
  1. input: 'a p/1',
     output: 'p(a)'
  2. input: 'Z Z p/1 EXISTS',
     output: '(EXISTS Z p(Z))
  3. input: 'Z X X a f/2 p/1 ∃ Y Y Z f/1 p/2 FORALL → FORALL',
     output: '(FORALL Z ((∃ X p(f(X, a))) → (FORALL Y p(Y, f(Z)))))'
  4. input: 'Z Y X X b c q/3 Z Y f/1 p/2 ~ & EXISTS FORALL EXISTS',
     output: '(EXISTS Z (FORALL Y (EXISTS X (q(X, b, c) & (~ p(Z, f(Y)))))))'
