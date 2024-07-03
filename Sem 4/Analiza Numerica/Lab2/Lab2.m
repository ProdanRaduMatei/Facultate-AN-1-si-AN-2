% 1.
% f : [a, b] -> R
% xi apartine [a, b] nodes
% f(xi) = y, i = 1,m
% (Lmf)(x) = (SUM(Ai * f(xi) * y))/ (SUM(Ai/(x - xi)
% Ai = 1/(PROD(xi - xj)

% x = [1960, 1970, 1980, 1990, 2000, 2010, 2020];
% y = [18458008, 19922618, 22125224, 22836234, 21919876, 20335211, 19442038];
% plot(x, y, '*');
% z = [1974, 2005, 2035];
% ans_z = Lagrange(z, x, y);
% fprintf('1974-%8.3f', ans_z(3));
% hold on;
% t = 1960:1:2020;
% plot(t, Lagrange(t, x, y)); %aproximate the population from 1960 until 2020

% 2.
% f(x) = sqrt(x)
% x = [144, 169, 196];
% y = [12, 13, 14];
% z = 153;
% ans_z = Lagrange(z, x, y)

% 3.
% x = 0:0.01:20;
% f = (2 + sin(3 * pi * x)) ./ (1 + x .^ 2);
% plot(x, f, 'r--');
% hold on;
% x_nodes = linspace(0, 20, 24);
% f_nodes = (2 + sin(3 * pi * x_nodes)) ./ (1 + x_nodes .^ 2);
% fL = Lagrange(x, x_nodes, f_nodes);
% plot(x, fL, 'b');

% Problem 4.
% % 1.
% % Define the function f(n)
% f = @(n) (3 * tan(n.^2)) ./ (n.^2 + 2);
% 
% % Create a vector of values for n within the interval [1, 14]
% n_values = linspace(1, 14, 1000); % Adjust the number of points for smoother plot
% 
% % Compute the corresponding values of f(n) for each n
% f_values = f(n_values);
% 
% % Plot the graph
% plot(n_values, f_values, 'b', 'LineWidth', 2);
% xlabel('n');
% ylabel('f(n)');
% title('Graph of f(n) = 3 * tan(n^2) / (n^2 + 2)');
% grid on;
% 
% % 2.
% % Define the function f(n)
% f = @(n) (3 * tan(n.^2)) ./ (n.^2 + 2);
% 
% % Generate interpolation points
% n_values = linspace(1, 14, 10); % Choose 10 points for interpolation
% f_values = f(n_values);
% 
% % Compute coefficients of the Lagrange interpolation polynomial
% p_coefficients = polyfit(n_values, f_values, length(n_values)-1);
% 
% % Define the Lagrange interpolation polynomial
% lagrange_poly = @(x) polyval(p_coefficients, x);
% 
% % Evaluate the Lagrange interpolation polynomial on a fine grid
% x_grid = linspace(1, 14, 1000);
% lagrange_values = lagrange_poly(x_grid);
% 
% % Plot the original function f(n)
% figure;
% plot(x_grid, f(x_grid), 'b', 'LineWidth', 2);
% hold on;
% 
% % Plot the Lagrange interpolation polynomial
% plot(x_grid, lagrange_values, 'r--', 'LineWidth', 2);
% 
% % Plot interpolation points
% scatter(n_values, f_values, 100, 'filled', 'MarkerFaceColor', 'g');
% 
% xlabel('n');
% ylabel('f(n)');
% title('Lagrange Interpolation Polynomial vs Original Function');
% legend('Original Function f(n)', 'Lagrange Interpolation Polynomial', 'Interpolation Points');
% grid on;
% 
% % 3.
% % Evaluate the Lagrange interpolation polynomial at f(2.5) and f(8.75)
% approximation_2_5 = lagrange_poly(2.5);
% approximation_8_75 = lagrange_poly(8.75);
% 
% % Display the results
% fprintf('Approximation of f(2.5): %.6f\n', approximation_2_5);
% fprintf('Approximation of f(8.75): %.6f\n', approximation_8_75);

% 4.
% % 1
% % Define the function f(n)
% f = @(n) (3 * tan(n.^2)) ./ (n.^2 + 2);
% 
% % Create a vector of values for n within the interval [1, 14]
% n_values = linspace(1, 14, 1000); % Adjust the number of points for smoother plot
% 
% % Compute the corresponding values of f(n) for each n
% f_values = f(n_values);
% 
% % Plot the graph
% plot(n_values, f_values, 'b', 'LineWidth', 2);
% xlabel('n');
% ylabel('f(n)');
% title('Graph of f(n) = 3 * tan(n^2) / (n^2 + 2)');
% grid on;
% 
% % 2
% % Define the function f(n)
% f = @(n) (3 * tan(n.^2)) ./ (n.^2 + 2);
% 
% % Generate interpolation points
% n_values = linspace(1, 14, 10); % Choose 10 points for interpolation
% f_values = f(n_values);
% 
% % Compute coefficients of the Lagrange interpolation polynomial
% p_coefficients = polyfit(n_values, f_values, length(n_values)-1);
% 
% % Define the Lagrange interpolation polynomial
% lagrange_poly = @(x) polyval(p_coefficients, x);
% 
% % Evaluate the Lagrange interpolation polynomial on a fine grid
% x_grid = linspace(1, 14, 1000);
% lagrange_values = lagrange_poly(x_grid);
% 
% % Plot the original function f(n)
% figure;
% plot(x_grid, f(x_grid), 'b', 'LineWidth', 2);
% hold on;
% 
% % Plot the Lagrange interpolation polynomial
% plot(x_grid, lagrange_values, 'r--', 'LineWidth', 2);
% 
% % Plot interpolation points
% scatter(n_values, f_values, 100, 'filled', 'MarkerFaceColor', '');
% 
% xlabel('n');
% ylabel('f(n)');
% title('Lagrange Interpolation Polynomial vs Original Function');
% legend('Original Function f(n)', 'Lagrange Interpolation Polynomial', 'Interpolation Points');
% grid on;
% 
% % 3
% % Evaluate the Lagrange interpolation polynomial at f(2.5) and f(8.75)
% approximation_2_5 = lagrange_poly(2.5);
% approximation_8_75 = lagrange_poly(8.75);
% 
% % Display the results
% fprintf('Approximation of f(2.5): %.6f\n', approximation_2_5);
% fprintf('Approximation of f(8.75): %.6f\n', approximation_8_75);


% 5.

% Define the function f(x)
f = @(x) log(x + 2);

% Generate interpolation points
x_values = linspace(-1, 1, 13); % 13 equispaced points in [-1, 1]
f_values = f(x_values);

% Compute coefficients of the Lagrange interpolation polynomial
p_coefficients = polyfit(x_values, f_values, length(x_values)-1);

% Define the Lagrange interpolation polynomial
lagrange_poly = @(x) polyval(p_coefficients, x);

% Evaluate the Lagrange interpolation polynomial on a fine grid
x_grid = linspace(-1, 1, 1000);
lagrange_values = lagrange_poly(x_grid);

% Plot the function f(x)
figure;
plot(x_grid, f(x_grid), 'b', 'LineWidth', 2);
hold on;

% Plot the Lagrange interpolation polynomial
plot(x_grid, lagrange_values, 'r--', 'LineWidth', 2);

% Plot interpolation points
scatter(x_values, f_values, 100, 'filled', 'MarkerFaceColor', 'r');

xlabel('x');
ylabel('f(x)');
title('Lagrange Interpolation Polynomial vs Original Function');
legend('Original Function f(x)', 'Lagrange Interpolation Polynomial', 'Interpolation Points');
grid on;
