part(r).
part(l).

%select a transformation index for each pentomino
{selected(A, N) : shape(A, N, _, _)} = 1 :- letter(A).

%for all pentominoes, choose a case and a side of the grid
{place(A, X, Y, D) : letter(A), X=1..6-X1, Y=1..5-Y1, part(D), max_column_selected(A, N, Y1), max_row_selected(A, N, X1), selected(A, N)} = 1 :- letter(A).

%fill the grid with the selected pentominoes
{case(X, Y, A, D) :  shape(A, N, X1, Y1), selected(A, N), X=I+X1, Y=J+Y1}=5 :- place(A, I, J, D).

%adding constraint 

%adding constraint for the pentominoes to be placed in the grid
:- case(X, Y, A, D), case(X, Y, B, D), A != B.

#show case/4.


