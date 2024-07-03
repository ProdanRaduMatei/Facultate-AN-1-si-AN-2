% 1.
% % Define the function f(x) = cos(x)
% f = @(x) cos(x);
% 
% % Define the nodes
% x_nodes = [0, pi/2, pi, 3*pi/2, 2*pi];
% y_nodes = f(x_nodes);
% 
% % Define x value for evaluation
% x_eval = pi/4;
% 
% % Compute cubic natural spline
% spline_natural = spline(x_nodes, y_nodes);
% 
% % Compute cubic clamped spline
% spline_clamped = spline(x_nodes, [0, y_nodes, 0]); % Add zeros at endpoints for clamped spline
% 
% % Evaluate spline functions
% y_spline_natural = ppval(spline_natural, x_eval);
% y_spline_clamped = ppval(spline_clamped, x_eval);
% 
% % Evaluate original function
% y_original = f(x_eval);
% 
% % Plot the original function and splines
% x_interval = linspace(0, 2*pi, 1000);
% y_interval = f(x_interval);
% 
% figure;
% plot(x_interval, y_interval, 'b-', 'LineWidth', 2); % Original function
% hold on;
% plot(x_interval, ppval(spline_natural, x_interval), 'r--', 'LineWidth', 2); % Cubic natural spline
% plot(x_interval, ppval(spline_clamped, x_interval), 'g--', 'LineWidth', 2); % Cubic clamped spline
% scatter(x_nodes, y_nodes, 100, 'ko', 'filled'); % Nodes
% scatter(x_eval, y_original, 100, 'r', 'filled'); % Point of evaluation
% xlabel('x');
% ylabel('y');
% title('Comparison of Cubic Splines and Original Function');
% legend('Original Function', 'Cubic Natural Spline', 'Cubic Clamped Spline', 'Nodes', 'Evaluation Point', 'Location', 'best');
% grid on;
% hold off;

% 2.
% % Prompt the user to select 5 arbitrary points
% disp('Please select 5 arbitrary points in the plot window.');
% points = ginput(5);
% 
% % Extract x and y coordinates of selected points
% x_points = points(:, 1);
% y_points = points(:, 2);
% 
% % Compute cubic natural spline passing through the selected points
% spline_natural = spline(x_points, y_points);
% 
% % Plot the selected points
% figure;
% scatter(x_points, y_points, 100, 'r', 'filled');
% hold on;
% 
% % Plot the cubic natural spline function
% x_interval = linspace(min(x_points), max(x_points), 1000);
% y_spline_natural = ppval(spline_natural, x_interval);
% plot(x_interval, y_spline_natural, 'b-', 'LineWidth', 2);
% 
% xlabel('x');
% ylabel('y');
% title('Cubic Natural Spline through Selected Points');
% legend('Selected Points', 'Cubic Natural Spline', 'Location', 'best');
% grid on;
% hold off;

% 3.
% % Given data
% t = [0, 3, 5, 8, 13]; % time
% d = [0, 225, 383, 623, 993]; % distance
% s = [75, 77, 80, 74, 72]; % speed
% 
% % Compute the clamped cubic spline for distance
% spline_distance = spline(t, [75, d, 72]);
% 
% % Compute the clamped cubic spline for speed
% spline_speed = spline(t, s);
% 
% % Evaluate the splines at t = 10
% t_predict = 10;
% d_predict = ppval(spline_distance, t_predict);
% s_predict = ppval(spline_speed, t_predict);
% 
% % Display the predicted position and speed
% fprintf('Predicted position of the car at t = 10: %.2f\n', d_predict);
% fprintf('Predicted speed of the car at t = 10: %.2f\n', s_predict);

% 4.
% % Define the function f(x) = sin(2x)
% f = @(x) sin(2*x);
% 
% % Define nodes between 0 and 2*pi
% n = 9;
% x_nodes = linspace(0, 2*pi, n);
% 
% % Compute function values at each node
% y_nodes = f(x_nodes);
% 
% % Define the interval for plotting
% x_interval = linspace(0, 2*pi, 1000);
% 
% % Initialize the plot
% figure;
% plot(x_interval, f(x_interval), 'b-', 'LineWidth', 2); % Plot the function
% hold on;
% 
% % Compute and plot the linear spline on each interval
% for i = 1:n-1
%     % Compute the slope of the linear spline
%     slope = (f(x_nodes(i+1)) - f(x_nodes(i))) / (x_nodes(i+1) - x_nodes(i));
% 
%     % Compute the linear spline function on the interval
%     spline_func = f(x_nodes(i)) + slope * (x_interval - x_nodes(i));
% 
%     % Plot the linear spline function
%     plot(x_interval, spline_func, 'r--');
% end
% 
% % Plot nodes
% scatter(x_nodes, y_nodes, 100, 'ko', 'filled');
% 
% xlabel('x');
% ylabel('y');
% title('Function and Linear Spline');
% legend('Function f(x)', 'Linear Spline', 'Nodes', 'Location', 'best');
% grid on;
% hold off;