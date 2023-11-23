import matplotlib.pyplot as plt

labels = ["gojek", "grab", "maxim"]  # Kategori
values = [0.390, 0.17, 0.436]  # Persentase

x = ["gojek", "grab", "maxim"]  # Nilai x
y = [0.390, 0.17, 0.436]  # Nilai y

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(30,15))

#Diagram Pie
ax1.pie(values, labels=labels, autopct='%1.1f%%')
ax1.set_title('Diagram Pie Ranking Aplikasi Pemesan Ojek Online') 

#Diagram Batang
ax2.bar(x, y)
ax2.set_title('Diagram Batang Ranking Aplikasi Pemesan Ojek Online')

plt.show()