% Facts: Define genders
male(nikesh).
male(rikesh).
male(bikash).

female(rita).
female(nita).
female(gita).

% Facts: Define who loves whom
loves(nikesh, rita).
loves(rikesh, nita).
loves(bikash, rita).

% Rule: Jealousy
% A person X is jealous of person Y if X loves Z, Y loves Z, X and Y are not the same, and Z is of opposite gender.
jealous(X, Y) :-
    loves(X, Z),
    loves(Y, Z),
    X \= Y,
    (
        (male(X), female(Z));
        (female(X), male(Z))
    ).

% Queries:
%
% 1) Basic: find all pairs of jealous persons:
% ?- jealous(X, Y).
% X = nikesh,
% Y = bikash
% X = bikash,
% Y = nikesh
%
% 2) Specific: check if nikesh is jealous of bikash:
% ?- jealous(nikesh, bikash).
% true
%
% and if nikesh is jealous of rikesh:
% ?- jealous(nikesh, rikesh).
% false
%
% 3) Specific Target: check who nikesh is jealous of:
% ?- jealous(nikesh, Y).
% Y = bikash
