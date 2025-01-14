% Facts: Define the edges in the graph
edge(a, 1).
edge(a, 3).
edge(1, 2).
edge(1, 4).
edge(3, 4).
edge(2, 5).
edge(4, 5).

% Base Case: Direct path from X to Y
path(X, Y, [X, Y]) :- 
    edge(X, Y).  % There is a direct edge from X to Y

% Recursive Case: Path from X to Y goes through Z
path(X, Y, [X | Path]) :- 
    edge(X, Z),         % There is an edge from X to Z
    path(Z, Y, Path).   % Recursive call: Find the path from Z to Y

% Queries:

% 1) Find the full path from 'a' to 5:
% ?- path(a, 5, Path).
% Path = [a, 1, 2, 5]
% Path = [a, 1, 4, 5]
% Path = [a, 3, 4, 5]

% 2) Find the full path from 'a' to 2:
% ?- path(a, 2, Path).
% Path = [a, 1, 2]

% 3) Check if there is a path from '4' to '2':
% ?- path(4, 2, Path).
% false.
