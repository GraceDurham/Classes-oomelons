"""This file should have our order classes in it."""


class AbstractMelonorder(object):
    def __init__(self, species, qty, tax, order_type):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type
  

    def get_total(self):
        """Calculate price."""
        base_price = 5
        flat_fee = 0

        if self.species == "Christmas melon":
            base_price = base_price * 1.5
        else:
            base_price

        if self.order_type == "international" and self.qty < 10:
            flat_fee = 3

        else: 
            flat_fee = 0

        total = ((1 + self.tax) * self.qty * base_price) + flat_fee
        return total  
        



    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True
        return self.shipped 


class DomesticMelonOrder(AbstractMelonorder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, 0.08, "domestic")
    
       


class InternationalMelonOrder(AbstractMelonorder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, 0.17, "international")
        self.country_code = country_code
    
   
        
        


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
