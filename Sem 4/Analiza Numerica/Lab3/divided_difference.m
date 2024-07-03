function divided_diff_value = divided_difference(x, f)
    % Check if the inputs are valid
    if ~isa(f, 'function_handle')
        error('Input f must be a function handle.');
    end
    
    % Initialize the divided difference value
    divided_diff_value = f(x);
end
