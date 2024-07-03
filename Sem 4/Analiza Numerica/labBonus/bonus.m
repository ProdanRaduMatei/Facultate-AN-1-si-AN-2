% 1.
% Define the matrix A and the vector b
A = [1 2 4; 3 8 14; 2 6 13];
b = [3; 13; 4];

% Compute the LU decomposition of A
[L, U] = lu(A);

% Solve the system Ax = b
y = L \ b;  % Solve the system Ly = b
x = U \ y;  % Solve the system Ux = y

% Display the LU decomposition and the solution
disp('LU decomposition:')
disp('L = ')
disp(L)
disp('U = ')
disp(U)

disp('Solution of the system Ax = b:')
disp(x)

% 2.
% % Define the matrix A and the vector b
% A = [5 -2 3; -3 9 1; 2 -1 7];
% b = [-1; 2; 3];

% % Define the initial guess and the precision
% x0 = zeros(3, 1);
% e = 1e-10;

% % Jacobi method
% D = diag(diag(A));
% R = A - D;
% x = x0;
% i = 0;
% disp('Jacobi method:')
% while norm(A*x - b) > e
%     x_new = D \ (b - R*x);
%     i = i + 1;
%     disp(['Step ', num2str(i), ', x = ', num2str(x_new')])
%     x = x_new;
% end

% % Gauss-Seidel method
% L = tril(A);
% U = triu(A, 1);
% x = x0;
% i = 0;
% disp('Gauss-Seidel method:')
% while norm(A*x - b) > e
%     x_new = L \ (b - U*x);
%     i = i + 1;
%     disp(['Step ', num2str(i), ', x = ', num2str(x_new')])
%     x = x_new;
% end

% % Relaxation method
% omega = 1.1;  % Relaxation factor
% x = x0;
% i = 0;
% disp('Relaxation method:')
% while norm(A*x - b) > e
%     x_new = (1 - omega)*x + omega*(D \ (b - R*x));
%     i = i + 1;
%     disp(['Step ', num2str(i), ', x = ', num2str(x_new')])
%     x = x_new;
% end

% 3.
% % Define the function and its derivative
% f = @(x) 4*x^3 - 2*x^2 + 3;
% df = @(x) 12*x^2 - 4*x;

% % Define the initial point
% x = -1;

% % Compute the first three Newton iterates
% for i = 1:3
%     x_new = x - f(x)/df(x);
%     disp(['Step ', num2str(i), ', x = ', num2str(x_new)])
%     x = x_new;
% end

% 4.
% % Define the function
% f = @(x) x^3 - sin(x) + 4*x^2 + 6*x + 9;

% % Define the initial points
% x = [8, 7];

% % Compute x2, x3, x4 using the Secant method
% for i = 3:5
%     x_new = x(i-1) - f(x(i-1))*(x(i-1) - x(i-2))/(f(x(i-1)) - f(x(i-2)));
%     disp(['Step ', num2str(i-1), ', x = ', num2str(x_new)])
%     x = [x, x_new];
% end

% 5.
% % Define the function
% f = @(x) x^2 - 2;

% % Define the initial points
% x = [0, 1];

% % Compute x2 using the Secant method
% x_new = x(2) - f(x(2))*(x(2) - x(1))/(f(x(2)) - f(x(1)));
% disp(['x2 = ', num2str(x_new)])

% 6.
% % Define the function
% f = @(x) x^2 - 4*x*sin(x) + (2*sin(x))^2;

% % Define the interval [a, b] and the precision
% a = 0;
% b = 2*pi;
% e = 1e-10;

% % Bisection algorithm
% while b - a > e
%     c = (a + b)/2;
%     if f(c) == 0
%         break
%     elseif f(a)*f(c) < 0
%         b = c;
%     else
%         a = c;
%     end
% end

% % Display the root
% disp(['Root = ', num2str(c)])