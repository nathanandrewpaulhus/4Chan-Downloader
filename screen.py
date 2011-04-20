import pygtk
pygtk.require('2.0')
import gtk
import downloader

class HelloWorld:

    def download(self,widget,entry,folder):
        downloader.download(entry.get_text(),folder.get_text())

    def delete_event(self,widget,event,data=None):
        print "delete event occured"
        return False
    
    def destroy(self,widget,data=None):
        gtk.main_quit()

    def __init__(self):

        window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        window.connect("delete_event",self.delete_event)
        window.connect("destroy",self.destroy)
        window.set_border_width(10)
        window.set_title("4chan Image Downloader")

        table = gtk.Table(5,2,True)
        
        pack = gtk.HBox(False,0)

        title = gtk.Label()
        title.set_markup("<big><big><big>4chan Image Downloader</big></big></big>")
       
        folder = gtk.Entry(max=0)
        folder.set_text("Enter the folder name here")
        
        url = gtk.Entry(max=0)
        url.set_text("Enter the thread URL here")

        confirm = gtk.Button("Begin Downloading")
        confirm.connect("clicked",self.download,url,folder)

        table.attach(title,0,5,0,1)
        table.attach(url,0,2,1,2)
        table.attach(folder,2,4,1,2)
        table.attach(confirm,4,5,1,2)
        
        pack.pack_start(table,True,True,0)
        
        window.add(pack)

        title.show()
        table.show()
        confirm.show()
        folder.show()
        url.show()
        pack.show()
        window.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()
