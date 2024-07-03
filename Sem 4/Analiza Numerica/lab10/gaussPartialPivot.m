function x = gaussPartialPivot(n, A, b)
% Initialize the solution vector
x = zeros(n, 1);

% Perform Gaussian elimination
for p = 1:n-1
    % Find the row with the largest absolute value in column p
    [~, q] = max(abs(A(p:n, p)));
    q = q + p - 1;
    
    % If the maximum value is zero, the system is incompatible
    if A(q, p) == 0
        error('The system is incompatible.');
    end
    
    % Swap rows p and q
    if q ~= p
        A([p q], :) = A([q p], :);
        b([p q]) = b([q p]);
    end
    
    % Perform elimination
    for i = p+1:n
        factor = A(i, p) / A(p, p);
        A(i, p:n) = A(i, p:n) - factor * A(p, p:n);
        b(i) = b(i) - factor * b(p);
    end
end

% If the last element of the matrix is zero, the system is incompatible
if A(n, n) == 0
    error('The system is incompatible.');
end

% Back substitution
x(n) = b(n) / A(n, n);
for i = n-1:-1:1
    x(i) = (b(i) - A(i, i+1:n) * x(i+1:n)) / A(i, i);
end
end