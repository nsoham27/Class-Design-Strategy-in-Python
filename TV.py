"""
@Author : Soham Naik
@Date: 27/12/2023
@Goal: To implement the class Television

Capture the real product from Amazon:
URL: https://www.amazon.in/Sony-Bravia-inches-Google-KD-55X74K/

Product details included->
Brand:                      tv_brand:                       str
Manufacturer:               tv_manufacturer:                str
Model:                      tv_model:                       str
Model Year:                 tv_model_year:                  int
Product Dimensions:         tv_product_dimensions:          ProductDimension(U)
Batteries:                  tv_nr_batteries:                int
Model number:               tv_nr_model:                    str
Operating system:           tv_os:                          [str]
Hardware Interface:         tv_hardare_interface :          [str]
Graphics Coprocessor:       tv_graphics_coprocessor:        str
Tuner Technology:           tv_tuner_technology:            str
Special features:           tv_features:                    [str]
Mounting Hardware:          tv_mounting_hardware:           [str]
Display Type:               tv_dsp_type:                    str
Remote control technology:  tv_remote_control_technology:   [str]
Resolution:                 tv_screen_resolution:           ProductResoultion(U)
Audio input:                tv_audio_input:                 [str]
Supported audio formats:    tv_audio_formats:               [str]
Wattage:                    tv_wattage:                     int
Voltage:                    tv_voltage:                     int
Power source:               tv_power_source:                str
Batteries included:         tv_are_batteries_included:      bool
Batteries required:         tv_are_batteries_required:      bool
Refresh Rate:               tv_refresh_rate:                int
Total  USB ports:           tv_nr_usb_ports:                int
Connector type:             tv_connector_type:              [str]
Media format:               tv_media_formats:               [str]
Include remote:             tv_is_remote_include:           bool
Country of origin:          tv_country_of_origin:           str
Net Quantity:               tv_net_quantity:                int

"""

import sys

class ProductDimension:
    """
    This class implement the dimensions of TV
    @__init__(self: object, length: float, width: float, height: float, weight: float):
        Constructor
    @get_length(self):
        getter of attribute length
    @get_width(self):
        getter of attribute width
    @get_height(self):
        getter of attribute height
    @get_weight(self):
        getter of attribute weight
    
    @set_length(self, new_length):
        setter of attribute length
    @set_width(self, new_width):
        setter of attribute width
    @set_height(self, new_height):
        setter of attribute height
    @set_weight(self, new_weight):
        setter of attribute weight
    """

    def __init__(self: object, length: float, width: float, height: float, weight: float) -> None:
        """
        def __init__(self: object, length: float, width: float, height: float, weight: float):
            @self: Newly created object of class ProductDimension
            @length: Client specified value for attribute length.
            @width: Client specified value for attribute width.
            @height: Client specified value for attribute height.
            @weight: Client specified value for attribute weight.
        """
        #Type Checking
        if type(length) != float:
            raise TypeError("Bad type: Product length.")
        if type(width) != float:
            raise TypeError("Bad type: Product width.")
        if type(height) != float:
            raise TypeError("Bad type: Product height.")
        if type(weight) != float:
            raise TypeError("Bad type: Product weight.")
        
        #Value Checking
        if length <= 0.0:
            raise ValueError("Product length must be positive.")
        if width <= 0.0:
            raise ValueError("Product width must be positive.")
        if height <= 0.0:
            raise ValueError("Product height must be positive.")
        if weight <= 0.0:
            raise ValueError("Product weight must be positive.")
        
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    #Getter Methods
    def get_length(self: object)-> float:
        """
        Return the length attribute of calling object.
        """
        return self.length
    
    def get_width(self: object)-> float:
        """
        Return the width attribute of calling object.
        """
        return self.width
    
    def get_height(self: object)-> float:
        """
        Return the height attribute of calling object.
        """
        return self.height
    
    def get_weight(self: object)-> float:
        """
        Return the weight attribute of calling object.
        """
        return self.weight
    
    #Setter Methods
    def set_length(self: object, new_length: float)-> None:
        """
        Set the length attribute of the calling object to @new_length.
        Before setting: Typecheck and Valuecheck are performed.
        """
        if type(new_length) != float:
            raise TypeError("Bad type: Product new length.")
        if new_length <= 0.0:
            raise ValueError("New length must be positive.")
        
        self.length = new_length
    
    def set_width(self: object, new_width: float)-> None:
        """
        Set the width attribute of the calling object to @new_width.
        Before setting: Typecheck and Valuecheck are performed.
        """
        if type(new_width) != float:
            raise TypeError("Bad type: Product new width.")
        if new_width <= 0.0:
            raise ValueError("New width must be positive.")
        
        self.width = new_width
    
    def set_height(self: object, new_height: float)-> None:
        """
        Set the height attribute of the calling object to @new_height.
        Before setting: Typecheck and Valuecheck are performed.
        """
        if type(new_height) != float:
            raise TypeError("Bad type: Product new height.")
        if new_height <= 0.0:
            raise ValueError("New height must be positive.")
        
        self.height = new_height
    
    def set_weight(self: object, new_weight: float)-> None:
        """
        Set the weight attribute of the calling object to @new_weight.
        Before setting: Typecheck and Valuecheck are performed.
        """
        if type(new_weight) != float:
            raise TypeError("Bad type: Product new weight.")
        if new_weight <= 0.0:
            raise ValueError("New weight must be positive.")

class ProductResolution:

    """
    This class implement the Resolution of TV in Pixel
    @__init__(self: object, rs_width: int, rs_height: int):
        Constructor
    @get_rs_width(self: object)-> int:
        getter of attribute width(Resolution in pixel).
    @get_rs_height(self: object)-> int:
        getter of attribute height(Resolution in pixel).
    
    ---------------------------------

    @set_rs_width(self: object, new_rs_width: int)-> None:
        setter of attribute width.
    @set_rs_height(self: object, new_rs_height: int)-> None:
        setter of attribute height.
    @set_rs_reset(self: object, new_rs_width: int, new_rs_height: int)-> None:
        setter of both attributes width and height

    """
    def __init__(self: object, rs_width: int, rs_height: int) -> None:
        """
        @self: Newly created class object of ProductResolution
        @rs_width: Client specified value for attribute width.
        @rs_height: Client specified value for attribute height.
        """
        #Type checking
        if type(rs_width) != int:
            raise TypeError("Bad type: Product resolution width.")
        if type(rs_height) != int:
            raise TypeError("Bad type: Product resolution height.")
        
        #Value checking
        if rs_width <= 0:
            raise ValueError("Product resolution width must be positive.")
        if rs_height <= 0:
            raise ValueError("Product resolution height must be positive.")
        
        self.rs_width = rs_width
        self.rs_height = rs_height
    
    #Getter methods
    def get_rs_width(self: object)-> int:
        """
        Return the resolution width attribute of the calling object in pixel.
        """
        return self.rs_width
    
    def get_rs_height(self: object)-> int:
        """
        Return the resolution height attribute of the calling object in pixel.
        """
        return self.rs_height
    
    #Setter methods
    def set_rs_width(self: object, new_rs_width: int)-> None:
        """
        Set the resolution width attribute of the calling object to @new_rs_width.
        Before setting: TypeCheck and ValueCheck are performed.
        """
        if type(new_rs_width) != int:
            raise TypeError("Bad type: Product resolution new width.")
        if new_rs_width <= 0:
            raise ValueError("Product resolution width must be positive.")
        self.rs_width = new_rs_width
    
    def set_rs_height(self: object, new_rs_height: int)-> None:
        """
        Set the resolution height attribute of the calling object to @new_rs_height.
        Before setting: TypeCheck and ValueCheck are performed.
        """
        if type(new_rs_height) != int:
            raise TypeError("Bad type: Product resolution new height.")
        if new_rs_height <= 0:
            raise ValueError("Product resolution height must be positive.")
        self.rs_height = new_rs_height
    
    def set_rs_reset(self: object, new_rs_width: int, new_rs_height: int)-> None:
        """
        Set the resolution width and height attributes of the calling object
        to @new_rs_width and @new_rs_height respectively.
        Before setting: TypeCheck and ValueCheck are performed.
        """
        if type(new_rs_width) != int:
            raise TypeError("Bad type: Product resolution new width.")
        if type(new_rs_height) != int:
            raise TypeError("Bad type: Product resolution new height.")
        
        if new_rs_width <= 0:
            raise ValueError("Product resolution width must be positive")
        if new_rs_height <= 0:
            raise ValueError("Product resolution height must be positive.")
        
        self.rs_width = new_rs_width
        self.rs_height = new_rs_height

class Television:
    """
    This class is implement the charachterstics on Watch.
    @__init__(
        self: object,
        tv_brand: str,
        tv_manufacturer: str,
        tv_model: str,
        tv_model_year: int,
        tv_product_dimensions: ProductDimension,
        tv_nr_batteries: int,
        tv_nr_model: str,
        tv_os: list[str],
        tv_hardare_interface: list[str],
        tv_graphics_coprocessor: str,
        tv_tuner_technology: str,
        tv_features: list[str],
        tv_mounting_hardware: list[str],
        tv_dsp_type: str,
        tv_remote_control_technology: list[str],
        tv_screen_resolution: ProductResolution,
        tv_audio_input: list[str],
        tv_audio_formats: list[str],
        tv_wattage: int,
        tv_voltage: int,
        tv_power_source: str,
        tv_are_batteries_included: bool,
        tv_are_batteries_required: bool,
        tv_refresh_rate: int,
        tv_nr_usb_ports: int,
        tv_connector_type: list[str],
        tv_media_formats: list[str],
        tv_is_remote_include: bool,
        tv_country_of_origin: str,
        tv_net_quantity: int
    )-> None:
        Constructor
    
    @get_tv_brand(self: object)->str:
        Getter of attribute tv_brand
    @get_tv_manufacturer(self: object)->str:
        Getter of attribute tv_manufacturer
    @get_tv_model(self: object)->str:
        Getter of attribute tv_model
    @get_tv_model_year(self: object)->int:
        Getter of attribute tv_model_year
    @get_tv_product_dimensions(self: object)->list:
        Getter of attribute tv_product_dimensions
    @get_tv_nr_batteries(self: object)-> int:
        Getter of attribute tv_nr_batteries
    @get_tv_nr_model(self: object)-> str:
        Getter of attribute tv_nr_model
    @get_tv_os(self: object)-> list:
        Getter of attribute tv_os
    @get_tv_hardare_interface(self: object)-> list:
        Getter of attribute tv_hardware_interface
    @get_tv_graphics_coprocessor(self: object)-> str:
        Getter of attribute tv_graphics_coprocessor
    @get_tv_tuner_technology(self: object)-> str:
        Getter of attribute tv_tuner_technology
    @get_tv_features(self: object)-> list:
        Getter of attribute tv_features
    @get_tv_mounting_hardware(self: object)-> list:
        Getter of attribute tv_mounting_hardware
    @get_tv_dsp_type(self: object)-> str:
        Getter of attribute tv_dsp_type
    @get_tv_remote_control_technology(self: object)-> list:
        Getter of attribute tv_remote_control_technology
    @get_tv_screen_resolution(self: object)->list:
        Getter of attribute tv_screen_resolution
    @get_tv_audio_input(self: object)-> list:
        Getter of attribute tv_audio_input
    @get_tv_audio_formats(self: object)-> list:
        Getter of attribute tv_audio_formats
    @get_tv_wattage(self: object)-> int:
        Getter of attribute tv_wattage
    @get_tv_voltage(self: object)-> int:
        Getter of attribute tv_voltage
    @get_tv_power_source(self: object)-> str:
        Getter of attribute tv_power_source
    @get_tv_are_batteries_included(self: object)-> bool:
        Getter of attribute tv_are_batteries_included
    @get_tv_are_batteries_required(self: object)-> bool:
        Getter of attribute tv_are_batteries_required
    @get_tv_refresh_rate(self: object)-> int:
        Getter of attribute tv_refresh_rate
    @get_tv_nr_usb_ports(self: object)-> int:
        Getter of attribute tv_nr_usb_ports
    @get_tv_connector_type(self: object)-> list:
        Getter of attribute tv_connector_type
    @get_tv_media_formats(self: object)-> list:
        Getter of attribute tv_media_formats
    @get_tv_is_remote_include(self: object)->bool:
        Getter of attribute tv_is_remote_include
    @get_tv_country_of_origin(self: object)-> str:
        Getter of attribute tv_country_of_origin
    @get_tv_net_quantity(self: object)->int:
        Getter of attribute tv_net_quantity
    ----------------------------------------------------------
    @set_tv_brand(self: object)->str:
        setter of attribute tv_brand
    @set_tv_manufacturer(self: object)->str:
        setter of attribute tv_manufacturer
    @set_tv_model(self: object)->str:
        setter of attribute tv_model
    @set_tv_model_year(self: object)->int:
        setter of attribute tv_model_year
    @set_tv_product_dimensions(self: object)->list:
        setter of attribute tv_product_dimensions
    @set_tv_nr_batteries(self: object)-> int:
        setter of attribute tv_nr_batteries
    @set_tv_nr_model(self: object)-> str:
        setter of attribute tv_nr_model
    @set_tv_os(self: object)-> list:
        setter of attribute tv_os
    @set_tv_hardare_interface(self: object)-> list:
        setter of attribute tv_hardware_interface
    @set_tv_graphics_coprocessor(self: object)-> str:
        setter of attribute tv_graphics_coprocessor
    @set_tv_tuner_technology(self: object)-> str:
        setter of attribute tv_tuner_technology
    @set_tv_features(self: object)-> list:
        setter of attribute tv_features
    @set_tv_mounting_hardware(self: object)-> list:
        setter of attribute tv_mounting_hardware
    @set_tv_dsp_type(self: object)-> str:
        setter of attribute tv_dsp_type
    @set_tv_remote_control_technology(self: object)-> list:
        setter of attribute tv_remote_control_technology
    @set_tv_screen_resolution(self: object)->list:
        setter of attribute tv_screen_resolution
    @set_tv_audio_input(self: object)-> list:
        setter of attribute tv_audio_input
    @set_tv_audio_formats(self: object)-> list:
        setter of attribute tv_audio_formats
    @set_tv_wattage(self: object)-> int:
        setter of attribute tv_wattage
    @set_tv_voltage(self: object)-> int:
        setter of attribute tv_voltage
    @set_tv_power_source(self: object)-> str:
        setter of attribute tv_power_source
    @set_tv_are_batteries_included(self: object)-> bool:
        setter of attribute tv_are_batteries_included
    @set_tv_are_batteries_required(self: object)-> bool:
        setter of attribute tv_are_batteries_required
    @set_tv_refresh_rate(self: object)-> int:
        setter of attribute tv_refresh_rate
    @set_tv_nr_usb_ports(self: object)-> int:
        setter of attribute tv_nr_usb_ports
    @set_tv_connector_type(self: object)-> list:
        setter of attribute tv_connector_type
    @set_tv_media_formats(self: object)-> list:
        setter of attribute tv_media_formats
    @set_tv_is_remote_include(self: object)->bool:
        setter of attribute tv_is_remote_include
    @set_tv_country_of_origin(self: object)-> str:
        setter of attribute tv_country_of_origin
    @set_tv_net_quantity(self: object)->int:
        setter of attribute tv_net_quantity

    """
    def __init__(
            self: object,
            tv_brand: str,
            tv_manufacturer: str,
            tv_model: str,
            tv_model_year: int,
            tv_product_dimensions: ProductDimension,
            tv_nr_batteries: int,
            tv_nr_model: str,
            tv_os: list[str],
            tv_hardare_interface: list[str],
            tv_graphics_coprocessor: str,
            tv_tuner_technology: str,
            tv_features: list[str],
            tv_mounting_hardware: list[str],
            tv_dsp_type: str,
            tv_remote_control_technology: list[str],
            tv_screen_resolution: ProductResolution,
            tv_audio_input: list[str],
            tv_audio_formats: list[str],
            tv_wattage: int,
            tv_voltage: int,
            tv_power_source: str,
            tv_are_batteries_included: bool,
            tv_are_batteries_required: bool,
            tv_refresh_rate: int,
            tv_nr_usb_ports: int,
            tv_connector_type: list[str],
            tv_media_formats: list[str],
            tv_is_remote_include: bool,
            tv_country_of_origin: str,
            tv_net_quantity: int
        )-> None:
        """
        @self: newly created class object of TV
        @tv_brand: Client specified value for attibute tv_brand
        @tv_manufacturer: Client specified value for attibute tv_manufacturer
        @tv_model: Client specified value for attibute tv_model
        @tv_model_year: Client specified value for attibute tv_model_year
        @tv_product_dimensions: Client specified value for attibute tv_product_dimensions
        @tv_nr_batteries: Client specified value for attibute tv_nr_batteries
        @tv_nr_model: Client specified value for attibute tv_nr_model
        @tv_os: Client specified value for attibute tv_os
        @tv_hardare_interface: Client specified value for attibute tv_hardware_interface
        @tv_graphics_coprocessor: Client specified value for attibute tv_graphics_coprocessor
        @tv_tuner_technology: Client specified value for attibute tv_tuner_technology
        @tv_features: Client specified value for attibute tv_features
        @tv_mounting_hardware: Client specified value for attibute tv_mounting_hardware
        @tv_dsp_type: Client specified value for attibute tv_dsp_type
        @tv_remote_control_technology: Client specified value for attibute tv_remote_control_technology
        @tv_screen_resolution: Client specified value for attibute tv_screen_resolution
        @tv_audio_input: Client specified value for attibute tv_audio_input
        @tv_audio_formats: Client specified value for attibute tv_audio_formats
        @tv_wattage: Client specified value for attibute tv_wattage
        @tv_voltage: Client specified value for attibute tv_voltage
        @tv_power_source: Client specified value for attibute tv_power_source
        @tv_are_batteries_included: Client specified value for attibute tv_are_batteries_included
        @tv_are_batteries_required: Client specified value for attibute tv_are_batteries_required
        @tv_refresh_rate: Client specified value for attibute tv_refresh_rate
        @tv_nr_usb_ports: Client specified value for attibute tv_nr_usb_ports
        @tv_connector_type: Client specified value for attibute tv_connector_type
        @tv_media_formats: Client specified value for attibute tv_media_formats
        @tv_is_remote_include: Client specified value for attibute tv_is_remote_include
        @tv_country_of_origin: Client specified value for attibute tv_country_of_origin
        @tv_net_quantity: Client specified value for attibute tv_net_quantity
        """

        #Type Checking

        if type(tv_brand) != str:
            raise TypeError("Bad type: TV brand.")
        if type(tv_manufacturer) != str:
            raise TypeError("Bad type: TV manufacturer.")
        if type(tv_model) != str:
            raise TypeError("Bad type: TV model.")
        if type(tv_model_year) != int:
            raise TypeError("Bad type: TV model year.")
        if type(tv_product_dimensions) != ProductDimension:
            raise TypeError("Bad type: TV Dimensions.")
        if type(tv_nr_batteries) != int:
            raise TypeError("Bad type: TV number of batteries.")
        if type(tv_nr_model) != str:
            raise TypeError("Bad type: TV model number.")
        if type(tv_os) != list:
            raise TypeError("Bad type: TV operating system.")
        if "__iter__" not in dir(type(tv_os)):
            raise TypeError("Bad type: TV OS must be iterable.")
        for os in tv_os:
            if type(os) != str:
                raise TypeError("Bad type: TV OS.")
        if type(tv_hardare_interface) != list:
            raise TypeError("Bad type: TV hardware interface.")
        if "__iter__" not in dir(type(tv_hardare_interface)):
            raise TypeError("Bad type: TV hardware interface must be iterable.")
        for hardware_interface in tv_hardare_interface:
            if type(hardware_interface) != str:
                raise TypeError("Bad type: TV hardware interface.")
        if type(tv_graphics_coprocessor) != str:
            raise TypeError("Bad type: TV graphics coprocessor.")
        if type(tv_tuner_technology) != str:
            raise TypeError("Bad type: TV tuner technology.")
        if type(tv_features) != list:
            raise TypeError("Bad type: TV features.")
        if "__iter__" not in dir(type(tv_features)):
            raise TypeError("Bad type: TV features must be iterable.")
        for feature in tv_features:
            if type(feature) != str:
                raise TypeError("Bad type: TV features.")
        if type(tv_mounting_hardware) != list:
            raise TypeError("Bad type: TV mounting hardware.")
        if "__iter__" not in dir(type(tv_mounting_hardware)):
            raise TypeError("Bad type: TV mounting hardware must be iterable.")
        for mounting_hardware in tv_mounting_hardware:
            if type(mounting_hardware) != str:
                raise TypeError("Bad type: TV mounting hardware.")
        if type(tv_dsp_type) != str:
            raise TypeError("Bad type: TV display type.")
        if type(tv_remote_control_technology) != list:
            raise TypeError("Bad type: TV remote control technology.")
        if "__iter__" not in dir(type(tv_remote_control_technology)):
            raise TypeError("Bad type: TV remote control technology must be iterable.")
        for remote_control_technology in tv_remote_control_technology:
            if type(remote_control_technology) != str:
                raise TypeError("Bad type: TV remote control technology.")
        if type(tv_screen_resolution) != ProductResolution:
            raise TypeError("Bad type: TV screen resolution.")
        if type(tv_audio_input) != list:
            raise TypeError("Bad type: TV audio input.")
        if "__iter__" not in dir(type(tv_audio_input)):
            raise TypeError("TV audio input must be iterable.")
        for audio_input in tv_audio_input:
            if type(audio_input) != str:
                raise TypeError("Bad type: TV audio input.")
        if type(tv_audio_formats) != list:
            raise TypeError("Bad type: TV audio formats.")
        for audio_formats in tv_audio_formats:
            if type(audio_formats) != str:
                raise TypeError("Bad type: TV audio format.")
        if type(tv_wattage) != int:
            raise TypeError("Bad type: TV wattage.")
        if type(tv_voltage) != int:
            raise TypeError("Bad type: TV voltage.")
        if type(tv_power_source) != str:
            raise TypeError("Bad type: TV power source.")
        if type(tv_are_batteries_included) != bool:
            raise TypeError("Bad type: TV battteries included.")
        if type(tv_are_batteries_required) != bool:
            raise TypeError("Bad type: TV batteries required.")
        if type(tv_refresh_rate) != int:
            raise TypeError("Bad type: TV refresh rate.")
        if type(tv_nr_usb_ports) != int:
            raise TypeError("Bad type: TV number of usb ports.")
        if type(tv_connector_type) != list:
            raise TypeError("Bad type: TV connector type.")
        for connector_type in tv_connector_type:
            if type(connector_type) != str:
                raise TypeError("Bad type: TV connector type.")
        if type(tv_media_formats) != list:
            raise TypeError("Bad type: TV media formats.")
        for media_formats in tv_media_formats:
            if type(media_formats) != str:
                raise TypeError("Bad type: TV media formats")
        if type(tv_is_remote_include) != bool:
            raise TypeError("Bad type: TV remote included.")
        if type(tv_country_of_origin) != str:
            raise TypeError("Bad type: TV country of origin.")
        if type(tv_net_quantity) != int:
            raise TypeError("Bad type: TV net quantity.")

        # Value checking

        if len(tv_brand.strip()) == 0:
            raise ValueError("TV brand cannot be empty.")
        if len(tv_manufacturer.strip()) == 0:
            raise ValueError("TV manufacturer cannot be empty.")
        if len(tv_model.strip()) == 0:
            raise ValueError("TV model cannot be empty.")
        if tv_model_year <= 0:
            raise ValueError("TV model year must be positive.")
        if tv_nr_batteries <= 0:
            raise ValueError("TV batteries must be positive.")
        if len(tv_nr_model.strip()) == 0:
            raise ValueError("TV model number cannot be emoty.")
        if len(tv_os) == 0:
            raise ValueError("TV OS cannot be empty.")
        for os in tv_os:
            if len(os) == 0:
                raise ValueError("TV OS cannot be blank.") 
        if len(tv_hardare_interface) == 0:
            raise ValueError("TV Hardware Interface cannot be empty.")
        for HI in tv_hardare_interface:
            if len(HI) == 0:
                raise ValueError("TV Hardware Interface cannot be blank.") 
        if len(tv_graphics_coprocessor) == 0:
            raise ValueError("TV graphics coprocessor cannot be empty.")
        if len(tv_tuner_technology) == 0:
            raise ValueError("TV tunner technology cannot be empty.")
        if len(tv_features) == 0:
            raise ValueError("TV features cannot be empty.")
        for feature in tv_features:
            if len(feature) == 0:
                raise ValueError("TV features cannot be blank.")
        if len(tv_mounting_hardware) == 0:
            raise ValueError("TV mounting hardware cannot be empty.")
        for mounting_hardware in tv_mounting_hardware:
            if len(mounting_hardware) == 0:
                raise ValueError("TV mounting hardware cannot be blank.")
        if len(tv_dsp_type) == 0:
            raise ValueError("TV display type cannot be emtpy.")
        if len(tv_remote_control_technology) == 0:
            raise ValueError("TV remote control Technology cannot be empty.")
        for remote_control_technology in tv_remote_control_technology:
            if len(remote_control_technology) == 0:
                raise ValueError("TV remote control Technology cannot be blank.")
        if len(tv_audio_input) == 0:
            raise ValueError("TV audio input cannot be empty.")
        for audio_input in tv_audio_input:
            if len(audio_input) == 0:
                raise ValueError("TV audio input cannot be blank.")
        if len(tv_audio_formats) == 0:
            raise TypeError("TV audio format cannot be empty.")
        for audio_formats in tv_audio_formats:
            if len(audio_formats) == 0:
                raise ValueError("TV audio format cannot be blank.")
        if tv_wattage <= 0:
            raise ValueError("TV wattage must be positive") 
        if tv_voltage <= 0 :
            raise ValueError("TV voltage must be positive.")
        if len(tv_power_source.strip()) == 0:
            raise ValueError("TV power source cannot be empty.")
        if tv_are_batteries_included != True and tv_are_batteries_included != False:
            raise ValueError("TV are batteries included must be boolean(True or False).")
        if tv_are_batteries_required != True and tv_are_batteries_required != False:
            raise ValueError("TV are batteries required must be boolean(True or False).")
        if tv_refresh_rate <=0:
            raise ValueError("TV refresh rate must be positive.")
        if tv_nr_usb_ports <= 0:
            raise ValueError("TV number of USB ports muust be positive.")
        if len(tv_connector_type) == 0:
            raise ValueError("TV connector type cannot be empty.")
        for connector_type in tv_connector_type:
            if len(connector_type) == 0:
                raise ValueError("TV connector type cannot be blank.")
        if len(tv_media_formats) == 0:
            raise ValueError("TV media format cannot be empty.")
        for media_formats in tv_media_formats:
            if len(media_formats) == 0:
                raise ValueError("TV media format cannot be blank.")
        if tv_is_remote_include != True and tv_is_remote_include != False:
            raise ValueError("is TV remote included must be boolean(True or False).")
        if len(tv_country_of_origin.strip()) == 0:
            raise ValueError("TV country of origin cannot be empty.")
        if tv_net_quantity <= 0:
            raise ValueError("TV net quantity must be positive.")
        
        self.tv_brand = tv_brand
        self.tv_manufacturer = tv_manufacturer
        self.tv_model = tv_model
        self.tv_model_year = tv_model_year
        self.tv_product_dimensions = tv_product_dimensions
        self.tv_nr_batteries = tv_nr_batteries
        self.tv_nr_model = tv_nr_model
        self.tv_os = tv_os
        self.tv_hardare_interface = tv_hardare_interface
        self.tv_graphics_coprocessor = tv_graphics_coprocessor
        self.tv_tuner_technology = tv_tuner_technology
        self.tv_features = tv_features
        self.tv_mounting_hardware = tv_mounting_hardware
        self.tv_dsp_type = tv_dsp_type
        self.tv_remote_control_technology = tv_remote_control_technology
        self.tv_screen_resolution = tv_screen_resolution
        self.tv_audio_input = tv_audio_input
        self.tv_audio_formats = tv_audio_formats
        self.tv_wattage = tv_wattage
        self.tv_voltage = tv_voltage
        self.tv_power_source = tv_power_source
        self.tv_are_batteries_included = tv_are_batteries_included
        self.tv_are_batteries_required = tv_are_batteries_required
        self.tv_refresh_rate = tv_refresh_rate
        self.tv_nr_usb_ports = tv_nr_usb_ports
        self.tv_connector_type = tv_connector_type
        self.tv_media_formats = tv_media_formats
        self.tv_is_remote_include = tv_is_remote_include
        self.tv_country_of_origin = tv_country_of_origin
        self.tv_net_quantity = tv_net_quantity
    
    # Getter Methods
    def get_tv_brand(self: object)->str:
        """
        Returns the tv_brand attribute of the calling object.
        """
        return self.tv_brand
    
    def get_tv_manufacturer(self: object)->str:
        """
        Returns the tv_manufacturer attribute of the calling object.
        """
        return self.tv_manufacturer
    
    def get_tv_model(self: object)->str:
        """
        Returns the tv_model attribute of the calling object.
        """
        return self.tv_model
    
    def get_tv_model_year(self: object)->int:
        """
        Returns the tv_model_year attribute of the calling object.
        """
        return self.tv_model_year
    
    def get_tv_product_dimensions(self: object)->list:
        """
        Returns the tv_product_dimensions attribute of the calling object.
        """
        L = []
        L.append(self.tv_product_dimensions.get_length())
        L.append(self.tv_product_dimensions.get_width())
        L.append(self.tv_product_dimensions.get_height())
        L.append(self.tv_product_dimensions.get_height())
        return L
    def get_tv_nr_batteries(self: object)-> int:
        """
        Returns the tv_nr_batteries attribute of the calling object.
        """
        return self.tv_nr_batteries
    def get_tv_nr_model(self: object)-> str:
        """
        Returns the tv_nr_model attribute of the calling object.
        """
        return self.tv_nr_model
    
    def get_tv_os(self: object)-> list:
        """
        Returns the tv_os attribute of the calling object.
        """
        return self.tv_os
    
    def get_tv_hardare_interface(self: object)-> list:
        """
        Returns the tv_hardware_interface attribute of the calling object.
        """
        return self.tv_hardare_interface
    
    def get_tv_graphics_coprocessor(self: object)-> str:
        """
        Returns the tv_graphics_coprocessor attribute of the calling object.
        """
        return self.tv_graphics_coprocessor
    
    def get_tv_tuner_technology(self: object)-> str:
        """
        Returns the tv_tuner_technology attribute of the calling object.
        """
        return self.tv_tuner_technology
    
    def get_tv_features(self: object)-> list:
        """
        Returns the tv_features attribute of the calling object.
        """
        return self.tv_features
    
    def get_tv_mounting_hardware(self: object)-> list:
        """
        Returns the tv_mounting_hardware attribute of the calling object.
        """
        return self.tv_mounting_hardware
    
    def get_tv_dsp_type(self: object)-> str:
        """
        Returns the tv_dsp_type attribute of the calling object.
        """
        return self.tv_dsp_type
    
    def get_tv_remote_control_technology(self: object)-> list:
        """
        Returns the tv_remote_control_technology attribute of the calling object.
        """
        return self.tv_remote_control_technology
    
    def get_tv_screen_resolution(self: object)->list:
        """
        Returns the tv_screen_resolution attribute of the calling object.
        """
        R = []
        R.append(self.tv_screen_resolution.get_rs_width())
        R.append(self.tv_screen_resolution.get_rs_height())
        return R
    
    def get_tv_audio_input(self: object)-> list:
        """
        Returns the tv_audio_input attribute of the calling object.
        """
        return self.tv_audio_input
    
    def get_tv_audio_formats(self: object)-> list:
        """
        Returns the tv_audio_formats attribute of the calling object.
        """
        return self.tv_audio_formats
    
    def get_tv_wattage(self: object)-> int:
        """
        Returns the tv_wattage attribute of the calling object.
        """
        return self.tv_wattage
    def get_tv_voltage(self: object)-> int:
        """
        Returns the tv_voltage attribute of the calling object.
        """
        return self.tv_voltage
    
    def get_tv_power_source(self: object)-> str:
        """
        Returns the tv_power_source attribute of the calling object.
        """
        return self.tv_power_source
    
    def get_tv_are_batteries_included(self: object)-> bool:
        """
        Returns the tv_are_batteries_included attribute of the calling object.
        """
        return self.tv_are_batteries_included
    
    def get_tv_are_batteries_required(self: object)-> bool:
        """
        Returns the tv_are_batteries_required attribute of the calling object.
        """
        return self.tv_are_batteries_required
    
    def get_tv_refresh_rate(self: object)-> int:
        """
        Returns the tv_refresh_rate attribute of the calling object.
        """
        return self.tv_refresh_rate
    
    def get_tv_nr_usb_ports(self: object)-> int:
        """
        Returns the tv_nr_usb_ports attribute of the calling object.
        """
        return self.tv_nr_usb_ports
    
    def get_tv_connector_type(self: object)-> list:
        """
        Returns the tv_connector_type attribute of the calling object.
        """
        return self.tv_connector_type
    
    def get_tv_media_formats(self: object)-> list:
        """
        Returns the tv_media_formats attribute of the calling object.
        """
        return self.tv_media_formats
    
    def get_tv_is_remote_include(self: object)->bool:
        """
        Returns the tv_is_remote_include attribute of the calling object.
        """
        return self.tv_is_remote_include
    
    def get_tv_country_of_origin(self: object)-> str:
        """
        Returns the tv_country_of_origin attribute of the calling object.
        """
        return self.tv_country_of_origin
    
    def get_tv_net_quantity(self: object)->int:
        """
        Returns the tv_net_quantity attribute of the calling object.
        """
        return self.tv_net_quantity
    
    # Setter Method
    def set_tv_brand(self: object, new_tv_brand: str)-> None:
        """
        Sets the tv_brand attribute of the calling object to @new_tv_brand
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_brand) != str:
            raise TypeError("Bad type: new TV brand.")
        if len(new_tv_brand.strip()) == 0:
            raise ValueError("new TV brand cannot be empty.")
        
        self.tv_brand = new_tv_brand
    
    def set_tv_manufacturer(self: object, new_tv_manufacturer: str)-> None:
        """
        Sets the tv_manufacturer attribute of the calling object to @new_tv_manufacturer
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_manufacturer) != str:
            raise TypeError("Bad type: new TV Manufacturer.")
        if len(new_tv_manufacturer.strip()) == 0:
            raise ValueError("new TV manufacturer cannot be empty.")
        
        self.tv_manufacturer = new_tv_manufacturer
    
    def set_tv_model(self: object, new_tv_model: str)-> None:
        """
        Sets the tv_model attribute of the calling object to @new_tv_model
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_model) != str:
            raise TypeError("Bad type: new TV model.")
        if len(new_tv_model.strip()) == 0:
            raise ValueError("new TV model cannot be empty.")
        
        self.tv_model = new_tv_model
    
    def set_tv_model_year(self: object, new_tv_model_year: int)-> None:
        """
        Sets the tv_model_year attribute of the calling object to @new_tv_model_year
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_model_year) != int:
            raise TypeError("Bad type: new TV model year.")
        if new_tv_model_year <= 0:
            raise ValueError("new TV model year.")
        
        self.tv_model_year = new_tv_model_year
    
    def set_tv_product_dimensions(self: object, new_tv_product_dimensions: ProductDimension)-> None:
        """
        Sets the tv_product_dimensions attribute of the calling object to @new_tv_product_dimensions
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_product_dimensions) != ProductDimension:
            raise TypeError("Bad type: new TV product dimensions.")
        
        tv_product_dimensions = new_tv_product_dimensions
    
    def set_tv_nr_batteries(self: object, new_tv_nr_batteries: int)-> None:
        """
        Sets the tv_nr_batteries attribute of the calling object to @new_tv_nr_batteries
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_nr_batteries) != int:
            raise TypeError("Bad type: new TV number of batteries.")
        if new_tv_nr_batteries <= 0:
            raise ValueError("new TV number of batteries must be positive.")
        
        self.tv_nr_batteries = new_tv_nr_batteries
    
    def set_tv_nr_model(self: object, new_tv_nr_model: str)->None:
        """
        Sets the tv_nr_model attribute of the calling object to @new_tv_nr_model
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_nr_model) != str:
            raise TypeError("Bad type: new TV number of model.")
        if len(new_tv_nr_model.strip()) == 0:
            raise ValueError("new TV number of model cannot be empty.")
        
        self.tv_nr_model = new_tv_nr_model
    
    def set_tv_os(self: object, new_tv_os: list)-> None:
        """
        Sets the tv_os attribute of the calling object to @new_tv_os
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_os) != list:
            raise TypeError("Bad type: new TV OS.")
        if len(new_tv_os) == 0:
            raise ValueError("new TV os cannot be empty.")
        for os in new_tv_os:
            if len(os.strip()) == 0:
                raise ValueError("new TV os cannot be blank.")
        
        self.tv_os = new_tv_os
    
    def set_tv_hardare_interface(self: object, new_tv_hardware_interface: list)-> None:
        """
        Sets the tv_hardware_interface attribute of the calling object to @new_tv_hardware_interface
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_hardware_interface) != list:
            raise TypeError("Bad type: new TV hardware interface.")
        if len(new_tv_hardware_interface) == 0:
            raise ValueError("new TV hardware interface.")
        for hardware_interface in new_tv_hardware_interface:
            if len(hardware_interface.strip()) == 0:
                raise ValueError("new TV hardware interface cannot be blank.")
        
        self.tv_hardare_interface = new_tv_hardware_interface
    
    def set_tv_graphics_coprocessor(self: object, new_tv_graphics_coprocessor: str)->None:
        """
        Sets the tv_graphics_coprocessor attribute of the calling object to @new_tv_graphics_coprocessor
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_graphics_coprocessor) != str:
            raise TypeError("Bad type: new TV graphics coprocessor.")
        if len(new_tv_graphics_coprocessor) == 0:
            raise ValueError("new TV Graphics coprocessor cannot be empty.")
        
        self.tv_graphics_coprocessor = new_tv_graphics_coprocessor
    
    def set_tv_tuner_technology(self: object, new_tv_tuner_technology: str)-> None:
        """
        Sets the tv_tuner_technology attribute of the calling object to @new_tv_tuner_technology
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_tuner_technology) != str:
            raise TypeError("Bad type: new TV tunner technology.")
        if len(new_tv_tuner_technology) == 0:
            raise ValueError("new TV tunner technology cannot be empty.")
        
        self.tv_tuner_technology = new_tv_tuner_technology
    
    def set_tv_features(self: object, new_tv_features: list)->None:
        """
        Sets the tv_features attribute of the calling object to @new_tv_features
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_features) != list:
            raise TypeError("Bad type: new TV features.")
        if len(new_tv_features) == 0:
            raise ValueError("new TV features.")
        for feature in new_tv_features:
            if len(feature.strip()) == 0:
                raise ValueError("new TV features cannot be blank.")
        
        self.tv_features = new_tv_features
    
    def set_tv_mounting_hardware(self: object, new_tv_mounting_hardware: list)-> None:
        """
        Sets the tv_mounting_hardware attribute of the calling object to @new_tv_mounting_hardware
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_mounting_hardware) != list:
            raise TypeError("Bad type: new TV mounting hardware.")
        if len(new_tv_mounting_hardware) == 0:
            raise ValueError("new TV mounting hardware.")
        for mounting_hardware in new_tv_mounting_hardware:
            if len(mounting_hardware.strip()) == 0:
                raise ValueError("new TV mounting hardware cannot be blank.")
            
        self.tv_mounting_hardware = new_tv_mounting_hardware
    
    def set_tv_dsp_type(self: object, new_tv_dsp_type: str)-> None:
        """
        Sets the tv_dsp_type attribute of the calling object to @new_tv_dsp_type
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_dsp_type) != str:
            raise TypeError("bad type: new TV display type.")
        if len(new_tv_dsp_type) == 0:
            raise ValueError("new TV display type cannot be empty.")
        
        self.tv_dsp_type = new_tv_dsp_type
    
    def set_tv_remote_control_technology(self: object, new_tv_remote_control_technology: list)-> str:
        """
        Sets the tv_remote_control_technology attribute of the calling object to @new_tv_remote_control_technology
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_remote_control_technology) != list:
            raise TypeError("Bad type: new TV remote control technology.")
        if len(new_tv_remote_control_technology) == 0:
            raise ValueError("new TV mounting hardware.")
        for remote_control_technology in new_tv_remote_control_technology:
            if len(remote_control_technology.strip()) == 0:
                raise ValueError("new TV mounting hardware cannot be blank.")
        
        self.tv_remote_control_technology = new_tv_remote_control_technology
    
    def set_tv_screen_resolution(self: object, new_tv_screen_resolution: ProductResolution)->None:
        """
        Sets the tv_screen_resolution attribute of the calling object to @new_tv_screen_resolution
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_screen_resolution) != ProductResolution:
            raise TypeError("Bad type: TV screen resolution.")
        
        self.tv_screen_resolution = new_tv_screen_resolution
    
    def set_tv_audio_input(self: object, new_tv_audio_input: list)-> None:
        """
        Sets the tv_audio_input attribute of the calling object to @new_tv_audio_input
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_audio_input) != list:
            raise TypeError("Bad type: TV audio input.")
        if len(new_tv_audio_input) == 0:
            raise ValueError("new TV audio input.")
        for audio_input in new_tv_audio_input:
            if len(audio_input.strip()) == 0:
                raise ValueError("new TV audio input cannot be blank.")
        
        self.tv_audio_input = new_tv_audio_input
    
    def set_tv_audio_formats(self: object, new_tv_audio_formats: list)-> None:
        """
        Sets the tv_audio_formats attribute of the calling object to @new_tv_audio_formats
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_audio_formats) != list:
            raise TypeError("Bad type: TV audio formats.")
        if len(new_tv_audio_formats) == 0:
            raise ValueError("new TV audio formats.")
        for audio_formats in new_tv_audio_formats:
            if len(audio_formats.strip()) == 0:
                raise ValueError("new TV audio formats cannot be blank.")
            
        self.tv_audio_formats = new_tv_audio_formats
    
    def set_tv_wattage(self: object, new_tv_wattage: int)-> None:
        """
        Sets the tv_wattage attribute of the calling object to @new_tv_wattage
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_wattage) != int:
            raise TypeError("Bad type: new TV wattage.")
        if new_tv_wattage <= 0:
            raise ValueError("new TV wattage must be positive.")
        self.tv_wattage = new_tv_wattage
    
    def set_tv_voltage(self: object, new_tv_voltage: int)-> None:
        """
        Sets the tv_voltage attribute of the calling object to @new_tv_voltage
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_voltage) != int:
            raise TypeError("Bad type: new TV voltage.")
        if new_tv_voltage <= 0:
            raise ValueError("new TV voltage must be positive.")
        self.tv_voltage = new_tv_voltage
    
    def set_tv_power_source(self: object, new_tv_power_source: str)-> None:
        """
        Sets the tv_power_source attribute of the calling object to @new_tv_power_source
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_power_source) != str:
            raise TypeError("Bad type: new TV power source.")
        if len(new_tv_power_source) == 0:
            raise ValueError("new TV power source must be positive.")
        self.tv_power_source = new_tv_power_source
    
    def set_tv_are_batteries_included(self: object, new_tv_are_batteries_included: bool)-> None:
        """
        Sets the tv_are_batteries_included attribute of the calling object to @new_tv_are_batteries_included
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_are_batteries_included) != bool:
            raise TypeError("Bad type: new TV are batteries included.")
        if new_tv_are_batteries_included != True and new_tv_are_batteries_included != False:
            raise ValueError("new TV are batteries included must be True or False.")
        self.tv_are_batteries_included = new_tv_are_batteries_included
    
    def set_tv_are_batteries_required(self: object, new_tv_are_batteries_required: bool)-> None:
        """
        Sets the tv_are_batteries_required attribute of the calling object to @new_tv_are_batteries_required
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_are_batteries_required) != bool:
            raise TypeError("Bad type: new TV are batteries required.")
        if new_tv_are_batteries_required != True and new_tv_are_batteries_required != False:
            raise ValueError("new TV are batteries requried must be True or False.")
        self.tv_are_batteries_required = new_tv_are_batteries_required
   
    def set_tv_refresh_rate(self: object, new_tv_refresh_rate: int)-> None:
        """
        Sets the tv_refresh_rate attribute of the calling object to @new_tv_refresh_rate
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_refresh_rate) != int:
            raise TypeError("Bad type: new TV refresh rate.")
        if new_tv_refresh_rate <= 0:
            raise ValueError("new TV refresh rate must be positive.")
        
        self.tv_refresh_rate = new_tv_refresh_rate
    
    def set_tv_nr_usb_ports(self: object, new_tv_nr_usb_ports: int)-> None:
        """
        Sets the tv_nr_usb_ports attribute of the calling object to @new_tv_nr_usb_ports
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_nr_usb_ports) != int:
            raise TypeError("Bad type: new TV number of USB ports.")
        if new_tv_nr_usb_ports <= 0:
            raise ValueError("new TV number of USB ports must be positive.")
        
        self.tv_nr_usb_ports = new_tv_nr_usb_ports
    
    def set_tv_connector_type(self: object, new_tv_connector_type: list)-> None:
        """
        Sets the tv_connector_types attribute of the calling object to @new_tv_connector_types
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_connector_type) != list:
            raise TypeError("Bad Type: new TV connector Type.")
        if len(new_tv_connector_type) == 0:
            raise ValueError("new TV connector type cannot be empty.")
        for connector_type in new_tv_connector_type:
            if len(connector_type) == 0:
                raise ValueError("new TV connector type cannot be blank.")
        self.tv_connector_type = new_tv_connector_type
    
    def set_tv_media_formats(self: object, new_tv_media_formats: list)-> None:
        """
        
        Sets the tv_media_formats attribute of the calling object to @new_tv_media_formats
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_media_formats) != list:
            raise TypeError("Bad Type: new TV media formats.")
        if len(new_tv_media_formats) == 0:
            raise ValueError("new TV media formats cannot be empty.")
        for media_formats in new_tv_media_formats:
            if len(media_formats) == 0:
                raise ValueError("new TV media formats cannot be blank.")
        self.tv_media_formats = new_tv_media_formats
    
    def set_tv_is_remote_include(self: object, new_tv_is_remote_include: bool)-> None:
        """
        Sets the tv_is_remote_include attribute of the calling object to @new_tv_is_remote_include
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_is_remote_include) != bool:
            raise TypeError("Bad type: new TV is remote included.")
        if new_tv_is_remote_include != True and new_tv_is_remote_include != False:
            raise ValueError("new TV is remote included must be True or False.")
        self.tv_is_remote_include = new_tv_is_remote_include
    
    def set_tv_country_of_origin(self: object, new_tv_country_of_origin: str)-> None:
        """
        Sets the tv_country_of_origin attribute of the calling object to @new_tv_country_of_origin
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_country_of_origin) != str:
            raise TypeError("Bad type: new TV country of origin.")
        if len(new_tv_country_of_origin) == 0:
            raise ValueError("Country of origin cannot be empty.")
        
        self.tv_country_of_origin = new_tv_country_of_origin
    def set_tv_net_quantity(self: object, new_tv_net_quantity: int)-> None:
        """
        Sets the tv_net_quantity attribute of the calling object to @new_tv_net_quantity
        Before setting: TypeCheck and ValueCheck is performed.
        """
        if type(new_tv_net_quantity) != int:
            raise TypeError("Bad type: new TV net quantity.")
        if new_tv_net_quantity <= 0:
            raise ValueError("new TV net quantity must be positive.")
        
        self.tv_net_quantity = new_tv_net_quantity
    
    def Display(self: object):
        print("Brand: ", self.tv_brand)
        print("Manufacturer: ", self.tv_manufacturer)
        print("Model: ", self.tv_model)
        print("Model Year: ", self.tv_model_year)
        print("Product Dimensions: ", 
              self.tv_product_dimensions.length,
              "X",
              self.tv_product_dimensions.width,
              "X",
              self.tv_product_dimensions.height,
              ";",
              self.tv_product_dimensions.weight,
              "KG"
            )
        
        print("Number of batteries: ", self.tv_nr_batteries)
        print("Number of model: ", self.tv_nr_model)
        print("OS: ", self.tv_os)
        print("Hardware Interface: ", self.tv_hardare_interface)
        print("Graphics Coprocessor: ", self.tv_graphics_coprocessor)
        print("Tunner Technology: ", self.tv_tuner_technology)
        print("Features: ", self.tv_features)
        print("Mounting Hardware: ", self.tv_mounting_hardware)
        print("Display type: ", self.tv_dsp_type)
        print("Remote Control Technology: ", self.tv_remote_control_technology)
        print("Screen Resolution: ", 
              self.tv_screen_resolution.rs_width,
              "X",
              self.tv_screen_resolution.rs_height,
              "Pixels"
            )
        print("Audio Input: ", self.tv_audio_input)
        print("Audio Formats: ", self.tv_audio_formats)
        print("Wattage: ", self.tv_wattage)
        print("Voltage: ", self.tv_voltage)
        print("Power Source: ", self.tv_power_source)
        print("Batteries Included: ", self.tv_are_batteries_included)
        print("Batteries Required: ", self.tv_are_batteries_required)
        print("Refresh Rate: ", self.tv_refresh_rate)
        print("Number of USB ports: ", self.tv_nr_usb_ports)
        print("Connector Type: ", self.tv_connector_type)
        print("Media Formats: ", self.tv_media_formats)
        print("Remote Included: ", self.tv_is_remote_include)
        print("Country of Origin: ", self.tv_country_of_origin)
        print("Net Quantity: ", self.tv_net_quantity) 
        



def main()-> None:
    """
    This is the main function where the object is created by
    passing client specified attribute value as a actual parameter
    and display the final output.
    @input: passing client specified attribute value as a formal parameter to constructor of class Television
        Television(
            tv_brand: str,
            tv_manufacturer: str,
            tv_model: str,
            tv_model_year: int,
            tv_product_dimensions: ProductDimension,
            tv_nr_batteries: int,
            tv_nr_model: str,
            tv_os: list[str],
            tv_hardare_interface: list[str],
            tv_graphics_coprocessor: str,
            tv_tuner_technology: str,
            tv_features: list[str],
            tv_mounting_hardware: list[str],
            tv_dsp_type: str,
            tv_remote_control_technology: list[str],
            tv_screen_resolution: ProductResolution,
            tv_audio_input: list[str],
            tv_audio_formats: list[str],
            tv_wattage: int,
            tv_voltage: int,
            tv_power_source: str,
            tv_are_batteries_included: bool,
            tv_are_batteries_required: bool,
            tv_refresh_rate: int,
            tv_nr_usb_ports: int,
            tv_connector_type: list[str],
            tv_media_formats: list[str],
            tv_is_remote_include: bool,
            tv_country_of_origin: str,
            tv_net_quantity: int  
        )
    """

    television_object = Television(
        "Sony",
        "Sony, Sony India Private Limited.",
        "KD-55X74K",
        2022,
        ProductDimension(8.41, 124.31, 72.9, 14.5),
        2,
        "KD-55X74K",
        ["Google TV", "Android"],
        ["USB", "HDMI"],
        "X1 4K Processor",
        "DVB-T",
        ["Google TV", "Watchlist", "Voice Search", "Google Play"],
        ["1 LED TV", "1 Table-Top Stand", "1 AC Power Cord"],
        "4K HDR",
        ["IR", "Bluetooth"],
        ProductResolution(3840, 2160),
        ["USB", "HDMI"],
        ["mp3_audio", "wma"],
        20,
        240,
        "AC",
        True,
        True,
        60,
        2,
        ["Wi-Fi", "USB", "Ethernet", "HDMI"],
        ["MPEG", "AVI"],
        True,
        "India",
        1
    )
    header = "television product details:"
    print(header.upper()) 
    television_object.Display()

    #we can also get the attribute using getter methods
    #we can set the specific attribute using setter methods
    sys.exit(0)

main()
        
        
        
        
        
                        


            
            
            
            


        
            
        
         

        
        


           
        
        

    


        
