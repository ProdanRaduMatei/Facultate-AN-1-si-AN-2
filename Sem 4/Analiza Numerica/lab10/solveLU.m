function x = solveLU(L, U, b)
n = length(b);
z = zeros(n, 1);
x = zeros(n, 1);

% Forward substitution
for i = 1:n
    z(i) = (b(i) - L(i, 1:i-1) * z(1:i-1)) / L(i, i);
end

% Backward substitution
for i = n:-1:1
    x(i) = (z(i) - U(i, i+1:n) * x(i+1:n)) / U(i, i);
end
end