import numpy as np
import random
import matplotlib.pyplot as plt

def numerical_gradient(f,f2,x,y,sig,param):
    h=1e-4
    grad=np.zeros_like(param)

    for i in range(grad.size):
        tmp_val=param[i]
        param[i]=tmp_val+h
        fxh1=f(f2,x,y,sig,param)

        param[i]=tmp_val-h
        fxh2=f(f2,x,y,sig,param)

        grad[i]=(fxh1-fxh2)/(2*h)
        param[i]=tmp_val

    return grad

def gradient_decent(f,f2,x,y,sig,init_param,eta=5e-5,step_num=100000,tol=1e-5):
    param=init_param
    
    chisq1=chi_square(f2,x,y,sig,param)
    for i in range(step_num):
        grad=numerical_gradient(f,f2,x,y,sig,param)
        param-=eta*grad
        #param-=eta*random.random()*grad
        chisq2=chi_square(f2,x,y,sig,param)
        del_chisq=np.abs(chisq2-chisq1)
        #norm_grad=np.linalg.norm(grad)
        #if norm_grad<tol:
        if del_chisq<tol:
            return param
        chisq1=chisq2
    return param

def chi_square(f,init_x,init_y,init_sigma,param):
    x=init_x
    y=init_y
    sigma=init_sigma
    chisq=0.0
    for i in range(x.size):
        chisq+=((y[i]-f(x[i],param))/sigma[i])**2

    return chisq

def chi_square_nosigma(f,init_x,init_y,init_sigma,param):
    x=init_x
    y=init_y
    sigma=init_sigma
    chisq=0.0
    for i in range(x.size):
        chisq+=((y[i]-f(x[i],param)))**2

    return chisq

def func(x,param):
    y=param[0]*x**2+param[1]*x+param[2]
    return y

data=np.loadtxt("sample_data.dat",float)
x=data[:,0]
y=data[:,1]
sigma=data[:,2]

xx=np.linspace(-5.0,5.0,500)
pguess=np.ones(3,float)
fitres=gradient_decent(chi_square,func,x,y,sigma,pguess)
chi_res=chi_square(func,x,y,sigma,fitres)
print(fitres)
print("chi_sq=",chi_res)
yy=np.zeros(500,float)
i=0
for xxval in xx:
    yy[i]=func(xxval,fitres)
    i+=1


fitres2=gradient_decent(chi_square_nosigma,func,x,y,sigma,pguess)
chi_res_nosigma=chi_square_nosigma(func,x,y,sigma,fitres2)
print(fitres2)
print("chi_sq=",chi_res_nosigma)

yy2=np.zeros(500,float)
i=0
for xxval in xx:
    yy2[i]=func(xxval,fitres2)
    i+=1
   

plt.plot(x,y,'ko')
plt.plot(xx,yy,'b--')
plt.plot(xx,yy2,'r--')
plt.show()