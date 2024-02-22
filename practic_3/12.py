# Task_12_Ekin_Viacheslaw


a_t_t, c_o_m_p, y_d_s, t_d, i_n_t = map(float, input().split())

c = ((c_o_m_p / a_t_t) * 100 - 30) / 20
y = ((y_d_s / a_t_t) - 3) * 1 / 4
t = (t_d / a_t_t) * 20
i = 2.375 - ((i_n_t / a_t_t) * 25)
pr = (((max(min(c, 2.375), 0) + max(min(y, 2.375), 0) + max(min(t, 2.375), 0) + max(min(i, 2.375), 0)) / 3) * 50)

print(pr)