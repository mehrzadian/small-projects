from pytube import YouTube


def youTubeDownloader(withDescription, link, path="D:\\film\\youtube"):
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    print("Downloading...")
    yd.download(path)
    if withDescription == 1:
        describe(yt)


def describe(yt):
    print("Title: ", yt.title, end="\n\n\n")
    print("Length: ", yt.length, end='\n\n\n')
    print("Rates: ", yt.rating, end='\n\n\n')
    print("description: ", yt.description, end='\n\n\n')


link = input("Enter the link: ")
withDescription = int(input("if you want the description enter 1: "))
youTubeDownloader(withDescription, link)
