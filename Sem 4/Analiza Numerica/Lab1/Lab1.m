% 1.
% x=-1:0.01:1;
% T1=cos(acos(x));
% T2=cos(acos(x)*.2);
% T3=cos(acos(x)*.3);
% plot(x, T1)
% hold on
% plot(x, T2)
% plot(x, T3)

% 2.
% x=-1:0.01:1;
% T0=1;
% T1=x;
% for n=1:10
%     T2=2.*x.*T1-T0;
%     plot(x, T2)
%     hold on
%     T0=T1;
%     T1=T2;
% end

% 3.
% x=-1:0.01:3;
% f=exp(x);
% plot(x,f,'r')
% hold on
% for n=1:6
%     t=Lab1p3Taylor(n, x);
%     plot(x, t)
%     hold on
% end
% f2=exp(2);
% for n=1:6
%     t2=Lab1p3Taylor(n, 2); %function defined the same as the file
%     err=abs(f2-t2)
% end

% 4.
% x=-1:0.1:1;
% f=2.*x.^2+cos(3.*x);
% plot(x, f)
% hold on
% x0=0;
% fx0=1;
% fd1=4.*x0-3.*sin(3.*x0);
% fd2=4-9.*cos(3.*x0);
% T1=1;
% T2=1-5/2*x.^2;
% plot(x,T1);
% hold on
% plot(x, T2);

% 5.
% Remarks:
% h=0.2;
% x=zeros(1,5); % x is defined with 0 x=[0,0,0,0,0]
% for k=1:5 % the start index can't be 0 in matlab
%     x(k)=1+k*h;
%     % x is a vector => x=[x1, x2, x3, x4, x5]
% end
% x;
% y=sqrt(2*x.^2+3);
% x = 2:2:8;
% f = ([4,8,14,16]);
% k=1;
% for i=1:4
%     table(i, 1) = f(i);
% end
% for j=2:7
%     for i = 1:4-j+1
%         table(i,j) = (table(i+1, j-1) - table(i, j-1))/(x(i+k)-x(i));
%     end
%     k=k+1;
% end
% 
% for i=1:4
%     fprintf('\n %.4f',x(i));
%     for j = 1:4-i+1
%         fprintf('\t %.4f', table(i,j));
%     end
% end

