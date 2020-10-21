

class Verify:
    """
    Module to verify the gh type input
    """
    
    def __init__(self):
        self.types = ["Repositories", "Issues", "Wikis"]

    def verified_type(self, type):
        return type in self.types

    def verify_keywords(self, keywords):
        return isinstance(keywords, str)

    def verify_params(self, args):
        if self.verify_keywords(args[1]):
            if self.verified_type(args[2]):
                return True
            else:
                print("There is an error in the type of search. Please send Repositories, Issues or Wikis")
                return False
        else:
            print("There is an error in the Keywords. Please send words divided by commas in unicode type.")
            return False