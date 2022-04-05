from turtle import ht



# Given a string, where each seperate Li element are sperated by '+', this functions returns
# copy and pastable code for .html files.
def generateLiElement():

    inputString = input("Give me text: ")
    elements = inputString.split('+')
    htmlCode = ''

    for element in elements:
        htmlCode += f'<li>{element}</li>\n'
    
    print(htmlCode)


if __name__ == "__main__":
    generateLiElement();