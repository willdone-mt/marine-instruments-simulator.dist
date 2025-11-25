import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QTextBrowser, QSplitter
from PyQt5.QtCore import Qt
import markdown

class MarkdownViewer(QWidget):
    def __init__(self, root_dir):
        super().__init__()
        self.setWindowTitle("SIRENIA wiki")
        self.resize(900, 600)

        splitter = QSplitter(Qt.Horizontal)

        # Tree widget for folders/files
        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("Documentation Files")
        self.tree.itemClicked.connect(self.load_file)
        splitter.addWidget(self.tree)

        # Viewer
        self.viewer = QTextBrowser()
        splitter.addWidget(self.viewer)

        layout = QVBoxLayout()
        layout.addWidget(splitter)
        self.setLayout(layout)

        # Populate tree
        self.root_dir = root_dir
        self.populate_tree(self.root_dir, self.tree.invisibleRootItem())

    def populate_tree(self, directory, parent_item):
        for entry in sorted(os.listdir(directory)):
            path = os.path.join(directory, entry)
            if os.path.isdir(path):
                # Folder node
                folder_item = QTreeWidgetItem([entry])
                parent_item.addChild(folder_item)
                self.populate_tree(path, folder_item)  # recurse
            elif entry.endswith(".md"):
                # File node
                file_item = QTreeWidgetItem([entry])
                file_item.setData(0, Qt.UserRole, path)  # store full path
                parent_item.addChild(file_item)

    def load_file(self, item, column):
        path = item.data(0, Qt.UserRole)
        if path and os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            html = markdown.markdown(text, extensions=["fenced_code", "tables"])
            self.viewer.setHtml(html)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarkdownViewer("docs/wiki")  # root folder
    window.show()
    sys.exit(app.exec_())
