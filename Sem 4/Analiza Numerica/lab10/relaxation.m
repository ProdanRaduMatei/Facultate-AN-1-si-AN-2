function [x, iter] = relaxation(A, b, e, w)
n = length(b);
x = zeros(n, 1);
iter = 0;

while true
    x_new = x;
    for i = 1:n
        x_new(i) = (1 - w) * x(i) + (w / A(i, i)) * (b(i) - A(i, :) * x_new + A(i, i) * x_new(i));
    end
    if max(abs(x_new - x)) < e
        break;
    end
    x = x_new;
    iter = iter + 1;
end
x = x_new;
end