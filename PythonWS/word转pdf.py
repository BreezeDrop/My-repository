import os
from docx2pdf import convert

def batch_convert_docx_to_pdf(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 获取所有的 .docx 文件路径
    docx_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.docx')]
    
    # 转换每一个 .docx 文件为 .pdf
    for docx_file in docx_files:
        # 确定输出路径
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(docx_file))[0] + '.pdf')
        # 调用docx2pdf进行转换
        convert(docx_file, output_file)
        print(f"Converted {docx_file} to {output_file}")

# 使用示例
input_folder = "path/to/your/docx/files"
output_folder = "path/to/save/pdf/files"
batch_convert_docx_to_pdf(input_folder, output_folder)
