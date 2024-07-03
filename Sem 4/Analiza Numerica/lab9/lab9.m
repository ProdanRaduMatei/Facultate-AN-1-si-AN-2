% 1.
% % Define the matrix A
% A = [10 8 -2 7; 2 3 0 1; -3 2 6 9; 7 5 9 10];

% % Define the vector b
% b = [5; -8; 3; 12];

% % Solve the system Ax = b
% x = A\b;

% % Display the solution
% disp('The solution of the system is:')
% disp(x)

% % Calculate the conditioning number of A
% cond_A = cond(A);

% % Display the conditioning number
% disp('The conditioning number of the matrix A is:')
% disp(cond_A)

% % Define the vector b2
% b2 = [5.6; -8.2; 3.9; 12.4];

% % Solve the system Ax2 = b2
% x2 = A\b2;

% % Display the solution
% disp('The solution of the system is:')
% disp(x2)

% % Compute the input relative error
% input_relative_error = norm(b - b2) / norm(b);

% % Display the input relative error
% disp('The input relative error is:')
% disp(input_relative_error)

% % Compute the output relative error
% output_relative_error = norm(x - x2) / norm(x);

% % Display the output relative error
% disp('The output relative error is:')
% disp(output_relative_error)

% % Define the matrix A3
% A3 = [10 8.54 -2.13 7.2; 2.12 3.1 0.6 0.99; -3 1.83 5.7 9.1; 6.77 5.23 8.87 10];

% % Solve the system A3x3 = b
% x3 = A3\b;

% % Display the solution
% disp('The solution of the system is:')
% disp(x3)

% % Compute the input relative error
% input_relative_error = norm(A - A3) / norm(A);

% % Display the input relative error
% disp('The input relative error is:')
% disp(input_relative_error)

% % Compute the output relative error
% output_relative_error = norm(x - x3) / norm(x);

% % Display the output relative error
% disp('The output relative error is:')
% disp(output_relative_error)

% 2.
% % Define the values of n
% n_values = 10:15;

% % Initialize the conditioning numbers vector
% cond_numbers = zeros(size(n_values));

% % Calculate the conditioning numbers for each value of n
% for i = 1:length(n_values)
%     n = n_values(i);

%     % Define the vector tk
%     tk = 1 ./ (1:n);

%     % Create the Vandermonde matrix V1
%     V1 = fliplr(vander(tk));

%     % Calculate the conditioning number of V1
%     cond_numbers(i) = cond(V1);
% end

% % Display the conditioning numbers
% for i = 1:length(n_values)
%     disp(['n = ', num2str(n_values(i)), ', conditioning number = ', num2str(cond_numbers(i))])
% end

% 3.
% % Define the values of n
% n_values = 10:15;

% % Initialize the conditioning numbers vector
% cond_numbers = zeros(size(n_values));

% % Calculate the conditioning numbers for each value of n
% for i = 1:length(n_values)
%     n = n_values(i);

%     % Define the vector tk
%     tk = -1 + 2*(1:n)/n;

%     % Create the Vandermonde matrix V2
%     V2 = fliplr(vander(tk));

%     % Calculate the conditioning number of V2
%     cond_numbers(i) = cond(V2);
% end

% % Display the conditioning numbers
% for i = 1:length(n_values)
%     disp(['n = ', num2str(n_values(i)), ', conditioning number = ', num2str(cond_numbers(i))])
% end

% 4.
% Define the values of n
n_values = 10:15;

% Initialize the conditioning numbers vector
cond_numbers = zeros(size(n_values));

% Calculate the conditioning numbers for each value of n
for i = 1:length(n_values)
    n = n_values(i);
    
    % Create the Hilbert matrix Hn
    Hn = hilb(n);
    
    % Calculate the conditioning number of Hn
    cond_numbers(i) = cond(Hn);
end

% Display the conditioning numbers
for i = 1:length(n_values)
    disp(['n = ', num2str(n_values(i)), ', conditioning number = ', num2str(cond_numbers(i))])
end