% Function for cubic interpolation
function y_interpolated = cubic_interpolation(x_values, y_values, dy_values, x_interpolate)
    n = length(x_values);
    A = zeros(n);

    % Construct A matrix
    for i = 1:n
        A(i, 1) = y_values(i);
        A(i, 2) = dy_values(i);
        if i > 1
            A(i, 3) = (3*(y_values(i) - y_values(i-1)) - 2*dy_values(i) - dy_values(i-1)) / (x_values(i) - x_values(i-1));
            A(i, 4) = (2*(y_values(i-1) - y_values(i)) + dy_values(i) + dy_values(i-1)) / (x_values(i) - x_values(i-1))^2;
        end
    end

    % Calculate interpolated value
    y_interpolated = A(1, 1) + A(1, 2)*(x_interpolate - x_values(1)) + A(1, 3)*(x_interpolate - x_values(1))^2 + A(1, 4)*(x_interpolate - x_values(1))^3;
end