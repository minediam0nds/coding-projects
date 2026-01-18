this is my most recent project, i asked my father for ideas for coding projects and he told me i could try to help him with his US taxes

i was glad i got the oppourtinity to help my dad and use my coding skills for a practical task as almost all my previous projects were games

as much as i would like to include the entire set of files, they contain alot of private information (but heres a sample of page 1 of the 1041 form - https://cdn.prod.website-files.com/60a6b551be6130e4e5b19b98/67f97be5d584ef693a388ba9_1041-tax-form.png )
i also had to take out some keys from the dictionarys (dic0) for the same reason

the task revolves around three files: 
    the 1099 pdf (sent to account owner),
    the 1041 pdf (for the user to write on and send to the IRS), 
    and the spreadsheet (my father's spreadsheet to calculate the taxes) 


previously my father would manually type in the numbers from the 1099 onto the spreadsheet (a .xlsx file), and then input the numbers onto the 1041 pdf.
so i knew i would need to:
    1. extract the numbers from the pdf
    2. input the extracted numbers to the spreadsheet
    3. extract the calculated numbers from the spreadsheet
    4. write the extracted numbers from the spreadsheet onto the 1041 form
     
    everything on the 1099 and 1041 was always in the same place, so i considered their consistent postion when searching for python modules
    
i looked online for suitable python modules and ended up with these 4:
    pdfplumber (for extracting the numbers from the pfd)
    openpyxl (for inputing and extracting from xlsx cells)
    Pillow(PIL) (for writing the extracted numbers onto the 1041 png)
    PyMuPDF(fitz) (only used for turning the 1041 from .pdf to .png for PIL)

    originally i wanted a module to input directly to the 1041 pdf (it came with some input function), but it just didnt work

its worth noting that the most of the time i spent on this program was manually finding the coordinates for the 'bounding boxes', and the pixel coordinates for PIL to draw on through guess and check 


