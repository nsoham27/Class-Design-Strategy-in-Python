"""

@Author: Soham Naik
@Date: 27/12/2023
@Goal: To implement class Watch
Capture Real Life Product on Amazon.
URL: https://www.amazon.in/Seiko-Analog-Blue-Dial-Watch-SSK003K1/dp/B0B3GJYFQX/ref=sr_1_3?pf_rd_i=2563504031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=7f19059d-3702-426d-9150-4e9084e071fb&pf_rd_r=NRK1TVNWH3MJFMEPEYRP&pf_rd_s=merchandised-search-12&qid=1702952424&refinements=p_89%3ASeiko&s=watches&sr=1-3&th=1

Product Details:
    Brand: wtch_brand : str
    Manufacturer: wtch_manufacturer : str
    Model: wtch_model : str
    Product Dimensions: wtch_product_dimensions : Dimension(U)
    Batteries: wtch_nr_batteries: int
    item model number: wtch_nr_model: str
    special features: wtch_features: list of string[str]
    display type: wtch_dsp_type: str
    batteries included: wtch_are_batteries_included: bool
    batteries required, wtch_are_required: bool
    country of origin, wtch_country_of_origin: str
"""

import sys

class ProductDimension:
    """
    This class implement the Dimension of watch.
    @__init__(self, length: float, width: float, height: float, weight: float):
        Constructor
    @get_length(self):
        getter of attribute length.
    @get_width(self):
        getter of attribute width.
    @get_height(self):
        getter of attribute height.
    @get_weight(self):
        getter of attribute weight.

    --------------------------------

    @set_length(self):
        setter of attribute length.
    @set_width(self):
        setter of attribute width.
    @set_height(self):
        setter of attribute height.
    @set_weight(self):
        setter of attribute weight.
    """
    def __init__(
            self: object,
            length: float,
            width: float,
            height: float,
            weight: float
        ) -> None:

        """
        Constructor of ProductDimension class:
        @__init__(self, length: float, width: float, height: float, weight: float):
            @self: newly created class object of ProductDimension.
            @length: Client specified value for attribute length.
            @width: Client specified value for attribute width.
            @height: Client specified value for attribute height.
            @weight: Client specified value for attribute weight
        """

        if type(length) != float:
            raise TypeError("Bad type: length")
        if type(width) != float:
            raise TypeError("Bad type: width")
        if type(height) != float:
            raise TypeError("Bad type: height")
        if type(weight) != float:
            raise TypeError("Bad type: weight")
        
        if length <= 0.0:
            raise ValueError("Length must be positive.")
        if width <= 0.0:
            raise ValueError("width must be positive.")
        if height <= 0.0:
            raise ValueError("height must be positive.")
        if weight <= 0.0:
            raise ValueError("weight must be positive.")
        
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    #Getter Method
    def get_length(self: object) -> float:
        """
        Return the length attribute of the calling object.
        """
        return self.length
    
    def get_width(self: object) -> float:
        """
        Return the width attribute of the calling object.
        """
        return self.width
    
    def get_height(self: object) -> float:
        """
        Return the height attribute of the calling object.
        """
        return self.height
    
    def get_weight(self: object) -> float:
        """
        Return the weight attribute of the calling object.
        """
        return self.weight
    
    #Setter Method
    def set_length(self: object, new_length: float):
        """
        Sets the length attribute of the calling object to @new_length.
        Before setting: TypeCheck and ValueCheck is performed.

        """
        if type(new_length) != float:
            raise TypeError("Bad type: length")
        if new_length <= 0.0:
            raise ValueError("Length must be positive")
        self.length = new_length
    
    def set_width(self: object, new_width: float):
        """
        Sets the width attribute of the calling object to @new_width.
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_width) != float:
            raise TypeError("Bad type: width")
        if new_width <= 0.0:
            raise ValueError("Width must be positive")
        self.width = new_width
    
    def set_height(self: object, new_height: float):
        """
        Sets the height attribute of the calling object to @new_height.
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_height) != float:
            raise TypeError("Bad type: height")
        if new_height <= 0.0:
            raise ValueError("Height must be positive")
        self.height = new_height
    
    def set_weight(self: object, new_weight: float):
        """
        Sets the weight attribute of the calling object to @new_weight.
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_weight) != float:
            raise TypeError("Bad type: weight")
        if new_weight <= 0.0:
            raise ValueError("Weight must be positive")
        self.weight = new_weight
        
    
class Watch:
    """
    This class is implement the charachterstics of Watch.
    @__init__(
        self: object,
        wtch_brand: str
        wtch_manufacturer: str,
        wtch_model: str,
        wtch_product_dimensions: ProductDimension,
        wtch_nr_batteries: int,
        wtch_nr_model: str,
        wtch_features: list [str]
        wtch_dsp_type: str
        wtch_are_batteries_included: bool
        wtch_are_batteries_required: bool
        wtch_country_of_origin: bool
        ):
        Constructor

    @get_wtch_brand(self):
        getter of attribute wtch_brand
    @get_wtch_manufacturer(self):
        getter of attribute wtch_manufacturer
    @get_wtch_model(self):
        getter of attribute wtch_model
    @get_wtch_product_dimension(self):
        getter of attribute wtch_product_dimensions
    @get_wtch_nr_batteries(self):
        getter of attribute wtch_nr_batteries
    @get_wtch_nr_model(self):
        getter of attribute wtch_nr_model
    @get_wtch_features(self):
        getter of attribute wtch_features
    @get_wtch_dsp_type(self):
        getter of attribute wtch_dsp_type
    @get_wtch_are_batteries_included(self):
        getter of attribute wtch_are_batteries_included.
    @get_wtch_are_batteries_required(self):
        getter of attribute wtch_are_batteries_required.
    @get_wtch_country_of_origin(self):
        getter of attribute wtch_country_of_origin

    -----------------------------------------------------

    @set_wtch_brand(self, new_wtch_brand):
        setter of attribute wtch_brand
    @set_wtch_manufacturer(self, new_wtch_manufacturer):
        setter of attribute wtch_manufacturer
    @set_wtch_model(self, new_wtch_model):
        setter of attribute wtch_model
    @set_wtch_product_dimensions_length(self, new_length):
        setter of attribute wtch_product_dimensions->length
    @set_wtch_product_dimensions_width(self, new_width):
        setter of attribute wtch_product_dimensions->width
    @set_wtch_product_dimensions_height(self, new_height):
        setter of attribute wtch_product_dimensions->height
    @set_wtch_product_dimensions_weight(self, new_weight):
        setter of attribute wtch_product_dimensions->weight
    @set_wtch_product_dimensions_reset(self, new_length, new_width, new_height, new_weight):
        setter of attribute wtch_product_dimensions->(length, width, height, weight)
    @set_wtch_nr_batteries(self, new_wtch_nr_batteries):
        setter of attribute wtch_nr_batteries.
    @set_wtch_nr_model(self, new_wtch_nr_model):
        setter of attribute wtch_nr_model
    @set_wtch_features(self, new_wtch_features):
        setter of attribute wtch_features
    @set_wtch_dsp_type(self, new_wtch_dsp_type):
        setter of attribute wtch_dsp_type
    @set_wtch_are_batteries_included(self, new_wtch_are_batteries_included)
        setter of attribute wtch_are_batteries_included
    @set_wtch_are_batteries_required(self, new_wtch_are_batteries_required)
        setter of attribute wtch_are_batteries_required
    @set_wtch_country_of_origin(self, new_wtch_country_of_origin):
        setter of attribute wtch_country_of_orgin

    
    """
    def __init__(
            self: object,
            wtch_brand: str,
            wtch_manufacturer: str,
            wtch_model: str,
            wtch_product_dimensions: ProductDimension,
            wtch_nr_batteries: int,
            wtch_nr_model: str,
            wtch_features: list,
            wtch_dsp_type: str,
            wtch_are_batteries_included: bool,
            wtch_are_batteries_required: bool,
            wtch_country_of_origin: str
        )-> None:

        """
        @self: newly created class object of Watch
        @wtch_brand: Client specified value for attribute wtch_brand
        @wtch_manufacturer: Client specified value for attribute wtch_manufacturer
        @wtch_model: Client specified value for attribute wtch_model
        @wtch_product_diemsions: Client specified value for attribute wtch_product_dimensions
        @wtch_nr_batteries: Client specified value for attribute wtch_nr_batteries
        @wtch_nr_model: Client specified value for attribute wtch_nr_model
        @wtch_features: Client specified value for attribute wtch_features
        @wtch_dsp_type: Client Specified value for attribute wtch_dsp_type
        @wtch_are_batteries_included: Client specified value for attribute wtch_are_batteries_included
        @wtch_are_batteries_required: Client specified value for attribute wtch_are_batteries_required
        @wtch_country_of_origin: Client specified value for attribute wtch_country_of_origin
        """

        if type(wtch_brand) != str:
            raise TypeError("Bad type: Brand")
        if type(wtch_manufacturer) != str:
            raise TypeError("Bad type: Manufacturer")
        if type(wtch_model) != str:
            raise TypeError("Bad type: Model")
        if type(wtch_product_dimensions) != ProductDimension:
            raise TypeError("Bad type: Product dimension")
        if type(wtch_nr_batteries) != int:
            raise TypeError("Bad type: Number of batteries")
        if type(wtch_nr_model) != str:
            raise TypeError("Bad type: Number of model")
        if '__iter__' not in dir(type(wtch_features)):
            raise TypeError("Bad type: watch features must be iterable")
        for feature in wtch_features:
            if type(feature) != str:
                raise TypeError("Bad type: feature")
        if type(wtch_features) != list:
            raise TypeError("Bad type: Features")
        if type(wtch_dsp_type) != str:
            raise TypeError("Bad type: Display type")
        if type(wtch_are_batteries_included) != bool:
            raise TypeError("Bad type: Batteries included")
        if type(wtch_are_batteries_required) != bool:
            raise TypeError("Bad type: Batteries required")
        if type(wtch_country_of_origin) != str:
            raise TypeError("Bad type: Country of origin")
        
        if len(wtch_brand.strip()) == 0:
            raise ValueError("Watch brand cannot be empty.")
        if len(wtch_manufacturer.strip()) == 0:
            raise ValueError("Watch Manufacturer cannot be empty.")
        if len(wtch_model.strip()) == 0:
            raise ValueError("Watch model cannot be empty.")
        if wtch_nr_batteries <=0:
            raise ValueError("Number of batteries must be positive.")
        if len(wtch_nr_model.strip()) == 0 :
            raise ValueError("Model number cannot be empty.")
        for feature in wtch_features:
            if len(feature.strip()) == 0:
                raise ValueError("Watch feature cannot be empty")
        if len(wtch_dsp_type.strip()) == 0:
            raise ValueError("Display type cannot be empty.")
        if len(wtch_country_of_origin.strip()) == 0:
            raise ValueError("Country of origin cannot be empty.")
            


        self.wtch_brand = wtch_brand
        self.wtch_manufacturer = wtch_manufacturer
        self.wtch_model = wtch_model
        self.wtch_product_dimensions = wtch_product_dimensions
        self.wtch_nr_batteries = wtch_nr_batteries
        self.wtch_nr_model = wtch_nr_model
        self.wtch_features = wtch_features
        self.wtch_dsp_type = wtch_dsp_type
        self.wtch_are_batteries_included = wtch_are_batteries_included
        self.wtch_are_batteries_required = wtch_are_batteries_required
        self.wtch_country_of_origin = wtch_country_of_origin 

    
    #Getter Method
    def get_wtch_brand(self: object)-> str:
        """
            Returns the wtch_brand attribute of the calling object.
        """
        return self.wtch_brand
    
    def get_wtch_manufacturer(self: object)-> str:
        """
            Returns the wtch_manufacturer attribute of the calling object.
        """
        return self.wtch_manufacturer
    
    def get_wtch_model(self: object)-> str:
        """
            Returns the wtch_model attribute of the calling object.
        """
        return self.wtch_model
    
    def get_wtch_product_dimensions(self: object)-> tuple:
        """
            Returns the wtch_product_dimensions attribute of the calling object.
        """
        return (self.wtch_product_dimensions.length, self.wtch_product_dimensions.width, self.wtch_product_dimensions.height, self.wtch_product_dimensions.weight)
    
    def get_wtch_nr_batteries(self: object)-> int:
        """
            Returns the wtch_nr_batteries attribute of the calling object.
        """
        return self.wtch_nr_batteries
    
    def get_wtch_nr_model(self: object)-> str:
        """
            Returns the wtch_nr_model attribute of the calling object.
        """
        return self.wtch_nr_model
    
    def get_wtch_features(self: object)-> list:
        """
            Returns the wtch_features attribute of the calling object.
        """
        return self.wtch_features
    
    def get_wtch_dsp_type(self: object)-> str:
        """
            Returns the wtch_dsp_type attribute of the calling object.
        """
        return self.wtch_dsp_type
    
    def get_wtch_are_batteries_included(self: object)-> bool:
        """
            Returns the wtch_are_batteries_included attribute of the calling object.
        """
        return self.wtch_are_batteries_included
    
    def get_wtch_are_batteries_required(self: object)-> bool:
        """
            Returns the wtch_are_batteries_required attribute of the calling object.
        """
        return self.wtch_are_batteries_required
    
    def get_wtch_country_of_origin(self: object)-> str:
        """
            Returns the wtch_country_of_country attribute of the calling object.
        """
        return self.wtch_country_of_origin
    

    #Setter Methods
    def set_wtch_brand(self: object, new_wtch_brand: str):
        """
        Sets the wtch_brand attribute of the calling object to @new_wtch_brand
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_wtch_brand) != str:
            raise TypeError("Bad type: Brand")
        if len(new_wtch_brand.strip()) == 0:
            raise ValueError("Watch brand cannot be empty.")
        self.wtch_brand = new_wtch_brand
    
    def set_wtch_manufacturer(self: object, new_wtch_maufacturer: str):
        """
        Sets the wtch_manufacturer attribute of the calling object to @new_wtch_manufacturer
        Before setting: TypeCheck is performed.
        """
        if type(new_wtch_maufacturer) != str:
            raise TypeError("Bad type: Manufacturer")
        if len(new_wtch_maufacturer.strip()) == 0:
            raise ValueError("Watch manufacturer cannot be empty.")
        self.wtch_manufacturer = new_wtch_maufacturer
    
    def set_wtch_model(self: object, new_wtch_model: str):
        """
        Sets the wtch_model attribute of the calling object to @new_wtch_model
        Before setting: TypeCheck is performed.
        """
        if type(new_wtch_model) != str:
            raise TypeError("Bad type: Model")
        if len(new_wtch_model.strip()) == 0:
            raise ValueError("Watch model cannot be empty.")
        self.wtch_model = new_wtch_model
    
    def set_wtch_product_dimensions_length(self: object, new_length : float):
        """
        Sets the wtch_product_dimensions length attribute of the calling object to @new_length
        Before setting: TypeCheck is performed.
        """
        self.wtch_product_dimensions.set_length(new_length)
    
    def set_wtch_product_dimensions_width(self: object, new_width: float):
        """
        Sets the wtch_product_dimension width attribute of the calling object to @new_width
        Before setting: TypeCheck is performed.
        """
        self.wtch_product_dimensions.set_width(new_width)

    def set_wtch_product_dimensions_height(self: object, new_height: float):
        """
        Sets the wtch_product_dimensions height attribute of the calling object to @new_height
        Before setting: TypeCheck is performed.
        """
        self.wtch_product_dimensions.set_height(new_height)
    
    def set_wtch_product_dimensions_weight(self: object, new_weight: float):
        """
        Sets the wtch_product_dimension weight attribute of the calling object to @new_weight
        Before setting: TypeCheck is performed.
        """
        self.wtch_product_dimensions.set_weight(new_weight)
    
    def set_wtch_product_dimensions_reset(self: object, new_length: float, new_width: float, new_height: float, new_weight: float ):
        """
        Sets the wtch_product_dimensions attribute of the calling object to @new_length, @new_width, @new_height, @new_weight
        Before setting: TypeCheck is performed.
        """
        self.wtch_product_dimensions.set_length(new_length)
        self.wtch_product_dimensions.set_width(new_width)
        self.wtch_product_dimensions.set_height(new_height)
        self.wtch_product_dimensions.set_weight(new_weight)

    def set_wtch_nr_batteries(self: object, new_wtch_nr_batteries: int):
        """
        Sets the wtch_are_batteries attribute of the calling object to @new_wtch_nr_batteries
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_wtch_nr_batteries) != int:
            raise TypeError("Bad type: Number of batteries")
        if new_wtch_nr_batteries <=0 :
            raise ValueError("Number of batteries must be positive.")
        self.wtch_nr_batteries = new_wtch_nr_batteries
    
    def set_wtch_nr_model(self: object, new_wtch_nr_model: str):
        """
        Sets the wtch_nr_model attribute of the calling object to @new_wtch_nr_model
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_wtch_nr_model) != str:
            raise TypeError("Bad type: Number of model")
        if len(new_wtch_nr_model.strip()) == 0:
            raise ValueError("Model number cannot be empty.")
        self.wtch_nr_model = new_wtch_nr_model
    
    def set_wtch_features(self: object, new_wtch_features: list):
        """
        Sets the wtch_features attribute of the calling object to @new_wtch_features
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_wtch_features) != list:
            raise TypeError("Bad type: Watch feature")
        if '__iter__' not in dir(type(new_wtch_features)):
            raise TypeError("Bad type: Watch features must be iterable")
        if len(new_wtch_features) == 0:
            raise ValueError("Watch features cannot be empty.")
        
        for feature in new_wtch_features:
            if type(feature) != str:
                raise TypeError("Bad type: Watch feature")
            if len(feature.strip()) == 0:
                raise ValueError("Watch feature cannot be empty")
        
        self.wtch_features = new_wtch_features
    
    def set_wtch_dsp_type(self: object, new_wtch_dsp_type: str):
        """
        Sets the wtch_dsp_type attribute of the calling object to @new_wtch_dsp_type
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_wtch_dsp_type) != str:
            raise TypeError("Bad type: Watch display type")
        if len(new_wtch_dsp_type.strip()) == 0:
            raise ValueError("Watch display type cannot be empty")
        self.wtch_dsp_type = new_wtch_dsp_type
    
    def set_wtch_are_batteries_included(self: object, new_wtch_are_batteries_included: bool):
        """
        Sets the wtch_are_batteries_included attribute of the calling object to @new_wtch_are_batteries_included
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_wtch_are_batteries_included) != bool:
            raise type("Bad type: Batteries included")
        self.wtch_are_batteries_included = new_wtch_are_batteries_included
    
    def set_wtch_are_batteries_required(self: object, new_wtch_are_batteries_required: bool):
        """
        Sets the wtch_are_batteries_required attribute of the calling object to @new_wtch_are_batteries_required
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_wtch_are_batteries_required) != bool:
            raise type("Bad type: Batteries required")
        self.wtch_are_batteries_required = new_wtch_are_batteries_required

    def set_wtch_country_of_origin(self: object, new_wtch_country_of_origin: str):
        """
        Sets the wtch_country_of_origin attribute of the calling object to @new_wtch_country_of_origin
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_wtch_country_of_origin) != str:
            raise TypeError("Bad type: Country of origin")
        if len(new_wtch_country_of_origin.strip()) == 0:
            raise ValueError("Country of origin cannot be empty")
        
        self.wtch_country_of_origin = new_wtch_country_of_origin

    

    def show(self: object)->None:
        """
        This function display all the characterstics of Watch class.
        """
        
        for data in self.__dict__.keys():
            if type(self.__dict__[data]) == ProductDimension:
                print(data,"(L x W x H; wt(g)) -->", self.__dict__[data].length, "X",  self.__dict__[data].width, "X", self.__dict__[data].height, "; ", self.__dict__[data].weight)
            elif type(self.__dict__[data]) == list:
                print(data, "--> ", end="")
                for i in self.__dict__[data]:
                    print(i,"\t", end="")
                print("")
            elif type(self.__dict__[data]) == bool:
                if self.__dict__[data] == False:
                    print(data, "-->", "No")
                else:
                    print(data, "-->", "Yes")       
            else:
                print(data, "-->", self.__dict__[data])




def main()-> None:
    """
    This is the main function where the object is created by
    passing client specified attribute value as a actual parameter
    and display the final output.
    @input: passing client specified attribute value as a formal parameter to constructor of class Watch
        Watch(
            wtch_brand: str
            wtch_manufacturer: str,
            wtch_model: str,
            wtch_product_dimensions: ProductDimension,
            wtch_nr_batteries: int,
            wtch_nr_model: str,
            wtch_features: list [str]
            wtch_dsp_type: str
            wtch_are_batteries_included: bool
            wtch_are_batteries_required: bool
            wtch_country_of_origin: bool
        )
    """
    watch_obj = Watch(
        "Seiko",
        "Seiko",
        "SSK003k1",
        ProductDimension(30.5, 30.5, 35.5, 250.5),
        1,
        "SSK003K1",
        ["Calculator", "Dual Time", "Glow in the dark", "Water Resistant"],
        "Analog",
        False,
        False,
        "China"
    )
    header = "watch product details:"
    print(header.upper())       
    watch_obj.show()
    print(help(Watch))

    #we can also get the attribute using getter methods
    #we can set the specific attribute using setter methods
    sys.exit(0)

main()