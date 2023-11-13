 #Quiz 12A
    def click(self):
        """Calls the action of clicking and changes the .is_on to True
        Toggle_Button -> None"""
        super().click()
        self.is_on = not self.is_on
