"""
Conversion of Omni-Notes java version to python.
"""
import toga
from toga.style import Pack
from toga.style.pack import *
from toga.constants import *

class OmniNotesPython(toga.App):
    fCount = 0
    mCount = 0
    svCount = 0
    sCount = 0



    def startup(self):

        self.main_window = toga.MainWindow(title=self.formal_name,size=(1200,800),resizeable=True)
        window_size = self.main_window.size
        window_width, window_height = window_size

        def return_main(widget):
            if split.parent != main_box:
                main_box.remove(*main_box.children)
                main_box.add(split)

        def search_action(widget):
            print("Searching")
            self.sCount += 1
            if self.sCount % 2 == 1:
                return search_box.add(input)
            else:
                search_box.remove(input)

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

        def openOptions_action(widget):
                if main_box == split.parent:
                    main_box.remove(split)
                    main_box.add(options_box)
                else:
                    main_box.remove(options_box)
                    main_box.add(split)

        note_title = toga.TextInput(placeholder='Enter Note Title Here!',style=Pack(direction=ROW,height=50,width=window_width,padding=15,flex=1))
        note_content = toga.TextInput(placeholder='Enter Note Content Here!',style=Pack(direction=ROW,height=100,width=window_width,padding=15,flex=2))

        def finish_note(widget):
            nTitle = note_title.value
            nContent = note_content.value
            print(nTitle,nContent)
            main_box.remove(addNote_box)
            main_box.add(split)
            content_box.remove(noNote_box)
            note_box.add(toga.Button(label=nTitle, on_press=open_note,style=Pack(
                padding=10, width=400,height=100,alignment=LEFT)))
            content_box.add(note_box,addNote_selection)

        def open_note(widget):
            main_box.remove(split)

        noteFinal_btn = toga.Button(label='Add Note', on_press=finish_note,style=Pack(
            flex=3,padding=15, width=window_width/20, height=window_height/20,alignment=RIGHT))

        def addNote_action(widget):
                if main_box == split.parent:
                    main_box.remove(split)
                    main_box.add(addNote_box)
                    if addNote_selection.value == "TextNote":
                        addNote_box.add(note_title,note_content,noteFinal_btn)
                else:
                    main_box.remove(addNote_box)
                    main_box.add(split)

        search_icon = toga.icons.Icon("search_icon.png",system=False)
        filter_icon = toga.icons.Icon("filter_icon.png",system=False)
        more_icon = toga.icons.Icon("more_icon.png",system=False)
        addNote_icon = toga.icons.Icon("addNote_img.png",system=False)
        sideView_icon = toga.icons.Icon("sideView_icon.png",system=False)

        filter_container = toga.Selection(items=['Title','Creation Date', 'Last Modified Date', 'Reminder Date'])

        more_container = toga.Selection(items=['Reduced View'])

        title_label = toga.Label(
            'Notes',
            style=Pack(padding=(0,5))
        )

        input = toga.TextInput(placeholder='Enter keyword(s) here', style=Pack())

        content_box = toga.Box(style=Pack(direction=COLUMN,background_color=LIGHTGRAY,height=window_height,width=window_width))

        toolbar_box = toga.Box(style=Pack(flex=0,direction=ROW,width=300,height=50,padding=10))
        main_box = toga.Box(style=Pack(direction=COLUMN))
        search_box = toga.Box(style=Pack(direction=COLUMN,width=250,height=50,flex=1,padding=10))
        noNote_box = toga.Box(style=Pack(direction=COLUMN,alignment=RIGHT,width=250,height=400,flex=3,padding=10))
        note_box = toga.Box(style=Pack(direction=COLUMN,alignment=RIGHT,width=250,height=400,flex=3,padding=10))
        sideView_box = toga.Box(style=Pack(direction=COLUMN,alignment=LEFT,flex=2,padding=10,background_color=LIGHTGRAY))
        options_box = toga.Box(style=Pack(direction=COLUMN, background_color=LIGHTGRAY,width=window_width,height=window_height))
        addNote_box = toga.Box(style=Pack(direction=COLUMN, background_color=LIGHTGRAY,width=window_width,height=window_height))

        back_btn = toga.Button(label='Return', on_press=return_main,style=Pack(
            flex=0,padding=15, width=window_width/20, height=window_height/20,alignment=LEFT))

        options_box.add(back_btn)
        addNote_box.add(back_btn)

        addNote_selection = toga.Selection(style=Pack(
            flex=3,padding_top=80, padding_left=400, padding_right=20, width=100, height=100,alignment=RIGHT),items=["Photo", "CheckList", "TextNote", "Canvas"], on_select=addNote_action)

        note_count = 0
        nNotes_img = toga.ImageView(image="no_notesImg.png", id='no_notesImg', style=Pack(
            flex=1,padding_top=note_box.style.height/4, padding_left=note_box.style.width, padding_right=note_box.style.width, width=50, height=50,alignment=CENTER))

        add_noteImg = toga.ImageView(image="add_noteImg.png", id='add_noteImg', style=Pack(
            flex=3,padding_top=150, padding_left=note_box.style.width, padding_right=note_box.style.width, width=50, height=50))

        left_container = sideView_box
        right_container = content_box
        split = toga.SplitContainer(style=Pack(padding=0,width=window_width,height=window_height))
        split.content = [left_container,right_container]
        #split.SplitterWidth=0


        content_box.add(toolbar_box)
        content_box.add(search_box)
        content_box.add(noNote_box)
        left_container.style.visibility=HIDDEN
        main_box.add(split)


        nNotes_txt = toga.Label('Nothing Here!', style=Pack(
            flex=2,padding_top=10,padding_left=note_box.style.width-10, padding_right=note_box.style.width,alignment=CENTER,direction=COLUMN))

        noNote_box.add(nNotes_img,nNotes_txt,addNote_selection)


        sideView_content = toga.Box(style=Pack(direction=COLUMN))
        sideView_container = toga.ScrollContainer(content=sideView_content,vertical = True, horizontal = False,style=Pack(width=sideView_box.style.width))

        options_btn=toga.Button(label='Options', on_press=openOptions_action,style=Pack(width=sideView_box.style.width))
        sideView_content.add(options_btn)

        def sideView_action(widget):
            self.svCount += 1
            if self.svCount % 2 == 1:
                sideView_box.width=window_width/2.1
                sideView_box.height=window_height
                left_container.style.visibility=VISIBLE
                return sideView_box.add(sideView_container)
            else:
                left_container.style.visibility=HIDDEN
                sideView_box.remove(sideView_container)
                sideView_box.width=1
                sideView_box.height=1


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

        sideView_cmd = toga.Command(
            sideView_action,
            label="Side View",
            icon = sideView_icon,
            group = toolbar_grp,
        )

        self.main_window.toolbar.add(search_cmd)
        self.main_window.toolbar.add(filter_cmd)
        self.main_window.toolbar.add(more_cmd)
        self.main_window.toolbar.add(sideView_cmd)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return OmniNotesPython()
