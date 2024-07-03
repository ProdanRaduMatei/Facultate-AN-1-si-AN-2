% % 1.
% % Define the function f(x)
% f = @(x) 3 ./ (1 + 2 * x.^2);

% % Trapezoidal rule
% a = 0; b = 1; % Limits of integration
% n = 1000; % Number of subintervals
% x = linspace(a, b, n+1);
% h = (b - a) / n;
% I_trapezium = h * (0.5 * (f(a) + f(b)) + sum(f(x(2:end-1))));

% % Plot the graph of the function and the trapezium
% x_interval = linspace(a, b, 1000);
% y_interval = f(x_interval);
% trapezium_x = [0, 0, 1, 1, 0];
% trapezium_y = [0, f(0), f(1), 0, 0];
% figure;
% plot(x_interval, y_interval, 'b-', 'LineWidth', 2); % Function
% hold on;
% plot(trapezium_x, trapezium_y, 'r--', 'LineWidth', 2); % Trapezium
% xlabel('x');
% ylabel('f(x)');
% title('Graph of the Function and Trapezium');
% legend('f(x)', 'Trapezium', 'Location', 'best');
% grid on;
% hold off;

% % Simpson's rule
% I_simpson = (h / 3) * (f(a) + 4 * sum(f(x(2:2:end-1))) + 2 * sum(f(x(3:2:end-2))) + f(b));

% % Display the results
% fprintf('Approximation of the integral using trapezium rule: %.6f\n', I_trapezium);
% fprintf('Approximation of the integral using Simpson''s rule: %.6f\n', I_simpson);

% 2.
% % Define the function f(x, y)
% f = @(x, y) log(2 * x + y);

% % Define the limits of integration
% a = 1.2; b = 3; % limits for x
% c = 1; d = 1.6; % limits for y

% % Trapezium formula for double integrals
% I_trapezium = (((b - a) * (d - c)) / 16) * (f(a, c) + f(a, d) + f(b, c) + f(b, d) + 2 * f((a + b) / 2, c) + 2 * f((a + b) / 2, d) + 2 * f(a, (c + d) / 2) + 2 * f(b, (c + d) / 2) + 4 * f((a + b) / 2, (c + d) / 2));

% % Display the result
% fprintf('Approximation of the double integral using trapezium formula: %.6f\n', I_trapezium);

% 3.
% % Define parameters
% R = 110;
% p = 75;

% % Define the function f(x)
% f = @(x) sqrt(1 - (p/R) * sin(x));

% % Define limits of integration
% a = 0; b = 2 * pi;

% % Repeated trapezium formula with two different values of n
% n_values = [10, 100]; % Number of subintervals

% % Evaluate the integral for each value of n
% for i = 1:length(n_values)
%     n = n_values(i);
%     x = linspace(a, b, n+1);
%     h = (b - a) / n;
%     H_approx = h * (0.5 * (f(a) + f(b)) + sum(f(x(2:end-1))));
%     H = (60 * R / (R^2 - p^2)) * H_approx;
%     fprintf('Approximation of H(p, R) with n = %d: %.6f\n', n, H);
% end

% 4.
% % Define the function f(x)
% f = @(x) 1 ./ (5 + sin(25 * x));

% % Define limits of integration
% a = 0; b = pi;

% % Repeated Simpson's formula with two different values of n
% n_values = [12, 30]; % Number of subintervals

% % Evaluate the integral for each value of n
% for i = 1:length(n_values)
%     n = n_values(i);
%     x = linspace(a, b, n+1);
%     h = (b - a) / n;

%     % Compute the sum of odd terms and even terms
%     sum_odd = sum(f(x(2:2:end-1)));
%     sum_even = sum(f(x(3:2:end-2)));

%     % Apply Simpson's rule
%     I_approx = (h / 3) * (f(a) + 4 * sum_odd + 2 * sum_even + f(b));

%     fprintf('Approximation of the integral with n = %d: %.6f\n', n, I_approx);
% end

% 5.
% Define the function f(t)
f = @(t) exp(-t.^2);

% Define limits of integration and x value
a = 0; x = 0.5;

% Repeated Simpson's formula with two different values of n
n_values = [4, 10]; % Number of subintervals

% Evaluate the integral for each value of n
for i = 1:length(n_values)
    n = n_values(i);
    t = linspace(a, x, n+1);
    h = (x - a) / n;
    
    % Compute the sum of odd terms and even terms
    sum_odd = sum(f(t(2:2:end-1)));
    sum_even = sum(f(t(3:2:end-2)));
    
    % Apply Simpson's rule
    E_approx = (h / 3) * (f(a) + 4 * sum_odd + 2 * sum_even + f(x));
    
    % Display the result
    fprintf('Approximation of E(0.5) with n = %d: %.12f\n', n, E_approx);
    
    % Estimate the accuracy of the result
    correct_value = 0.520499876;
    error = abs(E_approx - correct_value);
    fprintf('Estimated error: %.12f\n', error);
end

% % Define the function
% f = @(t) exp(-t.^2);

% % Define the limits of integration
% a = 0;
% b = 0.5;

% % Define the values of n
% n_values = [4, 10];

% % Initialize the results vector
% E_values = zeros(size(n_values));

% % Calculate the integral for each value of n using the repeated Simpson's rule
% for i = 1:length(n_values)
%     n = n_values(i);
%     h = (b - a) / n;
%     x = a:h:b;
%     y = f(x);
%     E_values(i) = (2/sqrt(pi)) * h/3 * (y(1) + 4*sum(y(2:2:end-1)) + 2*sum(y(3:2:end-2)) + y(end));
% end

% % Define the correct value of E(0.5)
% E_correct = 0.520499876;

% % Calculate the absolute errors
% errors = abs(E_values - E_correct);

% % Display the results
% for i = 1:length(n_values)
%     disp(['n = ', num2str(n_values(i)), ', E = ', num2str(E_values(i)), ', error = ', num2str(errors(i))])
% end