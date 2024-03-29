import numpy as np

def sigmoid(data):
    return 1.0 / (1.0 + np.exp(-data))

input_num = 25
out1_num = 15
out2_num = 7
out_num = 3

out_1 = [0.0] * out1_num  # 은닉층 1번째 15개
out_2 = [0.0] * out2_num  # 은닉층 2번째 7개
output = [0.0] * out_num
bias = 1.0
f = open("C:/Users/SeoJun/PycharmProjects/pythonProject3/weight.txt", 'r')
a = f.readline()
a = f.readline()
weight_in_to_hid1 = np.array(a.split(" ")[3:-1])
weight_in_to_hid1 = weight_in_to_hid1.reshape(out1_num,input_num)
a = f.readline()
weight_hid1_to_hid2 = np.array(a.split(" ")[3:-1])
weight_hid1_to_hid2 = weight_hid1_to_hid2.reshape(out2_num,out1_num)
a = f.readline()
weight_hid2_to_out = np.array(a.split(" ")[3:-1])
weight_hid2_to_out = weight_hid2_to_out.reshape(out_num,out2_num)
a = f.readline()
bias_1 = np.array(a.split(" ")[3:out1_num+3])
bias_2 = np.array(a.split(" ")[out1_num+3:out1_num+out2_num+3])
bias_3 = np.array(a.split(" ")[out1_num+out2_num+3:out1_num+out2_num+out_num+3])
f.close()
def forward_pass(data, w, b, out):
    for i in range(len(w)):
        for number in range(len(w[i])):
            out[i] += float(w[i][number]) * data[number]
        out[i] = sigmoid(out[i] + float(b[i]))
    return out
def Forward_pass(data, w1, w2, w3, b1,b2,b3):
    out_1 = forward_pass(data, w1, b1, [0.0] * out1_num)
    out_2 = forward_pass(out_1, w2, b2, [0.0] * out2_num)
    output = forward_pass(out_2, w3, b3, [0.0]*out_num)
    return output

print("1 :           2:           3 : ")
print("■■■■■    □■■■■   ■■■■■")
print("■□■□□    ■□■□■   □□□□□")
print("■□■□□    □□■□□   ■■■■■")
print("□□■□□    □□■□□   ■□□□□")
print("□□■□□    □□■□■   ■■■■■")
print("4 :           5 :            6:")
print("■■■■■    ■□□□■   ■□□■■")
print("■□□□□    ■■□□■   ■□□□■")
print("■■■■□    ■■■■■   ■■■■■")
print("■□□□□    ■■□□■   ■□□□■")
print("■■■■■    ■□□□■   ■□□■■")
input_data = [[1.0, 1.0, 1.0, 1.0, 1.0,
               1.0, 0.1, 1.0, 1.0, 0.1,
               1.0, 0.1, 1.0, 0.1, 0.1,  # T
               0.1, 0.1, 1.0, 0.1, 0.1,
               0.1, 0.1, 1.0, 0.1, 0.1],
              [0.1, 1.0, 1.0, 1.0, 1.0,
               1.0, 0.1, 1.0, 0.1, 0.1,
               0.1, 0.1, 1.0, 0.1, 0.1,  # T
               0.1, 0.1, 1.0, 0.1, 0.1,
               0.1, 0.1, 1.0, 0.1, 1.0],
              [1.0, 1.0, 1.0, 1.0, 1.0,
               0.1, 0.1, 0.1, 0.1, 0.1,
               1.0, 1.0, 1.0, 1.0, 1.0,  # E
               1.0, 0.1, 0.1, 0.1, 0.1,
               1.0, 1.0, 1.0, 1.0, 1.0],
              [1.0, 1.0, 1.0, 1.0, 1.0,
               1.0, 0.1, 0.1, 0.1, 0.1,
               1.0, 1.0, 1.0, 1.0, 0.1,  # E
               1.0, 0.1, 0.1, 0.1, 0.1,
               1.0, 1.0, 1.0, 1.0, 1.0],
              [1.0, 0.1, 0.1, 0.1, 1.0,
               1.0, 1.0, 0.1, 0.1, 1.0,
               1.0, 1.0, 1.0, 1.0, 1.0,  # H
               1.0, 1.0, 0.1, 0.1, 0.1,
               1.0, 0.1, 0.1, 1.0, 1.0],
              [1.0, 0.1, 0.1, 1.0, 1.0,
               1.0, 0.1, 0.1, 0.1, 1.0,
               1.0, 1.0, 1.0, 1.0, 1.0,  # H
               1.0, 0.1, 0.1, 0.1, 1.0,
               1.0, 0.1, 0.1, 1.0, 1.0]
              ]

while True:
    i = int(input("실험할 데이터 선택 : "))
    a = Forward_pass(input_data[i-1],weight_in_to_hid1,weight_hid1_to_hid2,weight_hid2_to_out,bias_1,bias_2,bias_3)
    Max = a[0]
    Max_num = 0
    for j in range(len(a)-1):
        if(Max < a[j+1]):
            Max = a[j+1]
            Max_num = j+1
    if(Max_num == 0):
        print("T")
    elif(Max_num == 1):
        print("E")
    elif(Max_num == 2):
        print("H")
