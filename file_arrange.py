import os



class SortDirectory:

    def __init__(self):
        self.directory = "C:\\Users\\pc\\Downloads"

    @property
    def itemsInDirectory(self):
        if os.path.isdir(self.directory):
            return os.listdir(self.directory)
        elif not os.path.isdir(self.directory):
            return "No such directory"

    
    def checkOrCreateDirectory(self, path):
        """Checking if the directory is created,
            if not create file"""

        if not os.path.isdir(f"C:\\Users\\pc\\{path}"):
            os.mkdir(f"C:\\Users\\pc\\{path}")

    
    def sortItems(self):
        if self.itemsInDirectory == "No such directory":
            return
        
        activate = True
        while activate:
            print('Sorting.....')
            for item in self.itemsInDirectory:
                
                if item.endswith('.mp4') or  item.endswith('.mkv'):
                    self.checkOrCreateDirectory("Videos\\Downloaded")
                    try:
                        os.replace(f"C:\\Users\\pc\\Downloads\\{item}", f"C:\\Users\\pc\\Videos\\Downloaded\\{item}")
                    except:
                        print("THE FILE IS IN USE")
                        activate = False

                elif item.endswith('.png') or item.endswith('.jpg'):
                    self.checkOrCreateDirectory("OneDrive\\Pictures\\Downloaded")
                    try:
                        os.replace(f"C:\\Users\\pc\\Downloads\\{item}", f"C:\\Users\\pc\\OneDrive\\Pictures\\Downloaded\\{item}")
                    except:
                        print("THE FILE IS IN USE")
                        activate = False
                
                elif item.endswith('.gif'):
                    self.checkOrCreateDirectory("OneDrive\\Pictures\\Gifs")
                    try:
                        os.replace(f"C:\\Users\\pc\\Downloads\\{item}", f"C:\\Users\\pc\\OneDrive\\Pictures\\Gifs\\{item}")
                    except:
                        print("THE FILE IS IN USE")
                        activate = False
            
                elif item.endswith('.mp3'):
                    self.checkOrCreateDirectory("Music\\Downloaded")
                    try:
                        os.replace(f"C:\\Users\\pc\\Downloads\\{item}", f"C:\\Users\\pc\\Music\\Downloaded\\{item}")
                    except:
                        print("THE FILE IS IN USE")
                        activate = False
                
                elif item.endswith('.pdf'):
                    self.checkOrCreateDirectory("OneDrive\\Documents\\Downloaded")
                    try:
                        os.replace(f"C:\\Users\\pc\\Downloads\\{item}", f"C:\\Users\\pc\\OneDrive\\Documents\\Downloaded\\{item}")
                    except:
                        print("THE FILE IS IN USE")
                        activate = False

            
if __name__ == '__main__':
    SortDirectory().sortItems()
