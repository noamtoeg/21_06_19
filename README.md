import os
'''
def main():
    print(os.getcwd())
    fileEnding = 'txt'
    file = input('Input a file name: ')
    for dirpath, dirnames, filenames in os.walk(r'C:\\users'):
        for i in filenames:
#            print(i)
            if i == file:
                print(dirpath)

        for oneFile in filenames:

            if os.path.splitext(oneFile)[1] == fileEnding:
                print(oneFile)

#    filetype = input('enter a file type: ')
main()
'''
class Size:
    def biggestX():
        max = -1
        file_max_name = 'not found...'
        print(os.getcwd())
        for dirpath, dirnames, filenames in os.walk(r'C:\Users\rubi\.PyCharmCE2019.1'):
            for one_file in filenames:
                size_of_file = os.stat(os.path.join(dirpath, one_file)).st_size
                if size_of_file > max:
                    max = size_of_file
                    file_max_name = one_file
        print(f'Biggest file : {file_max_name} [{max}]')
        
biggestX()

def searchTXT():
    search_for_ext = '.txt'
    for dirpath, dirnames, filenames in os.walk(r'C:\Users\rubi\.PyCharmCE2019.1'):
        for one_file in filenames:
            if os.path.splitext(one_file)[1] == \
                    search_for_ext:
                print(one_file)

searchTXT()


