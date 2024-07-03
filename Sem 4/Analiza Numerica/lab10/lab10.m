% 1.
% % Define the system
% n = 4;
% A = [1 1 1 1; 2 3 1 5; -1 1 -5 3; 3 1 7 -2];
% b = [10; 31; -2; 18];

% % Solve the system
% x = gaussPartialPivot(n, A, b);

% % Display the solution
% disp(x);

% 2.
% % Define the system
% M = [6 2 1 -1; 2 4 1 0; 1 1 4 -1; -1 0 -1 3];
% b = [8; 7; 5; 1];

% % Compute LU decomposition
% [L, U] = doolittle(M);

% % Solve the system
% x = solveLU(L, U, b);

% % Display the solution
% disp(x);

% 3.
% Define the system
A = [3 -1 0 0 0 0; -1 3 -1 0 0 0; 0 -1 3 -1 0 0; 0 0 -1 3 -1 0; 0 0 0 -1 3 -1; 0 0 0 0 -1 3];
b = [2; 1; 1; 1; 1; 2];

% Solve the system using Jacobi method
[x_jacobi, iter_jacobi] = jacobi(A, b, 1e-3);
disp('Jacobi method:');
disp(x_jacobi);
disp('Number of iterations:');
disp(iter_jacobi);

% Solve the system using Gauss-Seidel method
[x_gs, iter_gs] = gaussSeidel(A, b, 1e-3);
disp('Gauss-Seidel method:');
disp(x_gs);
disp('Number of iterations:');
disp(iter_gs);

% Solve the system using relaxation method
[x_relax, iter_relax] = relaxation(A, b, 1e-3, 1.25);
disp('Relaxation method:');
disp(x_relax);
disp('Number of iterations:');
disp(iter_relax);