"""
Conversion of Omni-Notes java version to python.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, RIGHT
from toga.constants import BLUE


class OmniNotesPython(toga.App):
    fCount = 0
    mCount = 0
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        
        search_icon = toga.icons.Icon("search_icon.png",system=False) 
        filter_icon = toga.icons.Icon("filter_icon.png",system=False) 
        more_icon = toga.icons.Icon("more_icon.png",system=False) 
        addNote_icon = toga.icons.Icon("addNote_img.png",system=False) 
        
        filter_container = toga.Selection(items=['Title','Creation Date', 'Last Modified Date', 'Reminder Date'])
        
        more_container = toga.Selection(items=['Reduced View'])
        
        title_label = toga.Label(
            'Notes',
            style=Pack(padding=(0,5))
        )

        def search_action(widget):
            print("Searching")

        def filter_action(widget):
            self.fCount += 1
            if self.fCount % 2 == 1:            
                return toolbar_box.add(filter_container)
            else: 
                toolbar_box.remove(filter_container)
        
        def more_action(widget):
            self.mCount += 1
            if self.mCount % 2 == 1:            
                return toolbar_box.add(more_container)
            else: 
                toolbar_box.remove(more_container)
                
        def addNote_action(widget):
            print("Take to add note screen")
                
                
        toolbar_box = toga.Box(style=Pack(flex=0,direction=ROW,width=300,height=50))
        
        toolbar_grp: Group = toga.Group('Options') 
        
        filter_grp: Group = toga.Group('Filters') 
        
        search_cmd = toga.Command(
            search_action,
            label="Search",
            icon = search_icon,
            group = toolbar_grp,
        )
        
        filter_cmd = toga.Command(
            filter_action,
            label="Filter",
            icon = filter_icon,
            group = toolbar_grp,
        )
        
        more_cmd = toga.Command(
            more_action,
            label="More",
            icon = more_icon,
            group = toolbar_grp,           
        )
        
        addNote_btn = toga.Button(label='Add Note', on_press=addNote_action, style=Pack(
            flex=3,padding_top=80, padding_left=400, padding_right=20, width=50, height=50,alignment=RIGHT))
        
        note_count = 0
        nNotes_img = toga.ImageView(image="no_notesImg.png", id='no_notesImg', style=Pack(
            flex=1,padding_top=100, padding_left=270, padding_right=200, width=50, height=50))
            
        add_noteImg = toga.ImageView(image="add_noteImg.png", id='add_noteImg', style=Pack(
            flex=3,padding_top=150, padding_left=350, padding_right=20, width=50, height=50))
            
        main_box = toga.Box(style=Pack(direction=COLUMN))
        
        nNotes_txt = toga.Label('Nothing Here!', style=Pack(
            flex=2,padding_top=10,padding_left=260,padding_right=200,alignment=CENTER,direction=COLUMN))
        
        
        

        
        self.main_window = toga.MainWindow(title=self.formal_name)
        
        
        self.main_window.toolbar.add(search_cmd)
        self.main_window.toolbar.add(filter_cmd)
        self.main_window.toolbar.add(more_cmd)
        self.main_window.content = main_box
        main_box.add(toolbar_box)
        main_box.add(nNotes_img,nNotes_txt,addNote_btn)
        self.main_window.show()
     

def main():
    return OmniNotesPython()
