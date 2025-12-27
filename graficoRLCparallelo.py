import matplotlib.pyplot as plt
import numpy as np

# Impostazione del tempo
t = np.linspace(0, 20, 1000)
V_g = 0.8
# Parametri fissi
omega0 = 1.0  # Pulsazione naturale (rad/s)
# Assumiamo V/L = 1 per normalizzare l'ampiezza

# --- 1. NON SMORZATA (R = 0 -> alpha = 0) ---
# Condizione: alpha = 0
# Soluzione: oscillazione perenne a omega0
#i_undamped = np.sin(omega0 * t)

# --- 2. SOTTOSMORZATA (R bassa) ---
# Condizione: alpha < omega0 (Delta < 0)
alpha_under = 0.85
# Pulsazione smorzata wd = sqrt(omega0^2 - alpha^2)
wd = np.sqrt(omega0**2 - alpha_under**2)
# i(t) = (V/L) * (1/wd) * e^(-alpha*t) * sin(wd*t)
i_under = (1.0 / wd) * np.exp(-alpha_under * t) * np.sin(wd * t) + V_g

alpha_under_1 = 0.2
# Pulsazione smorzata wd = sqrt(omega0^2 - alpha^2)
wd_1 = np.sqrt(omega0**2 - alpha_under_1**2)
# i(t) = (V/L) * (1/wd) * e^(-alpha*t) * sin(wd*t)
i_under_1 = (1.0 / wd_1) * np.exp(-alpha_under_1 * t) * np.sin(wd_1 * t) + V_g

# --- 3. SMORZAMENTO CRITICO (R critica) ---
# Condizione: alpha = omega0 (Delta = 0)
alpha_crit = omega0
# i(t) = (V/L) * t * e^(-alpha*t)
i_critical = 1.0 * t * np.exp(-alpha_crit * t) + V_g

# --- 4. SOVRASMORZATA (R alta) ---
# Condizione: alpha > omega0 (Delta > 0)
alpha_over = 2.0
# Radici reali distinte s1, s2
# delta_rad = sqrt(alpha^2 - omega0^2)
delta_rad = np.sqrt(alpha_over**2 - omega0**2)

# Possiamo scriverla come seno iperbolico per simmetria con la sottosmorzata
# i(t) = (V/L) * (1/delta_rad) * e^(-alpha*t) * sinh(delta_rad*t)
i_over = (1.0 / delta_rad) * np.exp(-alpha_over * t) * np.sinh(delta_rad * t) + V_g


# --- Creazione del Grafico ---
fig= plt.figure(figsize=(10, 6))

#plt.plot(t, i_undamped, label=r'Non Smorzata ($\alpha = 0$)', color='green', linestyle=':', alpha=0.6)
plt.plot(t, i_under_1, color='blue', linestyle=':', label= r'Sottosmorzata ($\alpha = 0.2\omega_0$)',linewidth=2)
plt.plot(t, i_under, label=r'Sottosmorzata ($\alpha = 0.85 \omega_0$)', color='blue', linewidth=2)
plt.plot(t, i_critical, label=r'Critica ($\alpha = \omega_0$)', color='red', linewidth=2, linestyle='--')
plt.plot(t, i_over, label=r'Sovrasmorzata ($\alpha > \omega_0$)', color='orange', linewidth=2)
plt.plot(t, [V_g for x in t], color='black', linestyle='--', linewidth = 1)
plt.text(0.25,0.75, 'I_g'),

# Abbellimenti
plt.title(r'Risposta RLC parallelo al gradino: confronto su $\alpha$ e $\omega_0$', fontsize=14)
plt.xlabel('Tempo (s)', fontsize=12)
plt.ylabel('Corrente sull\'induttore(t) (A)', fontsize=12)

# Assi e Griglia
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(0, 18)
plt.ylim(0.0, 1.6)

# Legenda con formule
plt.legend(fontsize=12, loc='upper right')

# Salvataggio
plt.savefig('rlc_alpha_omega.png', dpi=300, bbox_inches='tight')
plt.show()
