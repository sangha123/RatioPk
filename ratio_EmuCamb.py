import numpy,scipy,os,pylab,sys
from scipy.interpolate import spline

num=sys.argv[1]
char=sys.argv[2]
path='/Users/sanghamitradeb/CheckCambEmuratio/'
#filecamb_0=path+'Results_emuz_%s/Matter%s%s_matterpower_5.dat'%(char,num,num)
filecamb_0=path+'Matter%s%s_matterpower_5.dat'%(char,num)

kc_0,Pkc0=numpy.loadtxt(filecamb_0,unpack=True)
zcamb=numpy.loadtxt('MP.redshifts.base')


PkE_0=numpy.loadtxt(path+'empow_emuz%s.dat'%num)
kE=numpy.loadtxt(path+'kfile.dat')
zE=numpy.loadtxt(path+'zfile.dat')
par_0=numpy.loadtxt(path+'out_params_emuz_%s.dat'%num)
h=par_0[3]
nkE=kE.shape[0]

kc_0=kc_0*h
Pkc0=Pkc0/h**3

Pk_z0=PkE_0[0*nkE:(0+1)*nkE]

Pfunc_spl=scipy.interpolate.splrep(kc_0,Pkc0)
P_new=scipy.interpolate.splev(kE,Pfunc_spl)

Pratio_0=P_new/Pk_z0
sys.exit()
#next####################################################################

filecamb_1=path+'Results_emuz_%s/Matter_%s_matterpower_2.dat'%(num,num)

kc_1,Pkc1=numpy.loadtxt(filecamb_1,unpack=True)
zcamb_4=0.6666

kc_1=kc_1*h
Pkc1=Pkc1/h**3
idE_1=1333
Pk_z1=PkE_0[idE_1*nkE:(idE_1+1)*nkE]

Pfunc_spl=scipy.interpolate.splrep(kc_1,Pkc1)
P_new=scipy.interpolate.splev(kE,Pfunc_spl)

Pratio_1=P_new/Pk_z1

#next#######################################################################

filecamb_2=path+'Results_emuz_%s/Matter_%s_matterpower_3.dat'%(num,num)

kc_2,Pkc2=numpy.loadtxt(filecamb_2,unpack=True)
zcamb_3=0.25

kc_2=kc_0*h
Pkc2=Pkc0/h**3
idE_2=500
Pk_z2=PkE_0[idE_2*nkE:(idE_2+1)*nkE]

Pfunc_spl=scipy.interpolate.splrep(kc_2,Pkc2)
P_new=scipy.interpolate.splev(kE,Pfunc_spl)

Pratio_2=P_new/Pk_z2

#next##########################################################################

filecamb_3=path+'Results_emuz_%s/Matter_%s_matterpower_4.dat'%(num,num)

kc_3,Pkc3=numpy.loadtxt(filecamb_3,unpack=True)
zcamb_3=0.11111


kc_3=kc_0*h
Pkc3=Pkc0/h**3
idE_3=220
Pk_z3=PkE_0[idE_2*nkE:(idE_2+1)*nkE]

Pfunc_spl=scipy.interpolate.splrep(kc_3,Pkc3)
P_new=scipy.interpolate.splev(kE,Pfunc_spl)

Pratio_3=P_new/Pk_z3

filecamb_4=path+'Results_emuz_%s/Matter_%s_matterpower_1.dat'%(num,num)

kc_4,Pkc4=numpy.loadtxt(filecamb_3,unpack=True)
zcamb_4=1.0

kc_4=kc_0*h
Pkc3=Pkc0/h**3
idE_4=999
Pk_z4=PkE_0[idE_4*nkE:(idE_4+1)*nkE]

Pfunc_spl=scipy.interpolate.splrep(kc_4,Pkc4)
P_new=scipy.interpolate.splev(kE,Pfunc_spl)

Pratio_4=P_new/Pk_z4

pylab.semilogx(kE,Pratio_0,kE,Pratio_1,kE,Pratio_2)
pylab.xlim(0.004,1.0)
pylab.ylim(0.9,1.05)
#pylab.legend((zcamb_0),loc=3)
pylab.text(0.005,1.03,'M000')

pylab.savefig('pratio_emuz_%s'%num)
pylab.close()
