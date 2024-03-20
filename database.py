path = 'D:\Python\project\student_management_application\QLSV.txt'

def save(line):
    try:
        with open(path, 'a', encoding='utf8') as f:
            f.write(line)
            f.write('\n')
            f.close()
    except Exception as e:
        print(f"An error occurred while save: ", str(e))
    

def read():
    sv = []
    
    try:
        with open(path, 'r', encoding='utf8') as f:
            for item in f:
                data = item.strip()
                arr = data.split('-')
                sv.append(arr)
            f.close()
    except Exception as e:
        print("An error occurred while read: ", str(e))

    return sv