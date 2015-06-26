function dudt = f(u,t)

dudt = zeros(2,1);
a1 = 0.4;
a2 = 0.018;
b1 = 0.8;
b2 = 0.023;

dudt(1) = a1 * u(1) - a2 * u(1) * u(2);
dudt(2) = -b1 * u(2) + b2 * u(1) * u(2);

end
