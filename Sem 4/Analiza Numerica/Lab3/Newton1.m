function Nw = Newton1(y, x, f)
    p = 1;
    s = f(1);
    m = length(x);
    D = div_diff(x, f);
    for (i = 1 : m - 1)
        p = p * (y - x(i));
        s = s + p * D(1, i + 1);
    end
    Nw = s;
end