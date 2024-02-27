numberOfTentsRows(N) :- N = #sum{S, C : rowsum(C, S), line(C)}.

possibleTentPos(X+1, Y, X, Y) :- free(X, Y), tree(X+1, Y), lines(L), X < L.
possibleTentPos(X, Y+1, X, Y) :- free(X, Y), tree(X, Y+1), columns(C), Y < C.
possibleTentPos(X-1, Y, X, Y) :- free(X, Y), tree(X-1, Y), X > 0.
possibleTentPos(X, Y-1, X, Y) :- free(X, Y), tree(X, Y-1), Y > 0.

N {tentAt(X, Y) : possibleTentPos(_, _, X, Y)} N :- numberOfTentsRows(N).

% rowsum must be correct
:- rowsum(R, M), N = #count{Y: tentAt(R, Y)}, N != M.

% colsum must be correct
:- colsum(C, M), N = #count{X: tentAt(X, C)}, N != M.

% RIGHT
adjacentTent(X, Y) :- tentAt(X, Y), tentAt(X+1, Y).
% LEFT
adjacentTent(X, Y) :- tentAt(X, Y), tentAt(X-1, Y).
% BOTTOM
adjacentTent(X, Y) :- tentAt(X, Y), tentAt(X, Y+1).
% BOTTOM RIGHT
adjacentTent(X, Y) :- tentAt(X, Y), tentAt(X+1, Y+1).
% BOTTOM LEFT
adjacentTent(X, Y) :- tentAt(X, Y), tentAt(X-1, Y+1).
% TOP
adjacentTent(X, Y) :- tentAt(X, Y), tentAt(X, Y-1).
% TOP RIGHT
adjacentTent(X, Y) :- tentAt(X, Y), tentAt(X+1, Y-1).
% TOP LEFT
adjacentTent(X, Y) :- tentAt(X, Y), tentAt(X-1, Y-1).

% no adjacent tent
:- tentAt(X, Y), adjacentTent(X, Y).

% each tree has exactly 1 tent
1 {belongsTo(TREE_X, TREE_Y, TENT_X, TENT_Y) : possibleTentPos(TREE_X, TREE_Y, TENT_X, TENT_Y)} 1 :- 
    tentAt(TENT_X, TENT_Y).

:- tree(X, Y), not belongsTo(X, Y, _, _).

#show tentAt/2.