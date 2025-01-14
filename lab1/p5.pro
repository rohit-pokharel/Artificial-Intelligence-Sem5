% Base case: When the counter reaches 11, stop the recursion.
% The cut operator (!) ensures no backtracking happens here once we reach the limit.
print_multiplication_table(_, 11) :- 
    !. % Stop recursion when counter reaches 11.

% Recursive case: Print the multiplication result of N and the current counter (from 1 to 10).
% After printing, increment the counter and call the function recursively.
print_multiplication_table(N, Counter) :-
    Result is N * Counter, % Calculate the multiplication result (N * Counter).
    format('~w * ~w = ~w~n', [N, Counter, Result]), % Print the result in the format "N * Counter = Result".
    NextCounter is Counter + 1, % Increment the counter by 1.
    print_multiplication_table(N, NextCounter). % Recursively call the predicate with the incremented counter.

% Wrapper Predicate: This predicate is called to start printing the multiplication table for a number N.
% It initializes the recursion by starting with the counter 1.
multiplication_table(N) :-
    print_multiplication_table(N, 1). % Start the recursion with the counter set to 1.


% Query:
% ?- multiplication_table(5).
% 5 * 1 = 5
% 5 * 2 = 10
% 5 * 3 = 15
% 5 * 4 = 20
% 5 * 5 = 25
% 5 * 6 = 30
% 5 * 7 = 35
% 5 * 8 = 40
% 5 * 9 = 45
% 5 * 10 = 50
