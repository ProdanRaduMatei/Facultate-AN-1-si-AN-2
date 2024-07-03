% 1.
% % Given data
% x = [1.2, 1.6, 2, 2.4, 3.1, 4];
% lg_x = [0.07918, 0.20412, 0.30103, 0.38021, 0.49136, 0.60206];
% 
% % Points to interpolate
% x_interpolate = [2.5, 3.26];
% 
% % Calculate divided differences
% n = length(x);
% F = zeros(n, n);
% F(:,1) = lg_x';
% 
% for j = 2:n
%     for i = j:n
%         F(i,j) = (F(i,j-1) - F(i-1,j-1)) / (x(i) - x(i-j+1));
%     end
% end
% 
% % Compute the interpolated values
% lg_interpolated = zeros(size(x_interpolate));
% for k = 1:length(x_interpolate)
%     sum = F(1,1);
%     for i = 2:n
%         prod = 1;
%         for j = 1:i-1
%             prod = prod * (x_interpolate(k) - x(j));
%         end
%         sum = sum + F(i,i) * prod;
%     end
%     lg_interpolated(k) = sum;
% end
% 
% % Display the interpolated values and compare with given values
% disp('Interpolated values:');
% disp(['lg(2.5) = ', num2str(lg_interpolated(1))]);
% disp(['lg(3.26) = ', num2str(lg_interpolated(2))]);
% 
% % Compare with given values
% lg_given = [0.39794, 0.5132176];
% error = abs(lg_interpolated - lg_given);
% disp('Absolute errors:');
% disp(['Error for lg(2.5) = ', num2str(error(1))]);
% disp(['Error for lg(3.26) = ', num2str(error(2))]);
% 
% % Evaluate the interpolation polynomial for plotting
% t_values = linspace(min(x), max(x), 100);
% lg_values = zeros(size(t_values));
% for k = 1:length(t_values)
%     t = t_values(k);
%     poly_newton = F(1,1);
%     for i = 2:n
%         prod = 1;
%         for j = 1:i-1
%             prod = prod * (t - x(j));
%         end
%         poly_newton = poly_newton + F(i,i) * prod;
%     end
%     lg_values(k) = poly_newton;
% end
% 
% % Plot the data points and the interpolation polynomial
% figure;
% hold on;
% plot(x, lg_x, 'ro', 'MarkerSize', 8); % Data points
% plot(t_values, lg_values, 'b-', 'LineWidth', 1.5); % Interpolation polynomial
% xlabel('x');
% ylabel('lg(x)');
% title('Newton Interpolation Polynomial');
% legend('Data Points', 'Interpolation Polynomial');
% grid on;
% hold off;
% 
% % Define the Newton interpolation polynomial function
% N_mf = @(x) F(1,1);
% for i = 2:n
%     prod = 1;
%     for j = 1:i-1
%         prod = prod .* (x - x(j));
%     end
%     N_mf = @(x) N_mf(x) + F(i,i) * prod;
% end
% 
% % Define f(y) = lg(y)
% f_y = @(y) log10(y);
% 
% % Estimate the maximum interpolation error
% max_error = 0;
% for i = 10:30
%     y_i = i / 10;
%     lg_y_i = f_y(y_i);
%     N_mf_x_i = N_mf(y_i);
%     error = abs(lg_y_i - N_mf_x_i);
%     if error > max_error
%         max_error = error;
%     end
% end
% 
% disp(['Maximum interpolation error: ', num2str(max_error)]);

% 2.
% Given data
Points = [1 2 3 4 5];
Students = [30 26 22 32 28];
x = Points; % x-coordinates
y = Students; % y-coordinates
n = length(x);

% Calculate the divided differences
F = zeros(n, n); % Initialize the divided differences table
F(:,1) = y'; % Assign the first column to be the y-coordinates

for j = 2:n
    for i = j:n
        F(i, j) = (F(i, j - 1) - F(i - 1, j - 1)) / (x(i) - x(i - j + 1));
    end
end

% Evaluate Newton interpolation polynomial at a point
x_eval = 3.5; % Point to evaluate
y_eval = F(1,1); % Initialize the result with the first term of the polynomial

for j = 2:n
    term = F(j,j);
    for i = 1:j-1
        term = term * (x_eval - x(i));
    end
    y_eval = y_eval + term;
end

% Display the approximate number of students
fprintf('Approximate number of students expected to obtain 3.5 points: %f\n', y_eval);

% Plot the data points
plot(x, y, 'bo', 'MarkerSize', 8);
hold on;

% Plot the Newton interpolation polynomial
xx = linspace(min(x), max(x), 100); % Generate points for smooth curve
yy = zeros(size(xx));
for k = 1:length(xx)
    % Evaluate the polynomial at each point
    yy(k) = F(1,1);
    for j = 2:n
        term = F(j,j);
        for i = 1:j-1
            term = term * (xx(k) - x(i));
        end
        yy(k) = yy(k) + term;
    end
end
plot(xx, yy, 'r-', 'LineWidth', 2);

% Add labels and legend
xlabel('Points');
ylabel('Students');
title('Newton Interpolation Polynomial');
legend('Data Points', 'Interpolation Polynomial', 'Location', 'northwest');

hold off;

% 3.
% % Define the function f(x) = e^cos(x)
% f = @(x) exp(cos(x));
% 
% % Generate 15 equidistant interpolation points in [0, 5]
% n = 15;
% x_interpolation = linspace(0, 5, n);
% 
% % Calculate corresponding y-values for interpolation points
% y_interpolation = f(x_interpolation);
% 
% % Calculate divided differences
% F = divided_diff(x_interpolation, y_interpolation);
% 
% % Plot the function f(x)
% x = linspace(0, 5, 1000);
% y = f(x);
% plot(x, y, 'b-', 'LineWidth', 2);
% hold on;
% 
% % Plot the interpolation points
% plot(x_interpolation, y_interpolation, 'ro', 'MarkerSize', 8);
% 
% % Plot the Newton interpolation polynomial
% xx = linspace(0, 5, 1000);
% yy = newton_interpolation(xx, x_interpolation, F);
% plot(xx, yy, 'g--', 'LineWidth', 2);
% 
% % Add labels and legend
% xlabel('x');
% ylabel('f(x)');
% title({'Newton Interpolation Polynomial for f(x) = e^(cos(x))'});
% legend('f(x)', 'Interpolation Points', 'Newton Interpolation Polynomial', 'Location', 'best');
% 
% hold off;
% 
% % Function to calculate divided differences
% function F = divided_diff(x, y)
%     n = length(x);
%     F = zeros(n, n); % Initialize the divided differences table
%     F(:,1) = y'; % Assign the first column to be the y-coordinates
% 
%     for j = 2:n
%         for i = j:n
%             F(i, j) = (F(i, j - 1) - F(i - 1, j - 1)) / (x(i) - x(i - j + 1));
%         end
%     end
% end
% 
% % Function to calculate Newton interpolation polynomial
% function yy = newton_interpolation(xx, x, F)
%     n = length(x);
%     yy = zeros(size(xx));
% 
%     for k = 1:length(xx)
%         % Evaluate the polynomial at each point
%         yy(k) = F(1, 1);
%         for j = 2:n
%             term = F(j, j);
%             for i = 1:j-1
%                 term = term * (xx(k) - x(i));
%             end
%             yy(k) = yy(k) + term;
%         end
%     end
% end

% 4.
% % Define the function for which we want to find the root
% f = @(x) x ^ 2 - 178;
% 
% % Initial guess
% x0 = 10;
% 
% % Desired precision
% epsilon = 10^(-3);
% 
% % Aitken algorithm
% x1 = f(x0);
% x2 = f(x1);
% x_approx = x0 - ((x1 - x0) ^ 2) / (x2 - 2 * x1 + x0);
% 
% % Iterative process
% while abs(x_approx - x0) >= epsilon
%     x0 = x_approx;
%     x1 = f(x0);
%     x2 = f(x1);
%     x_approx = x0 - ((x1 - x0) ^ 2) / (x2 - 2 * x1 + x0);
% end
% 
% % Display the result
% fprintf('Approximate value of sqrt(178) using Aitken algorithm: %f\n', x_approx);

% 5.
% % Define the functions
% f = @(x) 5.^x; % f(x) = 5^x
% g = @(x) sqrt(x); % g(x) = sqrt(x)
% 
% % Define the intervals and number of nodes
% nodes_f = linspace(-2, 2, 5); % Nodes for f(x)
% nodes_g = linspace(1, 5, 5); % Nodes for g(x)
% 
% % Define the target value
% target_value = sqrt(5);
% 
% % Neville's algorithm function
% neville = @(x, x_nodes, y_nodes) neville_interpolation(x, x_nodes, y_nodes);
% 
% % Approximate sqrt(5) using Neville's algorithm for f(x) = 5^x
% approx_f = neville(1/2, nodes_f, f(nodes_f));
% 
% % Approximate sqrt(5) using Neville's algorithm for g(x) = sqrt(x)
% approx_g = neville(5, nodes_g, g(nodes_g));
% 
% % Display the results
% fprintf('Approximation of sqrt(5) using f(x) = 5^x: %f\n', approx_f);
% fprintf('Approximation of sqrt(5) using g(x) = sqrt(x): %f\n', approx_g);
% 
% % Neville's algorithm function
% function y_interpolated = neville_interpolation(x, x_nodes, y_nodes)
%     n = length(x_nodes);
%     Q = zeros(n, n);
% 
%     % Fill the first column with y_nodes
%     Q(:,1) = y_nodes;
% 
%     % Neville's algorithm
%     for i = 2:n
%         for j = 2:i
%             Q(i,j) = ((x - x_nodes(i - j + 1)) * Q(i, j - 1) - (x - x_nodes(i)) * Q(i - 1, j - 1)) / (x_nodes(i) - x_nodes(i - j + 1));
%         end
%     end
% 
%     % The interpolated value is the value at the last row and last column
%     y_interpolated = Q(n,n);
% end
