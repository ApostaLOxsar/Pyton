import math

n1 = int(input("������� ���������� �������� � 1�� ������ : "))
n2 = int(input("������� ���������� �������� � 2�� ������ : "))
n3 = int(input("������� ���������� �������� � 3�� ������ : "))

#��� ������� ��� ���������� ������ ������
c = math.ceil(n1 / 2) + math.ceil(n2 / 2) + math.ceil(n3 / 2)

print(f"����������� {c} ����")
