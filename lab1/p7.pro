% Base cases:
% Fibonacci of 0 is 0.
fib(0, 0).

% Fibonacci of 1 is 1.
fib(1, 1).

% Recursive case: Fibonacci of N is the sum of Fibonacci of N-1 and N-2.
fib(N, Result) :-
    N > 1,  % Ensure N is greater than 1.
    N1 is N - 1,  % N-1 for the recursive call.
    N2 is N - 2,  % N-2 for the recursive call.
    fib(N1, Result1),  % Recursive call to get fib(N-1).
    fib(N2, Result2),  % Recursive call to get fib(N-2).
    Result is Result1 + Result2.  % Sum of fib(N-1) and fib(N-2).

% Predicate to print Fibonacci series up to N terms.
print_fibonacci_series(N) :-
    print_fibonacci_series(0, N).  % Start from term 0 up to N.

% Helper predicate to print Fibonacci series from 0 to N.
print_fibonacci_series(Current, N) :-
    Current =< N,  % Ensure that the current term is less than or equal to N.
    fib(Current, Result),  % Get the Fibonacci result for the current term.
    format('~w ', [Result]),  % Print the result for the current term.
    Next is Current + 1,  % Increment the current term.
    print_fibonacci_series(Next, N).  % Recursive call for the next term.

% Base case for the printing predicate when Current is greater than N.
print_fibonacci_series(Current, N) :-
    Current > N.  % Stop printing when Current exceeds N.

% Query:
% ?- print_fibonacci_series(5).
% 0 1 1 2 3 5
