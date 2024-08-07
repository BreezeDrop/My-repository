import os
from docx2pdf import convert

def batch_convert_docx_to_pdf(docx_folder, pdf_folder):
    # 确保输出文件夹存在
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
    
    # 遍历docx文件夹中的所有文件
    for filename in os.listdir(docx_folder):
        if filename.endswith('.docx'):
            docx_path = os.path.join(docx_folder, filename)
            pdf_path = os.path.join(pdf_folder, filename.replace('.docx', '.pdf'))
            convert(docx_path, pdf_path)
            print(f"Converted {docx_path} to {pdf_path}")

# 示例用法
docx_folder = "path/to/your/docx_folder"  # 替换为你的docx文件夹路径
pdf_folder = "path/to/your/pdf_folder"    # 替换为你的pdf文件夹路径

batch_convert_docx_to_pdf(docx_folder, pdf_folder)