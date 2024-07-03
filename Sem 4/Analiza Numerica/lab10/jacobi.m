function [x, iter] = jacobi(A, b, e)
n = length(b);
x = zeros(n, 1);
iter = 0;

while true
    x_new = (b - A * x + diag(A) .* x) ./ diag(A);
    if max(abs(x_new - x)) < e
        break;
    end
    x = x_new;
    iter = iter + 1;
end
x = x_new;
end