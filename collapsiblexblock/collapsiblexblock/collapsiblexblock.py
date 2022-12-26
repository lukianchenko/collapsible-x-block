"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String


class CollapsibleXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.

    header = String(default="My xBlock", scope=Scope.user_state)
    content = String(default="Main text of the xBlock", scope=Scope.user_state)
    
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the CollapsibleXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/collapsiblexblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/collapsiblexblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/collapsiblexblock.js"))
        frag.initialize_js('CollapsibleXBlock')
        return frag

    
    @XBlock.json_handler
    def apply_data(self, data, suffix=''):

        self.header = data['headerText']   
        self.content = data['contentText']

        return {'header': self.header, 'content': self.content}
    

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("CollapsibleXBlock",
             """<collapsiblexblock/>
             """),
            ("Multiple CollapsibleXBlock",
             """<vertical_demo>
                <collapsiblexblock/>
                <collapsiblexblock/>
                <collapsiblexblock/>
                </vertical_demo>
             """),
        ]
