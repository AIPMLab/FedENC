import os
import csv

# 假设您的文件夹路径为 '/path/to/your/folder'
# folder_path = './results/OfficeHome/CPRA/FedAVG/lr=1e-3/'
# folder_path = './results/OfficeHome/CPRA/Ours/Original/lr=1e-3/twolayerMLP/MMDBased/'
# folder_path = './results/OfficeHome/CPRA/FedCLIP/lr=1e-3/'
# folder_path = './results/MultiImageNet/FedCLIP/lr=1e-3/'
# folder_path = './results/MultiImageNet/Ours/Original/lr=1e-3/twolayerMLP/MMDBased/'
# folder_path = './results/RealSkin/FedCLIP/lr=1e-3/'
# folder_path = './results/DomainNet/IPQRSC/Ours/Original/lr=1e-3/twolayerMLP(512)/KLBased/GeneralizationMatrix(PQRSCI)/(4-6)/'
# folder_path = './results/DomainNet/IPQRSC/Ours/Original/lr=5e-5/twolayerMLP(lr=1e-3)/KLBased/'
# folder_path = './results/OfficeHome/ACPR/pFedCLIP++/ViT-B-32/lr=5e-5/twolayerMLP(lr=1e-3)/KLBased/CorrectedOT/0-3/'
# folder_path = './results/DomainNet/CIPQRS/Ours/Original/lr=5e-5/twolayerMLP(lr=1e-3)/KLBased/ScalabilityV3/'
folder_path = ('./results/ISIC2019/IJCAI2026/FedCLIPNC/ViT-B-32/lr=5e-4/twolayerMLP(lr=1e-3)/Components/noAPT2/')
# folder_path = './results/OfficeHome/ACRP/promptFL/'
# folder_path = './results/miniDomainNet/IPQRSC/pFedCLIP++/ViT-B-32/lr=5e-5/twolayerMLP(lr=1e-3)/KLBased/'
# 初始化一个空列表来保存所有的第一列数值
values = []

files_to_process = [f for f in os.listdir(folder_path) if f.startswith('TestingMetrics') and f.endswith('.csv')]

# 对文件名进行排序，确保按照数字顺序读取
files_to_process.sort(key=lambda x: int(x.split('TestingMetrics')[1].split('.')[0]))

for filename in files_to_process:
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row:  # 确保行不为空
                first_column_value = row[0]
                # 将第一列的数值乘以100并保留两位小数，然后添加到列表中
                if int(first_column_value[0]) <= 1:
                    values.append(f"{float(first_column_value) * 100. :.2f}")
                else:
                    values.append(f"{float(first_column_value) :.2f}")

# 计算平均值并添加到列表中
# mean = sum(float(v) for v in values[:-1]) / len(values[:-1])
mean = sum(float(v) for v in values) / len(values)
# print(len(values))
values.append(str(round(mean, 2)))

# 将列表中的值用'&'连接起来
result = '&'.join(values)

print(result)


# 遍历文件夹中的所有文件
# for filename in os.listdir(folder_path):
#     # 检查文件名是否包含'TestingMetrics'并且以'.csv'结尾
#     if 'TestingMetrics' in filename and filename.endswith('.csv'):
#         # 构建完整的文件路径
#         file_path = os.path.join(folder_path, filename)
#         # 打开并读取csv文件
#         with open(file_path, 'r') as csvfile:
#             csvreader = csv.reader(csvfile)
#             # 读取第一列数据
#             for row in csvreader:
#                 if row:  # 确保行不为空
#                     print(row)
#                     first_column_value = row[0]
#                     # 将第一列的数值乘以100并保留两位小数，然后添加到列表中
#                     if int(first_column_value[0]) < 1:
#                         values.append(f"{float(first_column_value) * 100. :.2f}")
#                     else:
#                         values.append(f"{float(first_column_value) :.2f}")
#
# mean = 0
# for v in values:
#     mean += float(v)
# values.append(str(round(mean / 16, 2)))
# result = '&'.join(values)
#
# print(result)
