#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Data preparation
y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Plotting
plt.figure(figsize=(10, 8))
plt.suptitle('All in One')

# First subplot
plt.subplot(3, 2, 1)
plt.plot(y0, color='b')
plt.title('Cubic Numbers')
plt.xlabel('Index')
plt.ylabel('Value')

# Second subplot
plt.subplot(3, 2, 2)
plt.scatter(x1, y1, color='m', s=5)
plt.title('Random Multivariate Distribution', )
plt.xlabel('X')
plt.ylabel('Y')

# Third subplot
plt.subplot(3, 2, 3)
plt.plot(x2, y2)
plt.title('Exponential Decay')
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')

# Fourth subplot
plt.subplot(3, 2, 4)
plt.plot(x3, y31, label='t31 = 5730', linestyle='--')
plt.plot(x3, y32, label='t32 = 1600', linestyle='-')
plt.title('Exponential Decay Comparison')
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.legend(fontsize='x-small')

# Fifth subplot - Histogram
plt.subplot(3, 2, 5)
plt.hist(student_grades, bins=10, edgecolor='black')
plt.title('Student Grades Distribution')
plt.xlabel('Grades')
plt.ylabel('Number of Students')

# Sixth subplot spanning two columns
plt.subplot(3, 2, (5, 6))
plt.hist(student_grades, bins=10, edgecolor='black')
plt.title('Student Grades Distribution (Larger View)')
plt.xlabel('Grade')
plt.ylabel('Number of Students')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

