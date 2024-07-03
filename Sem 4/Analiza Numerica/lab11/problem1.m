A = [8 2 4; 
    3 5 1; 
    2 1 4];
b = [-16; 4; -12];

% Jacobi method
[x_jacobi, iter_jacobi] = jacobiMethod(A, b);
disp('Solution by Jacobi method:'), disp(x_jacobi)

% Gauss-Seidel method
[x_gs, iter_gs] = gaussSeidelMethod(A, b);
disp('Solution by Gauss-Seidel method:'), disp(x_gs)

% Relaxation method
omega = 1.1;
[x_relax, iter_relax] = sorMethod(A, b, omega);
disp('Solution by Relaxation method:'), disp(x_relax)

function [x, iter] = jacobiMethod(A, b)
    n = length(b);
    x = zeros(n, 1);
    x_new = x;
    epsilon = 1e-3;
    max_iter = 1000; % nr of interations
    iter = 0;
    while iter < max_iter
        for i = 1:n
            x_new(i) = (b(i) - A(i, :) * x + A(i, i) * x(i)) / A(i, i);
        end
        if norm(x_new - x, inf) < epsilon
            break;
        end
        x = x_new;
        iter = iter + 1;
    end
end

function [x, iter] = gaussSeidelMethod(A, b)
    n = length(b);
    x = zeros(n, 1);
    epsilon = 1e-3;
    max_iter = 1000;
    iter = 0;
    while iter < max_iter
        x_old = x;
        for i = 1:n
            sum1 = A(i, 1:i-1) * x(1:i-1); 
            sum2 = A(i, i+1:n) * x(i+1:n);
            x(i) = (b(i) - sum1 - sum2) / A(i, i);
        end
        if norm(x - x_old, inf) < epsilon
            break;
        end
        iter = iter + 1;
    end
end

function [x, iter] = sorMethod(A, b, omega)
    n = length(b);
    x = zeros(n, 1);
    epsilon = 1e-3;
    max_iter = 1000;
    iter = 0;
    while iter < max_iter
        x_old = x;
        for i = 1:n
            sum1 = A(i, 1:i-1) * x(1:i-1);
            sum2 = A(i, i+1:n) * x(i+1:n);
            x(i) = (1 - omega) * x(i) + (omega / A(i, i)) * (b(i) - sum1 - sum2);
        end
        if norm(x - x_old, inf) < epsilon
            break;
        end
        iter = iter + 1;
    end
end