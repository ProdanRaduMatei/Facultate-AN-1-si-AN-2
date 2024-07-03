% Function to compute the derivative of the polynomial
function der = poly_der(x, index)
    n = length(index);
    der = zeros(size(x));

    for i = 1:n
        p = 1;
        for j = 1:n
            if j ~= index(i)
                p = p .* (x - index(j));
            end
        end
        der = der + p;
    end
end