

'''You need to make a back button for a browser.
You use a stack to store the website links visited. Each new link visited is pushed onto the stack.
The back button needs to pop the top link from the stack and navigate to it.

The given code declares a Browser class as a stack and implements some of its methods. Then, some links are pushed onto the stack.
A while loop is then used to go back to all links and print them.

Implement the required pop() method for the Browser, so that the given code works as expected.'''


class Browser:
    def __init__(self):
        self.links = []

    def is_empty(self):
        return self.links== []

    def link_visited(self,link):

        self.links.insert(0,link)

    def back_button(self):
        return self.links.pop(0)

    def print_browser(self):
        print(self.links)


browser1 = Browser()
browser1.is_empty()
browser1.link_visited("www.google.com")
browser1.link_visited("www.myntra.com")
browser1.link_visited("www.udemy.com")
browser1.link_visited("www.linkedin.com")
browser1.print_browser()
# browser1.back_button()
# browser1.back_button()
# browser1.print_browser()


#when back button is pressed ,it should go to that link
while not browser1.is_empty():
     print(browser1.back_button())

#o/p was --
['www.linkedin.com', 'www.udemy.com', 'www.myntra.com', 'www.google.com']
www.linkedin.com
www.udemy.com
www.myntra.com
www.google.com





