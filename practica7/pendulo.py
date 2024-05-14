from math import gamma, sin
import matplotlib.pyplot as plt

def f (gamma, omega, theta, thetapoint) :
	"""
	Fonction correpsondant à l'equation du pendule
	"""
	return -gamma*thetapoint-omega*sin(theta)



def euler(gamma, omega, theta, thetapoint, h, n, tableau_t, tableau_theta, tableau_theta_point) :
	for _ in range(n) :
		theta1 = theta+h*thetapoint
		thetapoint1 = thetapoint+h*f(gamma, omega, theta, thetapoint)
		theta = theta1
		thetapoint = thetapoint1
		tableau_t += [h]
		tableau_theta += [theta]
		tableau_theta_point += [thetapoint]
	return (tableau_theta, tableau_theta_point)

h=0.1
n=200


#entrées
print("Ecuacion θ\"+ Γθ'+ ω0²sinθ : ")
print("Entradas: Γ=0.5, ω=1, θ'(0)=0")

gamma=float(input("Introdusca el valor de la friccion Γ : "))
omega=float(input("Velocidad angular ω : "))
thetapoint=float(input("Introdusca θ'(0) : "))




#création et paramètrage de la figure
plt.figure()
plt.grid(True)
plt.xlim(-1,4)
plt.ylim(-2,2)
plt.xlabel('angle')
plt.ylabel('dangle')

#cálculo de diferentes curvas según valores theta
for theta in [0, 0.5, 1, 1.6, 2, 2.5, 3, 3.141592654]:
	tableau_t = [0]
	tableau_theta=[theta]
	tableau_theta_point=[thetapoint]
	tableau_theta, tableau_theta_point = euler(gamma, omega, theta, thetapoint, h, n, tableau_t, tableau_theta, tableau_theta_point)
	plt.plot(tableau_theta, tableau_theta_point)

#affichage des courbes
plt.show()
