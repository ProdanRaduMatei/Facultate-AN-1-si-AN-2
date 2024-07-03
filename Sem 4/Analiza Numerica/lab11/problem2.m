A = [5 -1 0 0; 
    -1 5 -1 0; 
    0 -1 5 -1; 
    0 0 -1 5];
b = [7; -10; -6; 16];
epsilon = 1e-3;
max_iter = 1000;

% Jacobi method
D = diag(diag(A));
R = A - D;
x = zeros(size(b));
for iter = 1:max_iter
    x_new = inv(D)*(b - R*x);
    if max(abs(x_new - x)) < epsilon
        break;
    end
    x = x_new;
end
disp('Solution by Jacobi method:'), disp(x)

% Gauss-Seidel method
L = tril(A); % lower part of A
U = triu(A, 1); % upper part of A
x = zeros(size(b));
for iter = 1:max_iter
    x_new = inv(L)*(b - U*x);
    if max(abs(x_new - x)) < epsilon
        break;
    end
    x = x_new;
end
disp('Solution by Gauss-Seidel method:'), disp(x)

% Relaxation method
omega = 1.1; % relaxation factor
x = zeros(size(b));
for iter = 1:max_iter
    x_new = (1-omega)*x + omega*inv(D)*(b - R*x);
    if max(abs(x_new - x)) < epsilon
        break;
    end
    x = x_new;
end
disp('Solution by Relaxation method:'), disp(x)