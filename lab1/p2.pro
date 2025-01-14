% Facts: Define genders
male(rikesh).
male(nikesh).
male(bikash).

female(rita).
female(nita).
female(gita).

% Facts: Define sibling relationships
sibling(rikesh, nikesh).
sibling(rita, nita).
sibling(bikash, rita).

% Facts: Define spouse relationships
spouse(rikesh, nita).
spouse(nikesh, rita).
spouse(bikash, gita).

% Rule: Brother-in-law
% A person X is a brother-in-law of Y if:
% - X is the sibling of Y's spouse, or
% - X is the spouse of Y's sibling.
brother_in_law(X, Y) :- 
    male(X),
    (
        (sibling(X, Z), spouse(Y, Z));  % X is sibling of Y's spouse
        (spouse(X, Z), sibling(Z, Y))  % X is spouse of Y's sibling
    ).

% Rule: Sister-in-law
% A person X is a sister-in-law of Y if:
% - X is the sibling of Y's spouse, or
% - X is the spouse of Y's sibling.
sister_in_law(X, Y) :- 
    female(X),
    (
        (sibling(X, Z), spouse(Y, Z));  % X is sibling of Y's spouse
        (spouse(X, Z), sibling(Z, Y))  % X is spouse of Y's sibling
    ).

% Queries:

% 1) Basic: Find all brothers-in-law (pairs of X and Y):
% ?- brother_in_law(X, Y).
% X = nikesh,
% Y = nita
% X = bikash,
% Y = nikesh
%
% 2) Basic: Find all sisters-in-law (pairs of X and Y):
% ?- sister_in_law(X, Y).
% X = rita,
% Y = rikesh
%
% 3) Specific: Check if nikesh is brother-in-law of rikesh:
% ?- brother_in_law(nikesh, rikesh).
% false
%
% 4) Specific: Check if bikash is brother-in-law of nikesh:
% ?- brother_in_law(bikash, nikesh).
% true
%
% 5) Specific: Check if rita is the sister-in-law of rikesh:
% ?- sister_in_law(rita, rikesh).
% true
