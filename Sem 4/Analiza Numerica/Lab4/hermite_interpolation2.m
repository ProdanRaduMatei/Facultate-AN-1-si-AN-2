% Hermite interpolation function
function [distance_estimate, speed_estimate] = hermite_interpolation2(Time, Distance, Speed, t)
    n = length(Time);

    % Initialize matrices
    Q = zeros(2*n, 2*n);
    C = zeros(2*n, 1);

    % Populate Q and C matrices
    for i = 1:n
        Q(2*i-1, 1) = Time(i);
        Q(2*i, 1) = Time(i);
        Q(2*i, 2) = 1;

        C(2*i-1) = Distance(i);
        C(2*i) = Distance(i);

        if i > 1
            Q(2*i-1, 3) = (Q(2*i-1, 1) - Q(2*i-2, 1));
            Q(2*i, 3) = (Q(2*i, 1) - Q(2*i-1, 1));
            Q(2*i, 4) = 1;
        end

        if i > 2
            Q(2*i-1, 5) = (Q(2*i-1, 3) - Q(2*i-3, 3));
            Q(2*i, 5) = (Q(2*i, 3) - Q(2*i-2, 3));
        end
    end

    % Populate Hermite coefficients
    for i = 1:n-1
        Q(2*i+1, 2*i+1) = 1;
        Q(2*i+1, 2*i+2) = -1;
        Q(2*i+1, 2*i+3) = 2 * Q(2*i+1, 1) - 2 * Q(2*i, 1);
        Q(2*i+1, 2*i+4) = -2 * Q(2*i+1, 1) + 2 * Q(2*i, 1);

        C(2*i+1) = Speed(i);
        C(2*i+2) = Speed(i);
    end

    % Solve for Hermite coefficients
    hermite_coefficients = Q \ C;

    % Evaluate Hermite polynomials at t
    distance_estimate = 0;
    speed_estimate = 0;
    for i = 1:n
        distance_estimate = distance_estimate + hermite_coefficients(2*i-1) * hermite_polynomial(Q, t, i);
        speed_estimate = speed_estimate + hermite_coefficients(2*i) * hermite_polynomial(Q, t, i);
    end
end