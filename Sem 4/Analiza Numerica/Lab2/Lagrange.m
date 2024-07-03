function Lm = Lagrange(x, x_n, f_n)
    m = length(x_n);
    a = zeros(1, m);
    N = length(x);
    for j = 1:N
        s1 = 0;
        s2 = 0;
        for i = 1 : m
            a(i) = coeff_ai(x_n, i);
            s1 = s1 + a(i) * f_n(i) / (x(j) - x_n(i));
            s2 = s2 + a(i) / (x(j) - x_n(i));
        end
        Lm(j) = s1 / s2;
    end
end