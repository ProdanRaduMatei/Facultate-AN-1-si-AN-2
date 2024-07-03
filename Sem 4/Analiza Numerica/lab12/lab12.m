% 1.
% Define the function and its derivative
f = @(x) sin(x) - x - 1;
df = @(x) cos(x) - 1;

% Define the initial guess, the precision, and the maximum number of iterations
x0 = pi/4;
e = 1e-4;
N = 100;

% Initialize the current guess
x = x0;

% Perform the Newton's method
for i = 1:N
    % Update the guess
    x_new = x - f(x)/df(x);
    
    % Check if the precision has been reached
    if abs(x_new - x) < e
        break
    end
    
    % Update the current guess
    x = x_new;
end

% Display the solution
disp('The solution of the equation is:')
disp(x)

% 2.
% % Define the function and its derivative
% omega = @(x) x - (4*sin(x) - pi)/5;
% domega = @(x) 1 - (4*cos(x))/5;

% % Define the initial guess and the number of iterations
% x0 = 1;
% iterations = 6;

% % Initialize the current guess
% x = x0;

% % Perform the Newton's method
% for i = 1:iterations
%     % Update the guess
%     x = x - omega(x)/domega(x);
% end

% % Display the position of the satellite
% disp('The position of the satellite is:')
% disp(x)

% 3.
% % Define the function
% f = @(x) x^3 - 2*x^2 - 1;

% % Define the initial points, the precision, and the maximum number of iterations
% x0 = 1;
% x1 = 2;
% e = 1e-4;
% N = 100;

% % Initialize the current and previous guesses
% x = x1;
% x_prev = x0;

% % Perform the secant method
% for i = 1:N
%     % Update the guesses
%     x_new = x - f(x)*(x - x_prev)/(f(x) - f(x_prev));

%     % Check if the precision has been reached
%     if abs(x_new - x) < e
%         break
%     end

%     % Update the current and previous guesses
%     x_prev = x;
%     x = x_new;
% end

% % Display the solution and the number of iterations
% disp('The solution of the equation is:')
% disp(x)
% disp('The number of iterations is:')
% disp(i)

% 4.
% % Define the function
% f = @(x) (x-2)^2 - 2*log(x);

% % Define the interval, the precision, and the maximum number of iterations
% a = 1;
% b = 2;
% e = 1e-4;
% N = 100;

% % Bisection method
% a_bis = a;
% b_bis = b;
% for i = 1:N
%     c_bis = (a_bis + b_bis)/2;
%     if f(c_bis) == 0 || (b_bis - a_bis)/2 < e
%         break
%     end
%     if sign(f(c_bis)) == sign(f(a_bis))
%         a_bis = c_bis;
%     else
%         b_bis = c_bis;
%     end
% end

% % False position method
% a_fp = a;
% b_fp = b;
% for j = 1:N
%     c_fp = b_fp - f(b_fp)*(b_fp - a_fp)/(f(b_fp) - f(a_fp));
%     if abs(f(c_fp)) < e
%         break
%     end
%     if sign(f(c_fp)) == sign(f(a_fp))
%         a_fp = c_fp;
%     else
%         b_fp = c_fp;
%     end
% end

% % Display the solutions and the number of iterations
% disp('Bisection method:')
% disp(['The solution of the equation is: ', num2str(c_bis)])
% disp(['The number of iterations is: ', num2str(i)])

% disp('False position method:')
% disp(['The solution of the equation is: ', num2str(c_fp)])
% disp(['The number of iterations is: ', num2str(j)])

% 5.
% % Define the function, its derivative, and the exact solution
% f = @(x) x - 1/5 * sin(x) - 1/2;
% df = @(x) 1 - 1/5 * cos(x);
% exact_solution = 0.61546850;

% % Define the initial points and the precision
% x0 = 0.5;
% x1 = 1;
% e = 1e-6;

% % Newton's method
% x = x0;
% i = 0;
% disp('Newton''s method:')
% while abs(f(x)) > e
%     x_new = x - f(x)/df(x);
%     error = abs(x_new - exact_solution);
%     i = i + 1;
%     disp(['Step ', num2str(i), ', x = ', num2str(x_new), ', error = ', num2str(error)])
%     x = x_new;
% end

% % Secant method
% x_prev = x0;
% x = x1;
% i = 0;
% disp('Secant method:')
% while abs(f(x)) > e
%     x_new = x - f(x)*(x - x_prev)/(f(x) - f(x_prev));
%     error = abs(x_new - exact_solution);
%     i = i + 1;
%     disp(['Step ', num2str(i), ', x = ', num2str(x_new), ', error = ', num2str(error)])
%     x_prev = x;
%     x = x_new;
% end

% % Bisection method
% a = x0;
% b = x1;
% i = 0;
% disp('Bisection method:')
% while (b - a)/2 > e
%     c = (a + b)/2;
%     if f(c) == 0
%         break
%     end
%     if sign(f(c)) == sign(f(a))
%         a = c;
%     else
%         b = c;
%     end
%     error = abs(c - exact_solution);
%     i = i + 1;
%     disp(['Step ', num2str(i), ', x = ', num2str(c), ', error = ', num2str(error)])
% end

% 6.
% % Define the function, its derivative, and the multiplicity
% alpha = 2;
% f = @(x) (x^2 - 1)^alpha * log(x);
% df = @(x) 2*alpha*(x^2 - 1)^(alpha-1)*log(x) + (x^2 - 1)^alpha/x;
% m = alpha + 1;

% % Define the initial point and the precision
% x0 = 0.8;
% e = 1e-10;

% % Standard Newton's method
% x = x0;
% i = 0;
% disp('Standard Newton''s method:')
% while abs(f(x)) > e
%     x_new = x - f(x)/df(x);
%     i = i + 1;
%     disp(['Step ', num2str(i), ', x = ', num2str(x_new)])
%     x = x_new;
% end

% % Modified Newton's method for roots of multiplicity m
% x = x0;
% i = 0;
% disp('Modified Newton''s method:')
% while abs(f(x)) > e
%     x_new = x - m*f(x)/df(x);
%     i = i + 1;
%     disp(['Step ', num2str(i), ', x = ', num2str(x_new)])
%     x = x_new;
% end

% 7.
% x0 = 0.5;
% precision = 1e-10;
% max_iterations = 100;

% fprintf('Fixed Point Iteration a: x_{k+1} = e^{-x_k}\n');
% x_a = x0;
% for k = 1:max_iterations
%     x_a_prev = x_a;
%     x_a = exp(-x_a);
%     error_a = abs(x_a - x_a_prev);
%     fprintf('Iteration %d: x = %.10f, error = %.10e\n', k, x_a, error_a);
%     if error_a < precision
%         fprintf('Converged to root %.10f after %d iterations\n', x_a, k);
%         break;
%     end
% end
% if k == max_iterations
%     fprintf('Did not converge after %d iterations\n', max_iterations);
% end

% fprintf('\nFixed Point Iteration b: x_{k+1} = (1 + x_k) / (e^{x_k} + 1)\n');
% x_b = x0;
% for k = 1:max_iterations
%     x_b_prev = x_b;
%     x_b = (1 + x_b) / (exp(x_b) + 1);
%     error_b = abs(x_b - x_b_prev);
%     fprintf('Iteration %d: x = %.10f, error = %.10e\n', k, x_b, error_b);
%     if error_b < precision
%         fprintf('Converged to root %.10f after %d iterations\n', x_b, k);
%         break;
%     end
% end
% if k == max_iterations
%     fprintf('Did not converge after %d iterations\n', max_iterations);
% end

% fprintf('\nFixed Point Iteration c: x_{k+1} = x_k + 1 - x_k e^{x_k}\n');
% x_c = x0;
% for k = 1:max_iterations
%     x_c_prev = x_c;
%     x_c = x_c + 1 - x_c * exp(x_c);
%     error_c = abs(x_c - x_c_prev);
%     fprintf('Iteration %d: x = %.10f, error = %.10e\n', k, x_c, error_c);
%     if error_c < precision
%         fprintf('Converged to root %.10f after %d iterations\n', x_c, k);
%         break;
%     end
% end
% if k == max_iterations
%     fprintf('Did not converge after %d iterations\n', max_iterations);
% end
