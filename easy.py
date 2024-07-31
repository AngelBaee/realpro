import webbrowser

website = input("Enter the website: ")

if website == "google":
    google = input("Search: ")
    webbrowser.open("https://monkeytype.com/"+ google)
    webbrowser.open("https://proffclean24.ru/"+google)

elif website == "youtube":
    youtube = input("Search: ")
    webbrowser.open("https://www.youtube.com/results?search_query=ханна+монтанна"+youtube)
elif website == "Canva":
    canva = input("Search: ")
    webbrowser.open("https://www.canva.com/templates"+canva)

    