% Facts: Define direct friendships
friend(rikesh, nikesh).
friend(nikesh, bikash).
friend(rikesh, bikash).
friend(rita, nita).
friend(nita, gita).

% Recursive Rule: A person X is a friend of person Y if:
% - X is directly friends with Y, or
% - X is friends with Z, and Z is a friend of Y.
friendship(X, Y) :- 
    friend(X, Y).  % Direct friendship
    
friendship(X, Y) :- 
    friend(X, Z),   % X is friends with Z
    friendship(Z, Y), % Z is friends with Y (indirect friendship)
    X \= Y.          % X and Y should not be the same person

% Queries:

% 1) Basic: Find all direct friendships (X and Y are directly friends):
% ?- friend(X, Y).
% Output:
% X = rikesh, Y = nikesh ;
% X = nikesh, Y = rikesh ;
% X = nikesh, Y = bikash ;
% X = bikash, Y = nikesh ;
% X = rikesh, Y = bikash ;
% X = bikash, Y = rikesh ;
% X = rita, Y = nita ;
% X = nita, Y = rita ;
% X = nita, Y = gita ;
% X = gita, Y = nita ;

% 2) Query: Find all people who are friends with rikesh (direct or indirect):
% ?- friendship(rikesh, Y).
% Output:
% Y = nikesh ;
% Y = bikash ;

% 3) Query: Check if rikesh and gita are friends (direct or indirect):
% ?- friendship(rikesh, gita).
% Output:
% true.

% 4) Query: Find all friends of nikesh (direct or indirect):
% ?- friendship(nikesh, Y).
% Output:
% Y = rikesh ;
% Y = bikash ;

% 5) Query: Check if rikesh and rita are friends (direct or indirect):
% ?- friendship(rikesh, rita).
% Output:
% false.

% 6) Query: Check if rikesh is friends with nita (direct or indirect):
% ?- friendship(rikesh, nita).
% Output:
% true.

% 7) Query: Check if gita is a friend of rikesh (direct or indirect):
% ?- friendship(rikesh, gita).
% Output:
% true.

% 8) Query: Check if bikash and gita are friends (direct or indirect):
% ?- friendship(bikash, gita).
% Output:
% true.

% 9) Query: Check if rikesh and nita are friends (direct or indirect):
% ?- friendship(rikesh, nita).
% Output:
% true.

