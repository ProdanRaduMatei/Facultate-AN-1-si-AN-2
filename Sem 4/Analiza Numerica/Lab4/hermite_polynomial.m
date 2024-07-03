% Hermite polynomial function
function h = hermite_polynomial(Q, t, i)
    h = 1;
    for j = 1:i-1
        h = h * (t - Q(2*j-1, 1));
    end
end