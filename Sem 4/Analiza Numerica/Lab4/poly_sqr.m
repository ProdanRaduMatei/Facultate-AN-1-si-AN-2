% Function to compute the squared term of the polynomial
function sqr = poly_sqr(x, index)
    n = length(index);
    sqr = ones(size(x));

    for i = 1:n
        sqr = sqr .* (x - index(i)).^2;
    end
end