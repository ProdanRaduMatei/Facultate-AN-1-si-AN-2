function ai=coeff_ai(x, i)
    m = length(x);
    p = 1;
    for j = 1 : m
        if j ~= i
            p = p * (x(i) - x(j));
        end
    end
    ai = 1 / p;
end