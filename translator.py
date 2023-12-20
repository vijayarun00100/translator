from translate import Translator 
translator=Translator(to_lang='ja') 
_import=open('test.txt') 
print("the text from the file is: ",_import.read())
try:
    with open('test.txt',mode='r') as my_file:
        new=my_file.read()
        translation=translator.translate(new) 
        print("in japanese: ",translation)



except FileNotFoundError as e:
    print("check your file path!") 
