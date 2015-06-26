t0 = 0.0;
tf = 30;
n_pasos = 301;
tt = linspace(t0,tf,n_pasos);
u0 = [30.0, 4.0]';
EDIF = @(u,t) f(u,t);

u = lsode(EDIF,u0,tt);

figure(1)
plot(tt, u(:,1) , 'r', tt, u(:,2), 'b');
legend('X Presa', 'Y Predador');
xlabel('t');
ylabel('X, Y');
grid on;


figure(2)
plot(u(:,1), u(:,2));
legend('Diag Fase');
xlabel('X Presa');
ylabel('Y Predador');
grid on;


tabla = [transpose(tt),u];
csvwrite("out.csv", tabla);


