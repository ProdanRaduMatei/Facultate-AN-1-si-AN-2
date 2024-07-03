% 1.
% % Given data
% Time = [0, 3, 5, 8, 13];
% Distance = [0, 225, 383, 623, 993];
% Speed = [75, 77, 80, 74, 72];
% 
% % Time to estimate
% t = 10;
% 
% % Hermite interpolation function
% [distance_estimate, speed_estimate] = hermite_interpolation2(Time, Distance, Speed, t);
% 
% % Display the results
% fprintf('Estimated position of the car at t = 10: %.2f units\n', distance_estimate);
% fprintf('Estimated speed of the car at t = 10: %.2f units/time\n', speed_estimate);

% 2.
% Given data points
x_values = [1, 2];
y_values = [0, 0.6931];
dy_values = [1, 0.5];
x_interpolate = 1.5;

% Apply cubic interpolation
cubic_approximation = cubic_interpolation(x_values, y_values, dy_values, x_interpolate);

% Calculate the exact value of f(1.5)
exact_value = log(1.5);

% Calculate the absolute approximation error
absolute_error = abs(cubic_approximation - exact_value);

% Display the results
fprintf('Cubic interpolation approximation of f(1.5): %.4f\n', cubic_approximation);
fprintf('Exact value of f(1.5): %.4f\n', exact_value);
fprintf('Absolute approximation error: %.4f\n', absolute_error);

% % 3.
% % Define the function f(x) = sin(2x)
% f = @(x) sin(2*x);
% 
% % Generate 15 equidistant nodes between -5 and 5
% n = 15;
% x_nodes = linspace(-5, 5, n);
% 
% % Calculate function values and derivative values at the nodes
% y_nodes = f(x_nodes);
% dy_nodes = 2 .* cos(2 .* x_nodes);
% 
% % Define the interval for plotting
% x_interval = linspace(-5, 5, 1000);
% 
% % Hermite interpolation function
% hermite_interpolation1 = @(x) hermite_polynomial1(x, x_nodes, y_nodes, dy_nodes);
% 
% % Calculate Hermite interpolation polynomial values
% y_hermite = hermite_interpolation1(x_interval);
% 
% % Plot the original function and Hermite interpolation polynomial
% figure;
% plot(x_interval, f(x_interval), 'b-', 'LineWidth', 2);
% hold on;
% plot(x_interval, y_hermite, 'r--', 'LineWidth', 2);
% scatter(x_nodes, y_nodes, 100, 'ko', 'filled');
% xlabel('x');
% ylabel('y');
% title('Hermite Interpolation of sin(2x)');
% legend('sin(2x)', 'Hermite Interpolation Polynomial', 'Equidistant Nodes', 'Location', 'best');
% grid on;
% hold off;

% % 4.
% % Given data points
% x_values = [8.3, 8.6];
% y_values = [17.56492, 18.50515];
% dy_values = [3.116256, 3.151762];
% x_interpolate = 8.4;
% 
% % Apply Hermite interpolation
% hermite_approximation = hermite_interpolation(x_values, y_values, dy_values, x_interpolate);
% 
% % Calculate the exact value of f(8.4)
% exact_value = x_interpolate * log(x_interpolate);
% 
% % Calculate the absolute approximation error
% absolute_error = abs(hermite_approximation - exact_value);
% 
% % Display the results
% fprintf('Hermite interpolation approximation of f(8.4): %.6f\n', hermite_approximation);
% fprintf('Exact value of f(8.4): %.6f\n', exact_value);
% fprintf('Absolute approximation error: %.6f\n', absolute_error);
% 
% % Hermite interpolation function
% function f_interpolated = hermite_interpolation(x_values, y_values, dy_values, x_interpolate)
%     % Construct the divided difference table
%     n = length(x_values);
%     Q = zeros(2*n, 2*n);
%     Q(:, 1) = repelem(x_values, 2);
%     Q(:, 2) = repelem(y_values, 2);
%     Q(:, 3) = repelem(dy_values, 2);
% 
%     for j = 2:2*n
%         for i = j:2*n
%             if Q(i, 1) == Q(i-j+1, 1)
%                 Q(i, j+1) = Q(i, j);
%             else
%                 Q(i, j+1) = (Q(i, j) - Q(i-1, j)) / (Q(i, 1) - Q(i-j+1, 1));
%             end
%         end
%     end
% 
%     % Calculate the interpolated value at x_interpolate
%     f_interpolated = 0;
%     for i = 1:n
%         L = 1;
%         for j = 1:i-1
%             L = L .* (x_interpolate - x_values(j));
%         end
%         f_interpolated = f_interpolated + Q(2*i-1, i+1) * L + Q(2*i, i+1) * L .* (2 * (x_interpolate - x_values(i)));
%     end
% end
