import numpy as np
import random
import matplotlib.pyplot as plt
import os
from google.colab import drive 

#drive.mount('/content/drive/')

os.chdir("/content/drive/My Drive/Lecture/Comphys/test")

def SIR(rho,t,param):
  rho_s=rho[0]
  rho_i=rho[1]
  rho_r=rho[2]

  beta=param[0]
  gamma=param[1]

  rho_st=-beta*rho_i*rho_s
  rho_it=beta*rho_i*rho_s-gamma*rho_i
  rho_rt=gamma*rho_i

  return np.array([rho_st,rho_it,rho_rt],float)

def RK4th(f,r,t,tau,param):
  c1=tau*f(r,t,param)
  c2=tau*f(r+c1*0.5,t+tau*0.5,param)
  c3=tau*f(r+c2*0.5,t+tau*0.5,param)
  c4=tau*f(r+c3,t+tau,param)

  return r+(c1+c2*2+c3*2+c4)/6.0

def solve_ode(f,x,y_init,param):
  h=abs(x[0]-x[1])
  y=np.zeros((len(x),len(y_init)),float)
  y[0]=y_init
  i=0
  for i in range(1,len(x)):
    y[i]=RK4th(f,y[i-1],x[i-1],h,param)

  return y

def numerical_gradient(f,f2,rho_init,dt,x,y,param):
    h=1e-4
    grad=np.zeros_like(param)

    for i in range(grad.size):
        tmp_val=param[i]
        param[i]=tmp_val+h
        fxh1=f(f2,rho_init,dt,x,y,param)

        param[i]=tmp_val-h
        fxh2=f(f2,rho_init,dt,x,y,param)

        grad[i]=(fxh1-fxh2)/(2*h)
        param[i]=tmp_val

    return grad

def gradient_decent(f,f2,rho_init,dt,x,y,init_param,eta=5e-5,step_num=100000,tol=1e-5):
    param=init_param
    
    chisq1=f(f2,rho_init,dt,x,y,param)
    for i in range(step_num):
        grad=numerical_gradient(f,f2,rho_init,dt,x,y,param)
        param-=eta*grad
        #rnd=random.random()
        #param-=eta*rnd*grad
        chisq2=f(f2,rho_init,dt,x,y,param)
        del_chisq=np.abs(chisq2-chisq1)
        #norm_grad=np.linalg.norm(grad)
        #if norm_grad<tol:
        if del_chisq<tol:
            return param
        chisq1=chisq2
    return param

def chi_square(f,rho_init,dt,init_x,init_y,param):
  x=init_x
  y=init_y
  chisq=0.0
  rho_res=np.copy(rho_init)
  for i in range(x.size):
    if i==0:
      xmin=0.0
    else:
      xmin=x[i-1]
    rho_res=f(rho_res,xmin,x[i],dt,param)
    chisq+=np.sum((y[i]-rho_res)**2)

  return chisq

def calc_rhos(rho,tmin,tmax,dt,param):
  nt=int((tmax-tmin)/dt)+1
  rho_calc=np.copy(rho)
  tt=tmin
  for i in range(1,nt):
    rho_calc=RK4th(SIR,rho_calc,tt,dt,param)
    tt+=dt
  return np.array(rho_calc,float)

# Load data

data=np.loadtxt("SIR_sample_data.dat",float)
t=data[:,0]
x=data[:,1]
y=data[:,2]
z=data[:,3]
xyz=data[:,1:]

beta=0.5
gamma=0.2
param=[beta,gamma]
rho_i0=0.001
rho_r0=0.0
rho_s0=1.0-rho_i0-rho_r0
rho_init=np.array([rho_s0,rho_i0,rho_r0])
dt=0.01

pguess=np.ones(2,float)
fitres=gradient_decent(chi_square,calc_rhos,rho_init,dt,t,xyz,pguess,eta=1e-01)
print("param=",fitres)
chi_res=chi_square(calc_rhos,rho_init,dt,t,xyz,fitres)
print(chi_res)

tmin=0.0
tmax=5.0

tt=np.linspace(tmin,tmax,1001)

rho_res=solve_ode(SIR,tt,rho_init,fitres)

rho_s=rho_res[:,0]
rho_i=rho_res[:,1]
rho_r=rho_res[:,2]

plt.plot(tt,rho_s,'r-')
plt.plot(tt,rho_i,'b-')
plt.plot(tt,rho_r,'k-')

plt.plot(t,x,'ro',mfc='none')
plt.plot(t,y,'bo',mfc='none')
plt.plot(t,z,'ko',mfc='none')
plt.show()