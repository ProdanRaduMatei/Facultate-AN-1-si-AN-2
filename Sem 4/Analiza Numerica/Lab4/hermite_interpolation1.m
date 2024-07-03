% Hermite interpolation function
function f_interpolated = hermite_interpolation1(x_values, y_values, dy_values, x_interpolate)
    % Construct the divided difference table
    n = length(x_values);
    Q = zeros(2*n, 2*n);
    Q(:, 1) = repelem(x_values, 2);
    Q(:, 2) = repelem(y_values, 2);
    Q(:, 3) = repelem(dy_values, 2);

    for j = 2:2*n
        for i = j:2*n
            if Q(i, 1) == Q(i-j+1, 1)
                Q(i, j+1) = Q(i, j);
            else
                Q(i, j+1) = (Q(i, j) - Q(i-1, j)) / (Q(i, 1) - Q(i-j+1, 1));
            end
        end
    end

    % Calculate the interpolated value at x_interpolate
    f_interpolated = 0;
    for i = 1:n
        L = 1;
        for j = 1:i-1
            L = L .* (x_interpolate - x_values(j));
        end
        f_interpolated = f_interpolated + Q(2*i-1, i+1) * L + Q(2*i, i+1) * L .* (2 * (x_interpolate - x_values(i)));
    end
end