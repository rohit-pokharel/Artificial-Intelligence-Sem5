% Base case: Factorial of 0 is 1
factorial(0, 1).  

% Recursive case: N! = N * (N-1)!
factorial(N, Result) :-
    N > 0,  % Ensure N is a positive integer
    N1 is N - 1,  % Decrease N by 1
    factorial(N1, Result1),  % Recursively call factorial for (N-1)
    Result is N * Result1.  % Multiply N by the factorial of (N-1) to get the result

% Query:
% ?- factorial(5, Result).
% Result = 120
