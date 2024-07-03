% Hermite polynomial function
function y_interpolated = hermite_polynomial(x, x_nodes, y_nodes, dy_nodes)
    n = length(x_nodes);
    y_interpolated = zeros(size(x));

    for i = 1:n
        % Construct the Hermite basis function for each node
        h = @(z, i) (1 - 2 .* (z - x_nodes(i)) .* poly_der(z, i)) .* poly_sqr(z, i);

        % Calculate the interpolated value at each x
        y_interpolated = y_interpolated + y_nodes(i) .* h(x, i);
    end
end