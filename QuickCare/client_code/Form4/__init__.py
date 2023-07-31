from ._anvil_designer import Form4Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3')
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form5')
    pass

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form6')
    pass

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form7')
    pass

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form8')
    pass

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form9')
    pass

  def button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form91')
    pass









