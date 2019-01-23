data = xlsread('datam.xlsx')
cpu = data(:,[3])
% cpu = diff(cpu)
time = 1:1:200
% plot(time, cpu)
m = armax(cpu,'na', 8, 'nc', 0)
cpu1 = predict(m, cpu, 10)
plot(cpu,'g')
hold on
plot(cpu1,'r')
grid
legend('Original Data','Forecasting Data ARMA(1,1)')