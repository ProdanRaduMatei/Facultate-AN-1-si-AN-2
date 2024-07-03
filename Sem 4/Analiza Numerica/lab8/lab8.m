% 1.
% Define the function and its second derivative
f = @(x) exp(-x.^2);
f2 = @(x) (4*x.^2 - 2).*exp(-x.^2);

% Define the limits of integration
a = 1;
b = 1.5;

% Calculate the integral using the rectangle rule
E = (a + b) / 2;  % midpoint
R1 = ((b - a)^3 / 24) * f2(E);  % error term
I_rect = (b - a) * f(E) + R1;

% Display the result
disp(['Rectangle rule: ', num2str(I_rect)])

% Define the values of n
n_values = [150, 500];

% Initialize the results vector
I_values = zeros(size(n_values));

% Calculate the integral for each value of n using the repeated rectangle rule
for i = 1:length(n_values)
    n = n_values(i);
    h = (b - a) / n;
    x = a + h/2 : h : b;
    Rn = ((b - a)^3 / (24 * n^2)) * f2(E);  % error term
    I_values(i) = h * sum(f(x)) + Rn;
end

% Display the results
for i = 1:length(n_values)
    disp(['n = ', num2str(n_values(i)), ', I = ', num2str(I_values(i))])
end

% Plot the function
x = linspace(a, b, 100);
y = f(x);
figure
plot(x, y, 'b')
hold on

% Plot the rectangle
x_rect = [a a b b];
y_rect = [0 f(E) f(E) 0];
plot(x_rect, y_rect, 'r')

% Set the plot labels and title
xlabel('x')
ylabel('f(x)')
title('Approximation of the integral using the rectangle rule')
legend('f(x)', 'Rectangle', 'Location', 'Best')

% Hold off the plot
hold off

% 2.
% % Define the function
% f = @(x) 2 ./ (1 + x.^2);

% % Define the limits of integration
% a = 0;
% b = 1;

% % Define the precision
% epsilon = 10^-4;

% % Initialize the Romberg matrix
% R = zeros(10, 10);

% % Calculate the first element of the sequence using the trapezium formula
% h = b - a;
% R(1, 1) = h/2 * (f(a) + f(b));

% % Calculate the rest of the sequence using the Romberg algorithm
% for i = 2:10
%     h = h / 2;
%     sum = 0;
%     for k = 1:2^(i-2)
%         sum = sum + f(a + (2*k-1)*h);
%     end
%     R(i, 1) = 1/2 * R(i-1, 1) + h * sum;
%     for j = 2:i
%         R(i, j) = R(i, j-1) + (R(i, j-1) - R(i-1, j-1)) / (4^(j-1) - 1);
%     end
%     if (i > 1 && abs(R(i, i) - R(i-1, i-1)) < epsilon)
%         break;
%     end
% end

% % Display the result
% disp(['Romberg algorithm for trapezium formula: ', num2str(R(i, i))])

% % Initialize the Aitken matrix
% A = zeros(10, 10);

% % Calculate the first element of the sequence using the trapezium formula
% h = b - a;
% A(1, 1) = h/2 * (f(a) + f(b));

% % Calculate the rest of the sequence using the Aitken's form of the Romberg algorithm
% for i = 2:10
%     h = h / 2;
%     sum = 0;
%     for k = 1:2^(i-2)
%         sum = sum + f(a + (2*k-1)*h);
%     end
%     A(i, 1) = 1/2 * A(i-1, 1) + h * sum;
%     for j = 2:i
%         A(i, j) = ((4^(j-1)) * A(i, j-1) - A(i-1, j-1)) / (4^(j-1) - 1);
%     end
%     if (i > 1 && abs(A(i, i) - A(i-1, i-1)) < epsilon)
%         break;
%     end
% end

% % Display the result
% disp(['Aitken''s form of the Romberg algorithm: ', num2str(A(i, i))])

% 3.
% % Define the function
% f = @(x) 100./x.^2 .* sin(10./x);

% % Define the limits of integration
% a = 1;
% b = 3;

% % Define the precision
% epsilon = 10^-4;

% % Plot the function
% x = linspace(a, b, 1000);
% y = f(x);
% figure
% plot(x, y)
% xlabel('x')
% ylabel('f(x)')
% title('Graph of the function')

% % Define the Simpson's rule
% Simpson = @(a, b) (b - a) / 6 * (f(a) + 4*f((a + b) / 2) + f(b));

% % Calculate the integral using the adaptive quadrature algorithm
% I_adquad = adquad(a, b, epsilon, Simpson);

% % Display the result
% disp(['Adaptive quadrature: ', num2str(I_adquad)])

% % Define the values of n
% n_values = [50, 100];

% % Initialize the results vector
% I_values = zeros(size(n_values));

% % Calculate the integral for each value of n using the repeated Simpson's rule
% for i = 1:length(n_values)
%     n = n_values(i);
%     h = (b - a) / n;
%     x = a:h:b;
%     I_values(i) = h/3 * (f(a) + 4*sum(f(x(2:2:end-1))) + 2*sum(f(x(3:2:end-2))) + f(b));
% end

% % Display the results
% for i = 1:length(n_values)
%     disp(['n = ', num2str(n_values(i)), ', I = ', num2str(I_values(i))])
% end

% % Define the correct value of the integral
% I_correct = -1.4260247818;

% % Calculate the absolute errors
% errors = abs(I_values - I_correct);

% % Display the errors
% for i = 1:length(n_values)
%     disp(['n = ', num2str(n_values(i)), ', error = ', num2str(errors(i))])
% end

% % Define the adaptive quadrature algorithm
% function I = adquad(a, b, er, Simpson)
% I1 = Simpson(a, b);
% I2 = Simpson(a, (a + b)/2) + Simpson((a + b) / 2, b);
% if abs(I1 - I2) < 15 * er
%     I = I2;
% else
%     I = adquad(a, (a + b) / 2, er / 2, Simpson) + adquad((a + b) / 2, b, er / 2, Simpson);
% end
% end