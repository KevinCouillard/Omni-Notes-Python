#Conversion of Omni-Notes java version to python.

import toga
from toga.style import Pack
from toga.style.pack import *
from toga.constants import *

class OmniNotesPython(toga.App):
    #define constants used later
    fCount = 0
    mCount = 0
    svCount = 0
    sCount = 0
    newNoteCount = 0

    note1_title = ""
    note1_content = ""
    note2_title = ""
    note2_content = ""
    note3_title = ""
    note3_content = ""
    note4_title = ""
    note4_content = ""
    note5_title =""
    note5_content = ""
    note6_title = ""
    note6_content = ""
    note7_title = ""
    note7_content = ""
    note8_title = ""
    note8_content = ""
    note9_title = ""
    note9_content = ""
    note10_title = ""
    note10_content = ""

    #create app function
    def startup(self):

        #create main window
        self.main_window = toga.MainWindow(title=self.formal_name,size=(1200,800),resizeable=True)
        window_size = self.main_window.size
        window_width, window_height = window_size

        #
        def return_main(widget):
            if split.parent != main_box:
                main_box.remove(*main_box.children)
                main_box.add(split)

        toolbar_box = toga.Box(style=Pack(flex=0,direction=ROW,width=300,height=50,padding=10))
        main_box = toga.Box(style=Pack(direction=COLUMN,background_color=LIGHTBLUE, padding=15))
        search_box = toga.Box(style=Pack(direction=COLUMN,width=250,height=50,flex=1,padding=10))
        noNote_box = toga.Box(style=Pack(direction=COLUMN,alignment=RIGHT,flex=3,padding=10))
        note_box = toga.Box(style=Pack(direction=COLUMN,alignment=RIGHT,height=window_height/2,flex=3,padding=10))
        sideView_box = toga.Box(style=Pack(direction=COLUMN,alignment=LEFT,flex=2,padding=10,background_color=LIGHTYELLOW))
        options_box = toga.Box(style=Pack(direction=COLUMN, background_color=LIGHTYELLOW))
        addNote_box = toga.Box(style=Pack(direction=COLUMN, background_color=LIGHTYELLOW))
        display_note_box = toga.Box(style=Pack(direction=COLUMN, background_color=LIGHTYELLOW))

        options_box.add(toga.Button(label='Return', on_press=return_main,style=Pack(
        flex=0,padding=15, width=window_width/20, height=window_height/20,alignment=LEFT, background_color=LIGHTBLUE, color=ORANGE)))
        addNote_box.add(toga.Button(label='Return', on_press=return_main,style=Pack(
        flex=0,padding=15, width=window_width/20, height=window_height/20,alignment=LEFT, background_color=LIGHTBLUE, color=ORANGE)))
        display_note_box.add(toga.Button(label='Return', on_press=return_main,style=Pack(
        flex=0,padding=15, width=window_width/20, height=window_height/20,alignment=LEFT, background_color=LIGHTBLUE, color=ORANGE)))

        #adds search filter to note box
        def search_action(widget):
            self.sCount += 1
            if self.sCount % 2 == 1:
                search_box.add(input)
                search_box.refresh()
            else:
                search_box.remove(input)
                search_box.refresh()

        #adds note filter options to note box
        def filter_action(widget):
            self.fCount += 1
            if self.fCount % 2 == 1:
                toolbar_box.add(filter_container)
                toolbar_box.refresh()
            else:
                toolbar_box.remove(filter_container)
                toolbar_box.refresh()

        #adds more note filter to note box
        def more_action(widget):
            self.mCount += 1
            if self.mCount % 2 == 1:
                toolbar_box.add(more_container)
                toolbar_box.refresh()
            else:
                toolbar_box.remove(more_container)
                toolbar_box.refresh()

        #changes screen to options screen
        def openOptions_action(widget):
                if main_box == split.parent:
                    main_box.remove(split)
                    main_box.add(options_box)
                    main_box.refresh()
                else:
                    main_box.remove(options_box)
                    main_box.add(split)
                    main_box.refresh()

        #defines add note screen widgets
        input_note_title = toga.TextInput(id="note_title", placeholder='Enter Note Title Here!',style=Pack(direction=ROW,height=50,padding=15,flex=2,background_color=LIGHTBLUE))
        input_note_content = toga.TextInput(id="note_content", placeholder='Enter Note Content Here!',style=Pack(direction=ROW,height=100,padding=15,flex=3,background_color=LIGHTBLUE))
        addNote_label = toga.Label("", style=Pack(font_size=20, font_weight=BOLD, direction=ROW, padding=15, flex=1, text_align=LEFT, background_color=LIGHTYELLOW, color=ORANGE))

        # Originally the user would be able to set steps but this method wouldn't work in terms of actually adding textInputs
        # def checkList_num(stepNum):
        #     print(stepNum.value)
        #     if stepNum.value == 2:
        #         print("2")
        #         checkList_box.remove(noteFinal_btn)
        #         checkList_box.add(toga.TextInput(placeholder='Enter CheckList step 2', style=Pack(direction=ROW,height=100,width=window_width,padding=15)))
        #         checkList_box.add(noteFinal_btn)
        #         checkList_box.refresh()
        #     if stepNum.value == 3:
        #         print("3")
        #         addNote_box.add(toga.TextInput(placeholder='Enter CheckList step 2', style=Pack(direction=ROW,height=100,width=window_width,padding=15)))
        #         addNote_box.add(toga.TextInput(placeholder='Enter CheckList step 3', style=Pack(direction=ROW,height=100,width=window_width,padding=15)))
        #         addNote_box.refresh()
        #     if stepNum.value == 4:
        #         print("4")
        #         addNote_box.add(toga.TextInput(placeholder='Enter CheckList step 2', style=Pack(direction=ROW,height=100,width=window_width,padding=15)))
        #         addNote_box.add(toga.TextInput(placeholder='Enter CheckList step 3', style=Pack(direction=ROW,height=100,width=window_width,padding=15)))
        #         addNote_box.add(toga.TextInput(placeholder='Enter CheckList step 4', style=Pack(direction=ROW,height=100,width=window_width,padding=15)))
        #         addNote_box.refresh()
        #     if stepNum.value == 5:
        #         print("5")
        #         addNote_box.add(toga.TextInput(placeholder='Enter CheckList step 2', style=Pack(direction=ROW,height=100,width=window_width,padding=15)))
        #         addNote_box.add(toga.TextInput(placeholder='Enter CheckList step 3', style=Pack(direction=ROW,height=100,width=window_width,padding=15)))
        #         addNote_box.add(toga.TextInput(placeholder='Enter CheckList step 4', style=Pack(direction=ROW,height=100,width=window_width,padding=15)))
        #         addNote_box.add(toga.TextInput(placeholder='Enter CheckList step 5', style=Pack(direction=ROW,height=100,width=window_width,padding=15)))
        #         addNote_box.refresh()
        #
        # checkList_steps = toga.Selection(items=["2", "3", "4", "5"], style=Pack(direction=ROW, padding=15), on_select=checkList_num)
        # checkList_box = addNote_box = toga.Box(style=Pack(direction=COLUMN, background_color=LIGHTYELLOW,width=window_width,height=window_height))

        #default created 5 lists to for creating checklist
        listItem_1 = toga.TextInput(placeholder='Enter CheckList step 1', style=Pack(direction=ROW,height=20,width=window_width,padding=15,flex=4,background_color=LIGHTBLUE))
        listItem_2 = toga.TextInput(placeholder='Enter CheckList step 2', style=Pack(direction=ROW,height=20,width=window_width,padding=15,flex=5,background_color=LIGHTBLUE))
        listItem_3 = toga.TextInput(placeholder='Enter CheckList step 3', style=Pack(direction=ROW,height=20,width=window_width,padding=15,flex=6,background_color=LIGHTBLUE))
        listItem_4 = toga.TextInput(placeholder='Enter CheckList step 4', style=Pack(direction=ROW,height=20,width=window_width,padding=15,flex=7,background_color=LIGHTBLUE))
        listItem_5 = toga.TextInput(placeholder='Enter CheckList step 5', style=Pack(direction=ROW,height=20,width=window_width,padding=15,flex=8,background_color=LIGHTBLUE))

        #opens addnote screen depending on note type selected
        def addNote_action(widget):
                if main_box == split.parent:
                    main_box.remove(split)
                    main_box.add(addNote_box)
                    main_box.refresh()
                    if addNote_selection.value == "TextNote":
                        addNote_label.text = "TextNote"
                        addNote_box.add(addNote_label,input_note_title,input_note_content,noteFinal_btn)
                        addNote_box.refresh()
                    if addNote_selection.value == "CheckList":
                        addNote_label.text = "CheckList"
                        addNote_box.add(addNote_label,input_note_title,listItem_1,listItem_2,listItem_3,listItem_4,listItem_5,noteFinal_btn)
                        addNote_box.refresh()
                    if addNote_selection.value == "Canvas":
                        addNote_label.text = "Canvas"
                        addNote_box.add(addNote_label,canvasNote,noteFinal_btn)
                        addNote_box.refresh()
                else:
                    main_box.remove(addNote_box)
                    main_box.add(split)
                    main_box.refresh()

        #Only way I can think of is stupid long -> would need count int and have limit on notes one can have. Also title and content variable for each note count.
        #If statement to check the current count and save title and content specific to count. Make toga btn instance and in if statement change button accordingly.
        #Each button has an id which will correlate and be used to check the count. Based on the count of the btn selected the specific title and content will be displayed
        def finish_note(widget):
            self.newNoteCount += 1
            main_box.remove(addNote_box)
            main_box.add(split)
            content_box.remove(noNote_box)
            if addNote_label.text == "TextNote":
                if self.newNoteCount == 1:
                    self.note1_title += input_note_title.value
                    self.note1_content += input_note_content.value
                if self.newNoteCount == 2:
                    self.note2_title += input_note_title.value
                    self.note2_content += input_note_content.value
                if self.newNoteCount == 3:
                    self.note3_title += input_note_title.value
                    self.note3_content += input_note_content.value
                if self.newNoteCount == 4:
                    self.note4_title += input_note_title.value
                    self.note4_content += input_note_content.value
                if self.newNoteCount == 5:
                    self.note5_title += input_note_title.value
                    self.self.note5_content += input_note_content.value
                if self.newNoteCount == 6:
                    self.note6_title += input_note_title.value
                    self.note6_content += input_note_content.value
                if self.newNoteCount == 7:
                    self.note7_title += input_note_title.value
                    self.note7_content += input_note_content.value
                if self.newNoteCount == 8:
                    self.note8_title += input_note_title.value
                    self.note8_content += input_note_content.value
                if self.newNoteCount == 9:
                    self.note9_title += input_note_title.value
                    self.note9_content += input_note_content.value
                if self.newNoteCount == 10:
                    self.note10_title += input_note_title.value
                    self.note10_content += input_note_content.value
            if addNote_label.text == "CheckList":
                if self.newNoteCount == 1:
                    self.note1_title += input_note_title.value
                    self.note1_content += listItem_1.value + "\n\n" +  listItem_2.value + "\n\n" + listItem_3.value + "\n\n" + listItem_4.value + "\n\n" + listItem_5.value
                if self.newNoteCount == 2:
                    self.note2_title += input_note_title.value
                    self.note2_content += listItem_1.value + "\n\n" +  listItem_2.value + "\n\n" + listItem_3.value + "\n\n" + listItem_4.value + "\n\n" + listItem_5.value
                if self.newNoteCount == 3:
                    self.note3_title += input_note_title.value
                    self.note3_content += listItem_1.value + "\n\n" +  listItem_2.value + "\n\n" + listItem_3.value + "\n\n" + listItem_4.value + "\n\n" + listItem_5.value
                if self.newNoteCount == 4:
                    self.note4_title += input_note_title.value
                    self.note4_content += listItem_1.value + "\n\n" +  listItem_2.value + "\n\n" + listItem_3.value + "\n\n" + listItem_4.value + "\n\n" + listItem_5.value
                if self.newNoteCount == 5:
                    self.note5_title += input_note_title.value
                    self.self.note5_content += listItem_1.value + "\n\n" +  listItem_2.value + "\n\n" + listItem_3.value + "\n\n" + listItem_4.value + "\n\n" + listItem_5.value
                if self.newNoteCount == 6:
                    self.note6_title += input_note_title.value
                    self.note6_content += listItem_1.value + "\n\n" +  listItem_2.value + "\n\n" + listItem_3.value + "\n\n" + listItem_4.value + "\n\n" + listItem_5.value
                if self.newNoteCount == 7:
                    self.note7_title += input_note_title.value
                    self.note7_content += listItem_1.value + "\n\n" +  listItem_2.value + "\n\n" + listItem_3.value + "\n\n" + listItem_4.value + "\n\n" + listItem_5.value
                if self.newNoteCount == 8:
                    self.note8_title += input_note_title.value
                    self.note8_content += listItem_1.value + "\n\n" +  listItem_2.value + "\n\n" + listItem_3.value + "\n\n" + listItem_4.value + "\n\n" + listItem_5.value
                if self.newNoteCount == 9:
                    self.note9_title += input_note_title.value
                    self.note9_content += listItem_1.value + "\n\n" +  listItem_2.value + "\n\n" + listItem_3.value + "\n\n" + listItem_4.value + "\n\n" + listItem_5.value
                if self.newNoteCount == 10:
                    self.note10_title += input_note_title.value
                    self.note10_content += listItem_1.value + "\n\n" +  listItem_2.value + "\n\n" + listItem_3.value + "\n\n" + listItem_4.value + "\n\n" + listItem_5.value
            addNote_box.remove(*addNote_box.children)
            note_box.add(toga.Button(label=input_note_title.value, on_press=open_note,style=Pack(
                padding=10, width=400,height=25,alignment=LEFT,background_color=LIGHTBLUE,color=ORANGE)))
            input_note_title.clear()
            input_note_content.clear()
            content_box.add(note_box,addNote_selection)
            content_box.refresh()
            note_box.refresh()
            main_box.refresh()

        #open note function (displays correct info for note selected)
        def open_note(openNote_btn):
            display_note_box.remove(*display_note_box.children)
            display_note_box.add(toga.Button(label='Return', on_press=return_main,style=Pack(
            flex=0,padding=15, width=window_width/20, height=window_height/20,alignment=LEFT,background_color=LIGHTBLUE)))
            main_box.remove(split)
            if openNote_btn.label == self.note1_title:
                display_note_box.add(toga.Label(self.note1_title, style=Pack(padding=15, height=50, width=window_width, alignment=LEFT, text_align=LEFT, font_weight=BOLD, font_size=35, background_color=LIGHTBLUE)))
                display_note_box.add(toga.Label(self.note1_content, style=Pack(padding=10, alignment=CENTER, width=window_width, height=window_height, text_align=CENTER, font_size=15, background_color=LIGHTBLUE)))
            if openNote_btn.label == self.note2_title:
                display_note_box.add(toga.Label(self.note2_title, style=Pack(padding=15, height=50, width=window_width, alignment=LEFT, text_align=LEFT, font_weight=BOLD, font_size=35, background_color=LIGHTBLUE)))
                display_note_box.add(toga.Label(self.note2_content, style=Pack(padding=10, alignment=CENTER, width=window_width, height=window_height, text_align=CENTER, font_size=15, background_color=LIGHTBLUE)))
            if openNote_btn.label == self.note3_title:
                display_note_box.add(toga.Label(self.note3_title, style=Pack(padding=20, height=50, width=window_width, alignment=LEFT, text_align=LEFT, font_weight=BOLD, font_size=35, background_color=LIGHTBLUE)))
                display_note_box.add(toga.Label(self.note3_content, style=Pack(padding=10, alignment=CENTER, width=window_width, height=window_height, text_align=CENTER, font_size=15, background_color=LIGHTBLUE)))
            if openNote_btn.label == self.note4_title:
                display_note_box.add(toga.Label(self.note4_title, style=Pack(padding=20, height=50, width=window_width, alignment=LEFT, text_align=LEFT, font_weight=BOLD, font_size=35, background_color=LIGHTBLUE)))
                display_note_box.add(toga.Label(self.note4_content, style=Pack(padding=10, alignment=CENTER, width=window_width, height=window_height, text_align=CENTER, font_size=15, background_color=LIGHTBLUE)))
            if openNote_btn.label == self.note5_title:
                display_note_box.add(toga.Label(self.note5_title, style=Pack(padding=20, height=50, width=window_width, alignment=LEFT, text_align=LEFT, font_weight=BOLD, font_size=35, background_color=LIGHTBLUE)))
                display_note_box.add(toga.Label(self.note5_content, style=Pack(padding=10, alignment=CENTER, width=window_width, height=window_height, text_align=CENTER, font_size=15, background_color=LIGHTBLUE)))
            if openNote_btn.label == self.note6_title:
                display_note_box.add(toga.Label(self.note6_title, style=Pack(padding=20, height=50, width=window_width, alignment=LEFT, text_align=LEFT, font_weight=BOLD, font_size=35, background_color=LIGHTBLUE)))
                display_note_box.add(toga.Label(self.note6_content, style=Pack(padding=10, alignment=CENTER, width=window_width, height=window_height, text_align=CENTER, font_size=15, background_color=LIGHTBLUE)))
            if openNote_btn.label == self.note7_title:
                display_note_box.add(toga.Label(self.note7_title, style=Pack(padding=20, height=50, width=window_width, alignment=LEFT, text_align=LEFT, font_weight=BOLD, font_size=35, background_color=LIGHTBLUE)))
                display_note_box.add(toga.Label(self.note7_content, style=Pack(padding=10, alignment=CENTER, width=window_width, height=window_height, text_align=CENTER, font_size=15, background_color=LIGHTBLUE)))
            if openNote_btn.label == self.note8_title:
                display_note_box.add(toga.Label(self.note8_title, style=Pack(padding=20, height=50, width=window_width, alignment=LEFT, text_align=LEFT, font_weight=BOLD, font_size=35, background_color=LIGHTBLUE)))
                display_note_box.add(toga.Label(self.note8_content, style=Pack(padding=10, alignment=CENTER, width=window_width, height=window_height, text_align=CENTER, font_size=15, background_color=LIGHTBLUE)))
            if openNote_btn.label == self.note9_title:
                display_note_box.add(toga.Label(self.note9_title, style=Pack(padding=20, height=50, width=window_width, alignment=LEFT, text_align=LEFT, font_weight=BOLD, font_size=35, background_color=LIGHTBLUE)))
                display_note_box.add(toga.Label(self.note9_content, style=Pack(padding=10, alignment=CENTER, width=window_width, height=window_height, text_align=CENTER, font_size=15, background_color=LIGHTBLUE)))
            if openNote_btn.label == self.note10_title:
                display_note_box.add(toga.Label(self.note10_title, style=Pack(padding=20, height=50, width=window_width, alignment=LEFT, text_align=LEFT, font_weight=BOLD, font_size=35, background_color=LIGHTBLUE)))
                display_note_box.add(toga.Label(self.note10_content, style=Pack(padding=10, alignment=CENTER, width=window_width, height=window_height, text_align=CENTER, font_size=15, background_color=LIGHTBLUE)))
            main_box.add(display_note_box)
            main_box.refresh()
            display_note_box.refresh()

        #finish note button
        noteFinal_btn = toga.Button(label='Add Note', on_press=finish_note,style=Pack(
            flex=10,padding=15, width=window_width/20, height=window_height/20,alignment=RIGHT,color=ORANGE))

        #create icons
        search_icon = toga.icons.Icon("search_icon.png",system=False)
        filter_icon = toga.icons.Icon("filter_icon.png",system=False)
        more_icon = toga.icons.Icon("more_icon.png",system=False)
        addNote_icon = toga.icons.Icon("addNote_img.png",system=False)
        sideView_icon = toga.icons.Icon("sideView_icon.png",system=False)

        #create filter container (no backend)
        filter_container = toga.Selection(items=['Title','Creation Date', 'Last Modified Date', 'Reminder Date'])

        #create more option container
        more_container = toga.Selection(items=['Reduced View'])

        #create title label
        title_label = toga.Label(
            'Notes',
            style=Pack(padding=(0,5))
        )

        #create search filter
        input = toga.TextInput(placeholder='Enter keyword(s) here', style=Pack())

        #create/setup main note box/elements
        content_box = toga.Box(style=Pack(direction=COLUMN,background_color=LIGHTYELLOW))

        addNote_selection = toga.Selection(style=Pack(
            flex=3, width=200, padding_left=note_box.style.width+100, padding_top=note_box.style.height+6,padding_bottom=0,alignment=RIGHT),items=["Photo", "CheckList", "TextNote", "Canvas"], on_select=addNote_action)

        #track number of notes variable
        note_count = 0
        nNotes_img = toga.ImageView(image="no_notesImg.png", id='no_notesImg', style=Pack(
            flex=1, padding_left=note_box.style.width, padding_top=50, padding_bottom=0, width=50, height=50,alignment=CENTER))

        #create split to be sidebar
        left_container = sideView_box
        right_container = content_box
        split = toga.SplitContainer(style=Pack(padding=0))
        split.content = [left_container,right_container]

        #configure and add sidebar/main note box to main window
        content_box.add(toolbar_box)
        content_box.add(search_box)
        content_box.add(noNote_box)
        left_container.style.visibility=HIDDEN
        main_box.add(split)
        content_box.refresh()

        nNotes_txt = toga.Label('Nothing Here!', style=Pack(
            flex=2,padding_top=10,padding_left=note_box.style.width-10, padding_right=note_box.style.width,alignment=CENTER,direction=COLUMN))

        noNote_box.add(nNotes_img,nNotes_txt,addNote_selection)
        noNote_box.refresh()

        sideView_content = toga.Box(style=Pack(direction=COLUMN))
        sideView_container = toga.ScrollContainer(content=sideView_content,vertical = True, horizontal = False,style=Pack(width=sideView_box.style.width))

        options_btn=toga.Button(label='Options', on_press=openOptions_action,style=Pack(width=sideView_box.style.width))
        sideView_content.add(options_btn)
        sideView_content.refresh()

        #function to show and remove sidebar
        def sideView_action(widget):
            self.svCount += 1
            if self.svCount % 2 == 1:
                sideView_box.width=window_width/2.1
                sideView_box.height=window_height
                left_container.style.visibility=VISIBLE
                sideView_box.add(sideView_container)
                sideView_box.refresh()
            else:
                left_container.style.visibility=HIDDEN
                sideView_box.remove(sideView_container)
                sideView_box.refresh()
                sideView_box.width=1
                sideView_box.height=1

        #create toolbar and note filter groups
        toolbar_grp: Group = toga.Group('Options')

        filter_grp: Group = toga.Group('Filters')

        #create respective commands
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

        #add commands to toolbar (adds elements as commands)
        self.main_window.toolbar.add(search_cmd)
        self.main_window.toolbar.add(filter_cmd)
        self.main_window.toolbar.add(more_cmd)
        self.main_window.toolbar.add(sideView_cmd)
        self.main_window.content = main_box
        self.main_window.show()

#Attempted to use this to layout CSS elements but can't use CSS objects. Suppose to be able to style toga objects with CSS yet not able to because toga objects
#do not have an intrinsic size. Thought I could at least use CSS nodes (boxes) to make a layout template but cannot add toga elements to CSS nodes (b/c can't set parent attribute)
#can take child.parent = self out and can add toga objects however the style options are still limited and don't offer much more than Pack.
#also could not style button with CSS as it said no intrinsic size & wouldnt let me set one. If I took out self.intrinsic from BoxNode would work but no real point.
    # class BoxNode:
    #     def __init__(self,style):
    #         self.parent = None
    #         self.children = []
    #         self.intrinsic = Size(self)
    #         self.layout = Box(self)
    #         self.style = style.copy(self)
    #
    #     def add(self, child):
    #         self.children.append(child)
    #         #child.parent = self
    #
    # class Page:
    #     def __init__(self, width, height):
    #         self.content_width = width
    #         self.content_height = height

def main():
    return OmniNotesPython()
