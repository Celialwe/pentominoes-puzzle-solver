
part(r).
part(l).

{selected(A, N) : shape(A, N, _, _)} = 1 :- letter(A).

%for all pentominoes, choose a case and a side of the grid

%place t on the left side of the grid
{place(t, X, Y, l) :  X=1..6-X1, Y=1..2, max_row_selected(t, N, X1), selected(t, N), N!=2; place(t, X, Y, l) :  X=1..3, Y=1..2, max_row_selected(t, N, X1), selected(t, N), N=2} = 1.
{place(u, X, Y, D) :  X=1..6-X1, Y=1..2, max_row_selected(u, N, X1), selected(u, N), part(D), N=2; place(u, X, Y, D) :  X=1..3, Y=1..2, max_row_selected(u, N, X1), selected(u, N),part(D), N!=2} = 1.

%place all the pentominoes on any side of the grid
{place(A, X, Y, D) : letter(A), X=1..6-X1, Y=1..5-Y1, part(D), max_column_selected(A, N, Y1), max_row_selected(A, N, X1), selected(A, N), A != t, A!=u} = 1 :- letter(A), A != t, A != u.

%fill the grid with the selected pentominoes
{case(X, Y, A, D) :  shape(A, N, X1, Y1), selected(A, N), X=I+X1, Y=J+Y1}=5 :- place(A, I, J, D).

%adding constraint 

%adding constraint for the pentominoes to be placed in the grid
:- case(X, Y, A, D), case(X, Y, B, D), A != B.

#show case/4.


