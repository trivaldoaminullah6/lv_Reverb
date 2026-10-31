import docx
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os, shutil

doc_path = 'E:/PROJEK_AI/Tugas Minggu 10-1/Laporan.docx'
out_path = 'E:/PROJEK_AI/Tugas Minggu 10-1/Laporan_Baru.docx'

doc = docx.Document(doc_path)

# Dark slightly grayish: #2D3748
DARK_GRAY = RGBColor(0x2D, 0x37, 0x48)

def format_run(run):
    run.font.name = 'Arial'
    run.font.color.rgb = DARK_GRAY
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:ascii'), 'Arial')
    rFonts.set(qn('w:hAnsi'), 'Arial')
    rFonts.set(qn('w:cs'), 'Arial')
    rFonts.set(qn('w:eastAsia'), 'Arial')

# Process document paragraphs
for p in doc.paragraphs:
    for run in p.runs:
        if run.text.strip():
            format_run(run)

# Process all tables and cells
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                for run in p.runs:
                    if run.text.strip():
                        format_run(run)

doc.save(out_path)
print("Saved to Laporan_Baru.docx successfully.")

# Attempt to overwrite Laporan.docx if unlocked
try:
    shutil.copyfile(out_path, doc_path)
    print("Directly overwritten Laporan.docx successfully.")
except PermissionError:
    print("Laporan.docx still locked by Word.")
